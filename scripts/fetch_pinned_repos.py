#!/usr/bin/env python3
"""Fetch pinned GitHub repositories for a user into Jekyll _data JSON."""

from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path


GRAPHQL_QUERY = """
query($login: String!) {
  user(login: $login) {
    pinnedItems(first: 6, types: REPOSITORY) {
      nodes {
        ... on Repository {
          name
          description
          url
          stargazerCount
          primaryLanguage {
            name
          }
        }
      }
    }
  }
}
"""


def main() -> int:
    token = os.environ.get("GITHUB_TOKEN", "").strip()
    login = os.environ.get("GITHUB_USER", "rdyson").strip()
    if not token:
        print("GITHUB_TOKEN is required to fetch pinned repos.", file=sys.stderr)
        return 1
    if not login:
        print("GITHUB_USER is required.", file=sys.stderr)
        return 1

    payload = json.dumps({"query": GRAPHQL_QUERY, "variables": {"login": login}}).encode(
        "utf-8"
    )

    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=payload,
        method="POST",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "User-Agent": "rdysondev-pinned-repos-fetcher",
        },
    )

    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            body = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        print(f"GitHub GraphQL HTTP error: {exc.code}", file=sys.stderr)
        return 1
    except urllib.error.URLError as exc:
        print(f"GitHub GraphQL request failed: {exc}", file=sys.stderr)
        return 1

    if body.get("errors"):
        print(f"GraphQL returned errors: {body['errors']}", file=sys.stderr)
        return 1

    nodes = (
        body.get("data", {})
        .get("user", {})
        .get("pinnedItems", {})
        .get("nodes", [])
    )
    repos = []
    for node in nodes:
        repos.append(
            {
                "name": node.get("name"),
                "description": node.get("description") or "",
                "url": node.get("url"),
                "language": (node.get("primaryLanguage") or {}).get("name"),
                "stars": node.get("stargazerCount"),
            }
        )

    out_path = Path("_data/pinned_repos.json")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(
        json.dumps(repos, indent=2, ensure_ascii=False, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {len(repos)} pinned repos to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

---
layout: post
title: "Bypass Chrome SSL warnings in local dev"
date: "2024-02-16 14:30:00"
categories: development
---

If you're developing a site locally, your URL is not `localhost`, and you don't have an SSL certificate set up, you've probably run into Chrome's warning about your connection to the site being insecure.

As a quick workaround, you can click "Proceed" and then type `thisisunsafe`.

If you're going to be working with the URL regularly and can't or don't want to set up an SSL certificate, you can permanently add the domain to Chrome's flags by going to the following feature flag page in Chrome and adding the domain to the "Insecure origins treated as secure" list and enabling that flag.

```
chrome://flags/#unsafely-treat-insecure-origin-as-secure
```

More info in this [Cybercafe article](https://cybercafe.dev/thisisunsafe-bypassing-chrome-security-warnings). Be careful with this setting—only use it for local dev.

---
layout: post
title: "Toggl hours in your macOS toolbar"
date: "2024-02-18 14:30:00"
categories: productivity
---

I use [Toggl](https://toggl.com) to keep track of the hours I've worked in a given week. Toggl has desktop and mobile apps to view and track your hours, but I wanted a way to easily see my current hours at a glance. I wrote this [toggl-xbar plugin](https://github.com/rdyson/toggl-xbar) to do just that.

[xbar](https://xbarapp.com) is a free macOS app lets you "put anything in your macOS menu bar", and you can easily write your own plugins. Plugins are effectively scripts with some additional metadata. If you can write a script to output the data you want, you can display that data in xbar.

You can find setup instructions in the [repo](https://github.com/rdyson/toggl-xbar). You can track your hours across one or more Toggl workspaces. For example if you only want to track hours for a specific work project you can specify that workspace.

![Toggl hours in macOS toolbar using xbar](assets/img/2024-02-18-toggl-xbar.png "Toggl hours in macOS toolbar using xbar")

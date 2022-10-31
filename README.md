# What does `kasaverde` do?

It makes your house greener! It does this by turning [TP-Link kasa](https://www.kasasmart.com/us/products/smart-plugs) smartplugs off when the electricity grid in your area is emitting more than normal, and turning it back on when the power grid is cleaner than normal. 

# What can I use it for?

`kasaverde` is very good for things that are always on, but don't need to be - so, a cordless toothbrush charger, a cordless beard trimmer charger, phone charger, lawn mower battery charger. Things that need to run a few hours, but you don't care if they run now or later.  `kasaverde` also works well for appliances like dehumidifiers.

If a thing in your home uses electricity, is compatible with a TP-Link Kasa smart plug, and will start doing what it does once the power comes back on, `kasaverde` can help. 

You probably shouldn't use `kasaverde` for your tea kettle, coffee maker, or toaster though, as those aren't really using power unless you want toast, coffee or tea. So, if you turn it on to use it, and it turns off when you're done, it's not a great fit.

# How does it know when the power is green?

`kasaverde` queries the very excellent [WattTime](https://www.watttime.org) API. You can read more about their methods [here](https://www.watttime.org/marginal-emissions-methodology/). 

# Does it work anywhere in the world?

Today, WattTime covers most of the USA, most of Canada, lots of Europe and Australia. Check their [coverage map](https://www.watttime.org/explorer), as they are adding new locations all the time.

# How do I start?

Well, you need a small computer to run it on right now. It's working well on raspberry pi devices, but could work on any Linux machine, a mac, or windows machine even, that is on the same IP network with the device you want to manage, for instance over your home wifi. From there, you need to register a username with WattTime's API, get your lattitude and longitude, and configure the app.


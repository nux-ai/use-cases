

import json
input_array = [
    {
        "href": "http://paulgraham.com/wisdom.html",
        "title": "Is it Worth Being Wise?"
    },
    {
        "href": "http://paulgraham.com/kids.html",
        "title": "Having Kids"
    },
    {
        "href": "http://paulgraham.com/selfindulgence.html",
        "title": "How to Lose Time and Money"
    },
    {
        "href": "http://paulgraham.com/greatwork.html",
        "title": "How to Do Great Work"
    },
    {
        "href": "http://paulgraham.com/getideas.html",
        "title": "How to Get New Ideas"
    },
    {
        "href": "http://paulgraham.com/read.html",
        "title": "The Need to Read"
    },
    {
        "href": "http://paulgraham.com/want.html",
        "title": "What You (Want to)* Want"
    },
    {
        "href": "http://paulgraham.com/alien.html",
        "title": "Alien Truth"
    },
    {
        "href": "http://paulgraham.com/users.html",
        "title": "What I've Learned from Users"
    },
    {
        "href": "http://paulgraham.com/heresy.html",
        "title": "Heresy"
    },
    {
        "href": "http://paulgraham.com/words.html",
        "title": "Putting Ideas into Words"
    },
    {
        "href": "http://paulgraham.com/goodtaste.html",
        "title": "Is There Such a Thing as Good Taste?"
    },
    {
        "href": "http://paulgraham.com/smart.html",
        "title": "Beyond Smart"
    },
    {
        "href": "http://paulgraham.com/weird.html",
        "title": "Weird Languages"
    },
    {
        "href": "http://paulgraham.com/hwh.html",
        "title": "How to Work Hard"
    },
    {
        "href": "http://paulgraham.com/own.html",
        "title": "A Project of One's Own"
    },
    {
        "href": "http://paulgraham.com/fn.html",
        "title": "Fierce Nerds"
    },
    {
        "href": "http://paulgraham.com/newideas.html",
        "title": "Crazy New Ideas"
    },
    {
        "href": "http://paulgraham.com/nft.html",
        "title": "An NFT That Saves Lives"
    },
    {
        "href": "http://paulgraham.com/real.html",
        "title": "The Real Reason to End the Death Penalty"
    },
    {
        "href": "http://paulgraham.com/richnow.html",
        "title": "How People Get Rich Now"
    },
    {
        "href": "http://paulgraham.com/simply.html",
        "title": "Write Simply"
    },
    {
        "href": "http://paulgraham.com/donate.html",
        "title": "Donate Unrestricted"
    },
    {
        "href": "http://paulgraham.com/worked.html",
        "title": "What I Worked On"
    },
    {
        "href": "http://paulgraham.com/earnest.html",
        "title": "Earnestness"
    },
    {
        "href": "http://paulgraham.com/ace.html",
        "title": "Billionaires Build"
    },
    {
        "href": "http://paulgraham.com/airbnbs.html",
        "title": "The Airbnbs"
    },
    {
        "href": "http://paulgraham.com/think.html",
        "title": "How to Think for Yourself"
    },
    {
        "href": "http://paulgraham.com/early.html",
        "title": "Early Work"
    },
    {
        "href": "http://paulgraham.com/wtax.html",
        "title": "Modeling a Wealth Tax"
    },
    {
        "href": "http://paulgraham.com/conformism.html",
        "title": "The Four Quadrants of Conformism"
    },
    {
        "href": "http://paulgraham.com/orth.html",
        "title": "Orthodox Privilege"
    },
    {
        "href": "http://paulgraham.com/cred.html",
        "title": "Coronavirus and Credibility"
    },
    {
        "href": "http://paulgraham.com/useful.html",
        "title": "How to Write Usefully"
    },
    {
        "href": "http://paulgraham.com/noob.html",
        "title": "Being a Noob"
    },
    {
        "href": "http://paulgraham.com/fh.html",
        "title": "Haters"
    },
    {
        "href": "http://paulgraham.com/mod.html",
        "title": "The Two Kinds of Moderate"
    },
    {
        "href": "http://paulgraham.com/fp.html",
        "title": "Fashionable Problems"
    },
    {
        "href": "http://paulgraham.com/kids.html",
        "title": "Having Kids"
    },
    {
        "href": "http://paulgraham.com/lesson.html",
        "title": "The Lesson to Unlearn"
    },
    {
        "href": "http://paulgraham.com/nov.html",
        "title": "Novelty and Heresy"
    },
    {
        "href": "http://paulgraham.com/genius.html",
        "title": "The Bus Ticket Theory of Genius"
    },
    {
        "href": "http://paulgraham.com/sun.html",
        "title": "General and Surprising"
    },
    {
        "href": "http://paulgraham.com/pow.html",
        "title": "Charisma / Power"
    },
    {
        "href": "http://paulgraham.com/disc.html",
        "title": "The Risk of Discovery"
    },
    {
        "href": "http://paulgraham.com/pgh.html",
        "title": "How to Make Pittsburgh a Startup Hub"
    },
    {
        "href": "http://paulgraham.com/vb.html",
        "title": "Life is Short"
    },
    {
        "href": "http://paulgraham.com/ineq.html",
        "title": "Economic Inequality"
    },
    {
        "href": "http://paulgraham.com/re.html",
        "title": "The Refragmentation"
    },
    {
        "href": "http://paulgraham.com/jessica.html",
        "title": "Jessica Livingston"
    },
    {
        "href": "http://paulgraham.com/bias.html",
        "title": "A Way to Detect Bias"
    },
    {
        "href": "http://paulgraham.com/talk.html",
        "title": "Write Like You Talk"
    },
    {
        "href": "http://paulgraham.com/aord.html",
        "title": "Default Alive or Default Dead?"
    },
    {
        "href": "http://paulgraham.com/safe.html",
        "title": "Why It's Safe for Founders to Be Nice"
    },
    {
        "href": "http://paulgraham.com/name.html",
        "title": "Change Your Name"
    },
    {
        "href": "http://paulgraham.com/altair.html",
        "title": "What Microsoft Is this the Altair Basic of?"
    },
    {
        "href": "http://paulgraham.com/ronco.html",
        "title": "The Ronco Principle"
    },
    {
        "href": "http://paulgraham.com/work.html",
        "title": "What Doesn't Seem Like Work?"
    },
    {
        "href": "http://paulgraham.com/corpdev.html",
        "title": "Don't Talk to Corp Dev"
    },
    {
        "href": "http://paulgraham.com/95.html",
        "title": "Let the Other 95% of Great Programmers In"
    },
    {
        "href": "http://paulgraham.com/ecw.html",
        "title": "How to Be an Expert in a Changing World"
    },
    {
        "href": "http://paulgraham.com/know.html",
        "title": "How You Know"
    },
    {
        "href": "http://paulgraham.com/pinch.html",
        "title": "The Fatal Pinch"
    },
    {
        "href": "http://paulgraham.com/mean.html",
        "title": "Mean People Fail"
    },
    {
        "href": "http://paulgraham.com/before.html",
        "title": "Before the Startup"
    },
    {
        "href": "http://paulgraham.com/fr.html",
        "title": "How to Raise Money"
    },
    {
        "href": "http://paulgraham.com/herd.html",
        "title": "Investor Herd Dynamics"
    },
    {
        "href": "http://paulgraham.com/convince.html",
        "title": "How to Convince Investors"
    },
    {
        "href": "http://paulgraham.com/ds.html",
        "title": "Do Things that Don't Scale"
    },
    {
        "href": "http://paulgraham.com/invtrend.html",
        "title": "Startup Investing Trends"
    },
    {
        "href": "http://paulgraham.com/startupideas.html",
        "title": "How to Get Startup Ideas"
    },
    {
        "href": "http://paulgraham.com/hw.html",
        "title": "The Hardware Renaissance"
    },
    {
        "href": "http://paulgraham.com/growth.html",
        "title": "Startup = Growth"
    },
    {
        "href": "http://paulgraham.com/swan.html",
        "title": "Black Swan Farming"
    },
    {
        "href": "http://paulgraham.com/todo.html",
        "title": "The Top of My Todo List"
    },
    {
        "href": "http://paulgraham.com/speak.html",
        "title": "Writing and Speaking"
    },
    {
        "href": "http://paulgraham.com/ycstart.html",
        "title": "How Y Combinator Started"
    },
    {
        "href": "http://paulgraham.com/property.html",
        "title": "Defining Property"
    },
    {
        "href": "http://paulgraham.com/ambitious.html",
        "title": "Frighteningly Ambitious Startup Ideas"
    },
    {
        "href": "http://paulgraham.com/word.html",
        "title": "A Word to the Resourceful"
    },
    {
        "href": "http://paulgraham.com/schlep.html",
        "title": "Schlep Blindness"
    },
    {
        "href": "http://paulgraham.com/vw.html",
        "title": "Snapshot: Viaweb, June 1998"
    },
    {
        "href": "http://paulgraham.com/hubs.html",
        "title": "Why Startup Hubs Work"
    },
    {
        "href": "http://paulgraham.com/patentpledge.html",
        "title": "The Patent Pledge"
    },
    {
        "href": "http://paulgraham.com/airbnb.html",
        "title": "Subject: Airbnb"
    },
    {
        "href": "http://paulgraham.com/control.html",
        "title": "Founder Control"
    },
    {
        "href": "http://paulgraham.com/tablets.html",
        "title": "Tablets"
    },
    {
        "href": "http://paulgraham.com/founders.html",
        "title": "What We Look for in Founders"
    },
    {
        "href": "http://paulgraham.com/superangels.html",
        "title": "The New Funding Landscape"
    },
    {
        "href": "http://paulgraham.com/seesv.html",
        "title": "Where to See Silicon Valley"
    },
    {
        "href": "http://paulgraham.com/hiresfund.html",
        "title": "High Resolution Fundraising "
    },
    {
        "href": "http://paulgraham.com/yahoo.html",
        "title": "What Happened to Yahoo "
    },
    {
        "href": "http://paulgraham.com/future.html",
        "title": "The Future of Startup Funding "
    },
    {
        "href": "http://paulgraham.com/addiction.html",
        "title": "The Acceleration of Addictiveness"
    },
    {
        "href": "http://paulgraham.com/top.html",
        "title": "The Top Idea in Your Mind "
    },
    {
        "href": "http://paulgraham.com/selfindulgence.html",
        "title": "How to Lose Time and Money "
    },
    {
        "href": "http://paulgraham.com/organic.html",
        "title": "Organic Startup Ideas"
    },
    {
        "href": "http://paulgraham.com/apple.html",
        "title": "Apple's Mistake"
    },
    {
        "href": "http://paulgraham.com/really.html",
        "title": "What Startups Are Really Like"
    },
    {
        "href": "http://paulgraham.com/discover.html",
        "title": "Persuade xor Discover "
    },
    {
        "href": "http://paulgraham.com/publishing.html",
        "title": "Post-Medium Publishing"
    },
    {
        "href": "http://paulgraham.com/nthings.html",
        "title": "The List of N Things"
    },
    {
        "href": "http://paulgraham.com/determination.html",
        "title": "The Anatomy of Determination "
    },
    {
        "href": "http://paulgraham.com/kate.html",
        "title": "What Kate Saw in Silicon Valley "
    },
    {
        "href": "http://paulgraham.com/segway.html",
        "title": "The Trouble with the Segway"
    },
    {
        "href": "http://paulgraham.com/ramenprofitable.html",
        "title": "Ramen Profitable"
    },
    {
        "href": "http://paulgraham.com/makersschedule.html",
        "title": "Maker's Schedule, Manager's Schedule "
    },
    {
        "href": "http://paulgraham.com/revolution.html",
        "title": "A Local Revolution?"
    },
    {
        "href": "http://paulgraham.com/twitter.html",
        "title": "Why Twitter is a Big Deal"
    },
    {
        "href": "http://paulgraham.com/foundervisa.html",
        "title": "The Founder Visa"
    },
    {
        "href": "http://paulgraham.com/5founders.html",
        "title": "Five Founders"
    },
    {
        "href": "http://paulgraham.com/relres.html",
        "title": "Relentlessly Resourceful"
    },
    {
        "href": "http://paulgraham.com/angelinvesting.html",
        "title": "How to Be an Angel Investor"
    },
    {
        "href": "http://paulgraham.com/convergence.html",
        "title": "Why TV Lost"
    },
    {
        "href": "http://paulgraham.com/maybe.html",
        "title": "Can You Buy a Silicon Valley? Maybe."
    },
    {
        "href": "http://paulgraham.com/hackernews.html",
        "title": "What I've Learned from Hacker News"
    },
    {
        "href": "http://paulgraham.com/13sentences.html",
        "title": "Startups in 13 Sentences"
    },
    {
        "href": "http://paulgraham.com/identity.html",
        "title": "Keep Your Identity Small "
    },
    {
        "href": "http://paulgraham.com/credentials.html",
        "title": "After Credentials"
    },
    {
        "href": "http://paulgraham.com/divergence.html",
        "title": "Could VC be a Casualty of the Recession?"
    },
    {
        "href": "http://paulgraham.com/highres.html",
        "title": "The High-Res Society"
    },
    {
        "href": "http://paulgraham.com/artistsship.html",
        "title": "The Other Half of \"Artists Ship\" "
    },
    {
        "href": "http://paulgraham.com/badeconomy.html",
        "title": "Why to Start a Startup in a Bad Economy"
    },
    {
        "href": "http://paulgraham.com/fundraising.html",
        "title": "A Fundraising Survival Guide"
    },
    {
        "href": "http://paulgraham.com/prcmc.html",
        "title": "The Pooled-Risk Company Management Company"
    },
    {
        "href": "http://paulgraham.com/cities.html",
        "title": "Cities and Ambition"
    },
    {
        "href": "http://paulgraham.com/distraction.html",
        "title": "Disconnecting Distraction"
    },
    {
        "href": "http://paulgraham.com/lies.html",
        "title": "Lies We Tell Kids"
    },
    {
        "href": "http://paulgraham.com/good.html",
        "title": "Be Good"
    },
    {
        "href": "http://paulgraham.com/googles.html",
        "title": "Why There Aren't More Googles"
    },
    {
        "href": "http://paulgraham.com/heroes.html",
        "title": "Some Heroes"
    },
    {
        "href": "http://paulgraham.com/disagree.html",
        "title": "How to Disagree"
    },
    {
        "href": "http://paulgraham.com/boss.html",
        "title": "You Weren't Meant to Have a Boss"
    },
    {
        "href": "http://paulgraham.com/ycombinator.html",
        "title": "A New Venture Animal"
    },
    {
        "href": "http://paulgraham.com/trolls.html",
        "title": "Trolls"
    },
    {
        "href": "http://paulgraham.com/newthings.html",
        "title": "Six Principles for Making New Things"
    },
    {
        "href": "http://paulgraham.com/startuphubs.html",
        "title": "Why to Move to a Startup Hub"
    },
    {
        "href": "http://paulgraham.com/webstartups.html",
        "title": "The Future of Web Startups"
    },
    {
        "href": "http://paulgraham.com/philosophy.html",
        "title": "How to Do Philosophy"
    },
    {
        "href": "http://paulgraham.com/colleges.html",
        "title": "News from the Front"
    },
    {
        "href": "http://paulgraham.com/die.html",
        "title": "How Not to Die"
    },
    {
        "href": "http://paulgraham.com/head.html",
        "title": "Holding a Program in One's Head"
    },
    {
        "href": "http://paulgraham.com/stuff.html",
        "title": "Stuff"
    },
    {
        "href": "http://paulgraham.com/equity.html",
        "title": "The Equity Equation"
    },
    {
        "href": "http://paulgraham.com/unions.html",
        "title": "An Alternative Theory of Unions"
    },
    {
        "href": "http://paulgraham.com/guidetoinvestors.html",
        "title": "The Hacker's Guide to Investors"
    },
    {
        "href": "http://paulgraham.com/judgement.html",
        "title": "Two Kinds of Judgement"
    },
    {
        "href": "http://paulgraham.com/microsoft.html",
        "title": "Microsoft is Dead"
    },
    {
        "href": "http://paulgraham.com/notnot.html",
        "title": "Why to Not Not Start a Startup"
    },
    {
        "href": "http://paulgraham.com/wisdom.html",
        "title": "Is It Worth Being Wise?"
    },
    {
        "href": "http://paulgraham.com/foundersatwork.html",
        "title": "Learning from Founders"
    },
    {
        "href": "http://paulgraham.com/goodart.html",
        "title": "How Art Can Be Good"
    },
    {
        "href": "http://paulgraham.com/startupmistakes.html",
        "title": "The 18 Mistakes That Kill Startups"
    },
    {
        "href": "http://paulgraham.com/mit.html",
        "title": "A Student's Guide to Startups"
    },
    {
        "href": "http://paulgraham.com/investors.html",
        "title": "How to Present to Investors"
    },
    {
        "href": "http://paulgraham.com/copy.html",
        "title": "Copy What You Like"
    },
    {
        "href": "http://paulgraham.com/island.html",
        "title": "The Island Test"
    },
    {
        "href": "http://paulgraham.com/marginal.html",
        "title": "The Power of the Marginal"
    },
    {
        "href": "http://paulgraham.com/america.html",
        "title": "Why Startups Condense in America"
    },
    {
        "href": "http://paulgraham.com/siliconvalley.html",
        "title": "How to Be Silicon Valley"
    },
    {
        "href": "http://paulgraham.com/startuplessons.html",
        "title": "The Hardest Lessons for Startups to Learn"
    },
    {
        "href": "http://paulgraham.com/randomness.html",
        "title": "See Randomness"
    },
    {
        "href": "http://paulgraham.com/softwarepatents.html",
        "title": "Are Software Patents Evil?"
    },
    {
        "href": "http://paulgraham.com/6631327.html",
        "title": "6,631,372"
    },
    {
        "href": "http://paulgraham.com/whyyc.html",
        "title": "Why YC"
    },
    {
        "href": "http://paulgraham.com/love.html",
        "title": "How to Do What You Love"
    },
    {
        "href": "http://paulgraham.com/procrastination.html",
        "title": "Good and Bad Procrastination"
    },
    {
        "href": "http://paulgraham.com/web20.html",
        "title": "Web 2.0"
    },
    {
        "href": "http://paulgraham.com/startupfunding.html",
        "title": "How to Fund a Startup"
    },
    {
        "href": "http://paulgraham.com/vcsqueeze.html",
        "title": "The Venture Capital Squeeze"
    },
    {
        "href": "http://paulgraham.com/ideas.html",
        "title": "Ideas for Startups"
    },
    {
        "href": "http://paulgraham.com/sfp.html",
        "title": "What I Did this Summer"
    },
    {
        "href": "http://paulgraham.com/inequality.html",
        "title": "Inequality and Risk"
    },
    {
        "href": "http://paulgraham.com/ladder.html",
        "title": "After the Ladder"
    },
    {
        "href": "http://paulgraham.com/opensource.html",
        "title": "What Business Can Learn from Open Source"
    },
    {
        "href": "http://paulgraham.com/hiring.html",
        "title": "Hiring is Obsolete"
    },
    {
        "href": "http://paulgraham.com/submarine.html",
        "title": "The Submarine"
    },
    {
        "href": "http://paulgraham.com/bronze.html",
        "title": "Why Smart People Have Bad Ideas"
    },
    {
        "href": "http://paulgraham.com/mac.html",
        "title": "Return of the Mac"
    },
    {
        "href": "http://paulgraham.com/writing44.html",
        "title": "Writing, Briefly"
    },
    {
        "href": "http://paulgraham.com/college.html",
        "title": "Undergraduation"
    },
    {
        "href": "http://paulgraham.com/venturecapital.html",
        "title": "A Unified Theory of VC Suckage"
    },
    {
        "href": "http://paulgraham.com/start.html",
        "title": "How to Start a Startup"
    },
    {
        "href": "http://paulgraham.com/hs.html",
        "title": "What You'll Wish You'd Known"
    },
    {
        "href": "http://paulgraham.com/usa.html",
        "title": "Made in USA"
    },
    {
        "href": "http://paulgraham.com/charisma.html",
        "title": "It's Charisma, Stupid"
    },
    {
        "href": "http://paulgraham.com/polls.html",
        "title": "Bradley's Ghost"
    },
    {
        "href": "http://paulgraham.com/laundry.html",
        "title": "A Version 1.0"
    },
    {
        "href": "http://paulgraham.com/bubble.html",
        "title": "What the Bubble Got Right"
    },
    {
        "href": "http://paulgraham.com/essay.html",
        "title": "The Age of the Essay"
    },
    {
        "href": "http://paulgraham.com/pypar.html",
        "title": "The Python Paradox"
    },
    {
        "href": "http://paulgraham.com/gh.html",
        "title": "Great Hackers"
    },
    {
        "href": "http://paulgraham.com/gap.html",
        "title": "Mind the Gap"
    },
    {
        "href": "http://paulgraham.com/wealth.html",
        "title": "How to Make Wealth"
    },
    {
        "href": "http://paulgraham.com/gba.html",
        "title": "The Word \"Hacker\""
    },
    {
        "href": "http://paulgraham.com/say.html",
        "title": "What You Can't Say"
    },
    {
        "href": "http://paulgraham.com/ffb.html",
        "title": "Filters that Fight Back"
    },
    {
        "href": "http://paulgraham.com/hp.html",
        "title": "Hackers and Painters"
    },
    {
        "href": "http://paulgraham.com/iflisp.html",
        "title": "If Lisp is So Great"
    },
    {
        "href": "http://paulgraham.com/hundred.html",
        "title": "The Hundred-Year Language"
    },
    {
        "href": "http://paulgraham.com/nerds.html",
        "title": "Why Nerds are Unpopular"
    },
    {
        "href": "http://paulgraham.com/better.html",
        "title": "Better Bayesian Filtering"
    },
    {
        "href": "http://paulgraham.com/desres.html",
        "title": "Design and Research"
    },
    {
        "href": "http://paulgraham.com/spam.html",
        "title": "A Plan for Spam"
    },
    {
        "href": "http://paulgraham.com/icad.html",
        "title": "Revenge of the Nerds"
    },
    {
        "href": "http://paulgraham.com/power.html",
        "title": "Succinctness is Power"
    },
    {
        "href": "http://paulgraham.com/fix.html",
        "title": "What Languages Fix"
    },
    {
        "href": "http://paulgraham.com/taste.html",
        "title": "Taste for Makers"
    },
    {
        "href": "http://paulgraham.com/noop.html",
        "title": "Why Arc Isn't Especially Object-Oriented"
    },
    {
        "href": "http://paulgraham.com/diff.html",
        "title": "What Made Lisp Different"
    },
    {
        "href": "http://paulgraham.com/road.html",
        "title": "The Other Road Ahead"
    },
    {
        "href": "http://paulgraham.com/rootsoflisp.html",
        "title": "The Roots of Lisp"
    },
    {
        "href": "http://paulgraham.com/langdes.html",
        "title": "Five Questions about Language Design"
    },
    {
        "href": "http://paulgraham.com/popular.html",
        "title": "Being Popular"
    },
    {
        "href": "http://paulgraham.com/javacover.html",
        "title": "Java's Cover"
    },
    {
        "href": "http://paulgraham.com/avg.html",
        "title": "Beating the Averages"
    },
    {
        "href": "http://paulgraham.com/lwba.html",
        "title": "Lisp for Web-Based Applications"
    },
    {
        "href": "http://paulgraham.com/https://sep.turbifycdn.com/ty/cdn/paulgraham/acl1.txt?t=1693834979&",
        "title": "Chapter 1 of Ansi Common Lisp"
    },
    {
        "href": "http://paulgraham.com/https://sep.turbifycdn.com/ty/cdn/paulgraham/acl2.txt?t=1693834979&",
        "title": "Chapter 2 of Ansi Common Lisp"
    },
    {
        "href": "http://paulgraham.com/progbot.html",
        "title": "Programming Bottom-Up"
    },
    {
        "href": "http://paulgraham.com/prop62.html",
        "title": "This Year We Can End the Death Penalty in California"
    }
]


def slugify(text):
    return ''.join(char.lower() if char.isalnum() else '-' for char in text).strip('-')


output_array = []
for item in input_array:
    transformed_item = {
        "source_id": "paul_graham_essays",
        "type": "website",
        "path": item.get("href", ""),
        "metadata": {"title": item.get("title", "")}
    }
    output_array.append(transformed_item)

with open('transformed_array.json', 'w') as f:
    json.dump(output_array, f, indent=4)

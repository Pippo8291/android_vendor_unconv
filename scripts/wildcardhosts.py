from os.path import join
import sys


def replace_with_wildcards(args):
    new = []
    spam_domains = [
        "-active.mobi",
        "-bankq.com",
        ".000webhostapp.com",
        ".0236.info",
        ".0xf4a5.tk",
        ".207.net",
        ".247realmedia.com",
        ".2cnt.net",
        ".2mdn.net",
        ".2o7.net",
        ".302br.net",
        ".360.cn",
        ".360safe.com",
        ".3lift.com",
        ".51yes.com",
        ".a.volvelle.tech",
        ".a8.net",
        ".abnad.net",
        ".ace.advertising.com",
        ".actonsoftware.com",
        ".ad-score.com",
        ".ad-stir.com",
        ".ad.daum.net",
        ".ad.dotandad.com",
        ".ad.org.vn",
        ".ad.tomshardware.com",
        ".ad.xiaomi.com",
        ".adacado.com",
        ".adadapter.netzathleten-media.de",
        ".adalyser.com",
        ".adasiaholdings.com",
        ".adbureau.net",
        ".adcolony.com",
        ".addfreestats.com",
        ".addthis.com",
        ".adflex.vn",
        ".adform.com",
        ".adform.net",
        ".adfuture.cn",
        ".adhese.com",
        ".adition.com",
        ".adkmob.com",
        ".adledge.com",
        ".adlightning.com",
        ".adlooxtracking.com",
        ".admaster.com.cn",
        ".admicro.vn",
        ".admob.com",
        ".adnow.com",
        ".adnxs.com",
        ".adocean.pl",
        ".adonweb.ru",
        ".adotmob.com",
        ".adplus.co.id",
        ".adprotect.net",
        ".adpushup.com",
        ".adrevolver.com",
        ".adroll.com",
        ".ads.httpool.com",
        ".ads.link4ads.com",
        ".ads.oppomobile.com",
        ".ads.t-online.de",
        ".ads.tremorhub.com",
        ".adsafeprotected.com",
        ".adscience.nl",
        ".adserver.co.il",
        ".adserver.yahoo.com",
        ".adshostnet.com",
        ".adskeeper.co.uk",
        ".adsmoloco.com",
        ".adsplay.net",
        ".adsplay.xyz",
        ".adspruce.com",
        ".adsrvr.org",
        ".adswizz.com",
        ".adtech.de",
        ".adtech.fr",
        ".adtech.us",
        ".adtechus.com",
        ".adtlgc.com",
        ".adultfriendfinder.com",
        ".adups.cn",
        ".adups.com",
        ".adv.vz.ru",
        ".advance.net",
        ".adventori.com",
        ".advertik.com",
        ".advertising.com",
        ".advertising.yahoo.com",
        ".advertnative.com",
        ".advertserve.com",
        ".allaff.0649.pics",
        ".alldownloads.hapc.gdn",
        ".alphonso.tv",
        ".am15.net",
        ".amazingcounters.com",
        ".amazon-adsystem.com",
        ".ambientplatform.vn",
        ".amp.permutive.com",
        ".anthill.vn",
        ".aol.com",
        ".appboy.com",
        ".appier.net",
        ".applovin.com",
        ".apps.co.pl",
        ".appsflyer.com",
        ".appsgeyser.com",
        ".apptimize.com",
        ".as-eu.falkag.net",
        ".as-us.falkag.net",
        ".asian-flu-vaccine.com",
        ".asvoxod.ru",
        ".atm.youku.com",
        ".atwola.com",
        ".authedmine.com",
        ".axiatraders.com",
        ".b-cdn.net",
        ".baidu.com",
        ".bbelements.com",
        ".beginads.com",
        ".bidgear.com",
        ".bidvertiser.com",
        ".bilsyndication.com",
        ".bitterstrawberry.com",
        ".bloger.index.hr",
        ".bounceexchange.com",
        ".bounceme.net",
        ".brand.zing.vn",
        ".brandreachsys.com",
        ".bravenet.com",
        ".braze.com",
        ".buzzclicks.com",
        ".c.richmetrics.com",
        ".casalemedia.com",
        ".cedexis.com",
        ".checkm8.com",
        ".cinci.rr.com",
        ".cityads.com",
        ".clickon.co.il",
        ".cn.miaozhen.com",
        ".coccoc.com",
        ".coin-hive.com",
        ".coinhive.com",
        ".collector.snplow.net",
        ".com-notice.info",
        ".com.akadns.net",
        ".connextra.com",
        ".contentabc.com",
        ".conviva.com",
        ".count.brat-online.ro",
        ".counter.bloke.com",
        ".cpa.clicksure.com",
        ".cqcounter.com",
        ".criteo.com",
        ".crittercism.com",
        ".crwdcntrl.net",
        ".crypto-loot.com",
        ".crypto.csgocpu.com",
        ".cxense.com",
        ".dartsearch.net",
        ".datatrics.com",
        ".ddns.name",
        ".de.lv",
        ".delta-boa.com",
        ".deltadna.net",
        ".demdex.net",
        ".dol.ru",
        ".dotomi.com",
        ".doubleclick.net",
        ".doublepimp.com",
        ".doubleverify.com",
        ".duapps.com",
        ".duckdns.org",
        ".dynamicyield.com",
        ".ec.yimg.com",
        ".eclick.vn",
        ".economicoutlook.net",
        ".edgekey.net",
        ".edgesuite.net",
        ".elasticbeanstalk.com",
        ".eloqua.com",
        ".engageya.com",
        ".engine.adglare.net",
        ".ero-advertising.com",
        ".etargetnet.com",
        ".exacttarget.com",
        ".exelator.com",
        ".extreme-dm.com",
        ".face2trade.com",
        ".fastclick.net",
        ".fc2.com",
        ".fff.com.vn",
        ".file.co.pl",
        ".findprofile.net.pl",
        ".focalink.com",
        ".fop.jp",
        ".foresee.com",
        ".fotoable.com",
        ".fotoable.net",
        ".fractionalmedia.com",
        ".free-counter.co.uk",
        ".freelogs.com",
        ".fuckyoucash.com",
        ".fuseplatform.net",
        ".fyber.com",
        ".gameads.io",
        ".gemius.pl",
        ".generals.ea.com",
        ".geovisite.com",
        ".go2affise.com",
        ".go2cloud.org",
        ".gocunt.com",
        ".goforandroid.com",
        ".gostats.com",
        ".grandonmedia.com",
        ".grapeshot.co.uk",
        ".hadj1.adjuggler.net",
        ".hadj7.adjuggler.net",
        ".hashvault.pro",
        ".hemnes.win",
        ".hitbox.com",
        ".hittail.com",
        ".home.sapo.pt",
        ".hop.clickbank.net",
        ".hpg.com.br",
        ".hut1.ru",
        ".hyperbanner.net",
        ".hyprmx.com",
        ".i-mobile.co.jp",
        ".i2i.jp",
        ".iadsdk.apple.com",
        ".ic-live.com",
        ".iesnare.co.uk",
        ".ifdef.jp",
        ".ig.com.br",
        ".igexin.com",
        ".immomo.com",
        ".imonomy.com",
        ".impact-ad.jp",
        ".imrworldwide.com",
        ".in.net",
        ".inhit.com",
        ".init.cedexis-radar.net",
        ".inmobi.com",
        ".innity.com",
        ".innity.net",
        ".innovid.com",
        ".insightexpress.com",
        ".inteleksys.com",
        ".intellitxt.com",
        ".intentiq.com",
        ".interpolls.com",
        ".ipromote.com",
        ".is-best.net",
        ".isnssdk.com",
        ".ivwbox.de",
        ".iwanttodeliver.com",
        ".jp.eimg.jp",
        ".jumptap.com",
        ".justclick.ru",
        ".justpremium.com",
        ".kameleoon.com",
        ".kargo.com",
        ".kissmetrics.com",
        ".kontera.com",
        ".krxd.net",
        ".landing.comcontent.net",
        ".lavanetwork.net",
        ".lfstmedia.com",
        ".liftoff.io",
        ".lijit.com",
        ".lionmobi.com",
        ".lip.st",
        ".liveadvert.com",
        ".livejasmin.com",
        ".livetex.ru",
        ".local.vmsn.de",
        ".mangoads.vn",
        ".marketgid.com",
        ".marketo.com",
        ".marketo.net",
        ".marketscore.com",
        ".mathtag.com",
        ".maynemyltf.netdna-cdn.com",
        ".media.net",
        ".mediav.com",
        ".mediaz.vn",
        ".met.vgwort.de",
        ".mgid.com",
        ".mgr.consensu.org",
        ".mirror.co.uk",
        ".misstrends.com",
        ".mistat.intl.xiaomi.com",
        ".mmstat.com",
        ".moatads.com",
        ".mobileapptracking.com",
        ".monerise.com",
        ".mookie1.com",
        ".mtree.com",
        ".mybluemix.net",
        ".mydas.mobi",
        ".mystat-in.net",
        ".nastydollars.com",
        ".net-filter.com",
        ".newrelic.com",
        ".novaon.asia",
        ".novaonx.com",
        ".nuggad.net",
        ".nyc1.targetnet.com",
        ".oewabox.at",
        ".offermatica.com",
        ".offerx.co.uk",
        ".ogury.io",
        ".omniture.com",
        ".omtrdc.net",
        ".onion.pet",
        ".onscroll.com",
        ".opentracker.net",
        ".openx.net",
        ".opinionlab.com",
        ".optimizely.com",
        ".outbrain.com",
        ".outster.com",
        ".oxcash.com",
        ".p.xpanama.net",
        ".p2l.info",
        ".paycount.com",
        ".pcloadletter.quhu.info",
        ".perf.overture.com",
        ".petrovka.info",
        ".pinsightmedia.com",
        ".polybuild.ru",
        ".poorgoddaay.com",
        ".popmarker.com",
        ".popunder.loading-delivery1.com",
        ".presage.io",
        ".prod.criteo.net",
        ".prod.millennialmedia.com",
        ".propellerads.com",
        ".pubmatic.com",
        ".puhtml.com",
        ".pushengage.com",
        ".pushwoosh.com",
        ".putags.com",
        ".qq.com",
        ".quantserve.com",
        ".r.axf8.net",
        ".radar11ab.co.uk",
        ".rakuten.co.jp",
        ".rayjump.com",
        ".rce.veeseo.com",
        ".reporo.net",
        ".research.de.com",
        ".revcontent.com",
        ".revolvermaps.com",
        ".roboinside.me",
        ".rtk.io",
        ".ru.redtram.com",
        ".rubiconproject.com",
        ".s.ad6media.fr",
        ".s.moatpixel.com",
        ".s290.meetrics.net",
        ".sakura.ne.jp",
        ".scorecardresearch.com",
        ".searchteria.co.jp",
        ".segmentify.com",
        ".send.microad.jp",
        ".sextracker.be",
        ".sextracker.com",
        ".shengen.ru",
        ".shinobi.jp",
        ".shinystat.com",
        ".sina.com.cn",
        ".siteintercept.qualtrics.com",
        ".sitemeter.com",
        ".sitestats.com",
        ".skimlinks.com",
        ".smaato.net",
        ".smartadserver.com",
        ".sms13.de",
        ".socialbakers.com",
        ".solution.weborama.fr",
        ".sonobi.com",
        ".sp1.convertro.com",
        ".spotxchange.com",
        ".springserve.com",
        ".spylog.com",
        ".ssacdn.com",
        ".ssl.fastly.net",
        ".startappservice.com",
        ".stat.ku6.com",
        ".stat.pl",
        ".stat24.com",
        ".static.planet49.com",
        ".stats.esomniture.com",
        ".sumologic.com",
        ".super-promo.quhu.info",
        ".supersonicads.com",
        ".superstats.com",
        ".surf-town.net",
        ".survey7.adsservingtwig.xyz",
        ".sv.publicus.com",
        ".switchadhub.com",
        ".swrve.com",
        ".t.domdex.com",
        ".taboola.com",
        ".tactilews.com",
        ".tanx.com",
        ".taobao.com",
        ".tealiumiq.com",
        ".telemetry.microsoft.com",
        ".theblog.com.br",
        ".thinknearhub.com",
        ".thruport.com",
        ".tmweb.ru",
        ".toboads.com",
        ".top.list.ru",
        ".topbucks.com",
        ".trackalyzer.com",
        ".tradedoubler.com",
        ".trafficjunky.net",
        ".tremorhub.com",
        ".tribalfusion.com",
        ".tubemogul.com",
        ".turn.com",
        ".tvpage.com",
        ".ucweb.com",
        ".ulink.adjust.com",
        ".umeng.com",
        ".unbounce.com",
        ".unity3d.com",
        ".unrulymedia.com",
        ".uol.com.br",
        ".upalytics.com",
        ".ur.gcion.com",
        ".us.publicus.com",
        ".usebutton.com",
        ".usesfathom.com",
        ".v.fwmrm.net",
        ".vcmedia.vn",
        ".ventanasyaluminios.com.mx",
        ".vertamedia.com",
        ".videoplaza.tv",
        ".vietnamnetad.vn",
        ".vivo.com.cn",
        ".vivoglobal.com",
        ".vmsn.de",
        ".vo.llnwd.net",
        ".voiceads.cn",
        ".voluumtrk.com",
        ".vpptechnologies.com",
        ".vrvm.com",
        ".vungle.com",
        ".walla.co.il",
        ".web.hosting-test.net",
        ".webstats.motigo.com",
        ".webtrekk.net",
        ".ws.tidafors.xyz",
        ".xiti.com",
        ".xn--p1ai",
        ".xp1.ru4.com",
        ".yieldify.com",
        ".yieldmo.com",
        ".yinzcam.com",
        ".younetmedia.com",
        ".z19.web.core.windows.net",
        ".zadn.vn",
        ".zedo.com",
        ".zeroredirect1.com",
        ".zeroredirect2.com",
        ".ziyu.net",
    ]

    if len(args) == 2:
        input_file_path = args[0]
        output_file_path = args[1]

    else:
        raise ValueError("Wrong number of arguments %s" % len(args))

    with open(input_file_path, "r") as fip:
        new = fip.readlines()
        print("Initial size: ", len(new))

    with open(join(output_file_path, "hosts_unconv_w"), "w") as fop:
        i = 0
        for redirect in new:
            if any(item in redirect for item in spam_domains):
                continue
            fop.write(redirect)
            i += 1
        for domains in spam_domains:
            fop.write(f"0.0.0.0 *{domains}\n")
            i += 1
    print("Final   size: ", i)


if __name__ == "__main__":
    replace_with_wildcards(sys.argv[1:])

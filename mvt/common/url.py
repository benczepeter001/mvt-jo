# Mobile Verification Toolkit (MVT)
# Copyright (c) 2021 The MVT Project Authors.
# Use of this software is governed by the MVT License 1.1 that can be found at
#   https://license.mvt.re/1.1/

import requests
from tld import get_tld

SHORTENER_DOMAINS = [
    "1link.in",
    "1url.com",
    "2big.at",
    "2pl.us",
    "2tu.us",
    "2ya.com",
    "4url.cc",
    "6url.com",
    "a2a.me",
    "abbrr.com",
    "adf.ly",
    "adjix.com",
    "a.gg",
    "alturl.com",
    "a.nf",
    "atu.ca",
    "b23.ru",
    "bacn.me",
    "bit.ly",
    "bit.do",
    "bkite.com",
    "bloat.me",
    "budurl.com",
    "buff.ly",
    "buk.me",
    "burnurl.com",
    "chilp.it",
    "clck.ru",
    "clickmeter.com",
    "cli.gs",
    "c-o.in",
    "cort.as",
    "cut.ly",
    "cuturl.com",
    "decenturl.com",
    "decenturl.com",
    "dfl8.me",
    "digbig.com",
    "digg.com",
    "doiop.com",
    "dwarfurl.com",
    "dy.fi",
    "easyuri.com",
    "easyurl.net",
    "eepurl.com",
    "esyurl.com",
    "ewerl.com",
    "fa.b",
    "fff.to",
    "ff.im",
    "fhurl.com",
    "fire.to",
    "firsturl.de",
    "flic.kr",
    "fly2.ws",
    "fon.gs",
    "fwd4.me",
    "gl.am",
    "go2cut.com",
    "go2.me",
    "go.9nl.com",
    "goo.gl",
    "goshrink.com",
    "gowat.ch",
    "gri.ms",
    "gurl.es",
    "hellotxt.com",
    "hex.io",
    "hover.com",
    "href.in",
    "htxt.it",
    "hugeurl.com",
    "hurl.it",
    "hurl.me",
    "hurl.ws",
    "icanhaz.com",
    "idek.net",
    "inreply.to",
    "iscool.net",
    "is.gd",
    "iterasi.net",
    "jijr.com",
    "jmp2.net",
    "just.as",
    "kissa.be",
    "kl.am",
    "klck.me",
    "korta.nu",
    "krunchd.com",
    "liip.to",
    "liltext.com",
    "lin.cr",
    "linkbee.com",
    "linkbun.ch",
    "liurl.cn",
    "lnk.gd",
    "lnk.in",
    "ln-s.net",
    "ln-s.ru",
    "loopt.us",
    "lru.jp",
    "lt.tl",
    "lurl.no",
    "metamark.net",
    "migre.me",
    "minilien.com",
    "miniurl.com",
    "minurl.fr",
    "moourl.com",
    "myurl.in",
    "ne1.net",
    "njx.me",
    "nn.nf",
    "notlong.com",
    "nsfw.in",
    "om.ly",
    "ow.ly",
    "o-x.fr",
    "pd.am",
    "pic.gd",
    "ping.fm",
    "piurl.com",
    "pnt.me",
    "poprl.com",
    "posted.at",
    "post.ly",
    "profile.to",
    "qicute.com",
    "qlnk.net",
    "quip-art.com",
    "rb6.me",
    "redirx.com",
    "rickroll.it",
    "ri.ms",
    "riz.gd",
    "rsmonkey.com",
    "rubyurl.com",
    "ru.ly",
    "s7y.us",
    "safe.mn",
    "sharein.com",
    "sharetabs.com",
    "shorl.com",
    "short.ie",
    "shortlinks.co.uk",
    "shortna.me",
    "short.to",
    "shorturl.com",
    "shoturl.us",
    "shrinkify.com",
    "shrinkster.com",
    "shrten.com",
    "shrt.st",
    "shrunkin.com",
    "shw.me",
    "simurl.com",
    "sn.im",
    "snipr.com",
    "snipurl.com",
    "snurl.com",
    "sp2.ro",
    "spedr.com",
    "sqrl.it",
    "starturl.com",
    "sturly.com",
    "su.pr",
    "t.co",
    "tcrn.ch",
    "thrdl.es",
    "tighturl.com",
    "tiny123.com",
    "tinyarro.ws",
    "tiny.cc",
    "tiny.pl",
    "tinytw.it",
    "tinyuri.ca",
    "tinyurl.com",
    "tinyvid.io",
    "tnij.org",
    "togoto.us",
    "to.ly",
    "traceurl.com",
    "tr.im",
    "tr.my",
    "turo.us",
    "tweetburner.com",
    "twirl.at",
    "twit.ac",
    "twitterpan.com",
    "twitthis.com",
    "twiturl.de",
    "twurl.cc",
    "twurl.nl",
    "u6e.de",
    "ub0.cc",
    "u.mavrev.com",
    "u.nu",
    "updating.me",
    "ur1.ca",
    "url4.eu",
    "urlao.com",
    "urlbrief.com",
    "url.co.uk",
    "urlcover.com",
    "urlcut.com",
    "urlenco.de",
    "urlhawk.com",
    "url.ie",
    "urlkiss.com",
    "urlot.com",
    "urlpire.com",
    "urlx.ie",
    "urlx.org",
    "urlzen.com",
    "virl.com",
    "vl.am",
    "w3t.org",
    "wapurl.co.uk",
    "wipi.es",
    "wp.me",
    "xaddr.com",
    "x.co",
    "xeeurl.com",
    "xr.com",
    "xrl.in",
    "xrl.us",
    "x.se",
    "xurl.jp",
    "xzb.cc",
    "yep.it",
    "yfrog.com",
    "yweb.com",
    "zi.ma",
    "zi.pe",
    "zipmyurl.com",
    "zz.gd",
    "ymlp.com",
    "forms.gle",
    "ht.ly",
    "lnkd.in",
    "1drv.ms",
]

class URL:

    def __init__(self, url):
        if type(url) == bytes:
            url = url.decode()

        self.url = url
        self.domain = self.get_domain()
        self.top_level = self.get_top_level()
        self.is_shortened = False

    def get_domain(self):
        """Get the domain from a URL.
        :param url: URL to parse
        :returns: Just the domain name extracted from the URL
        """
        # TODO: Properly handle exception.
        try:
            return get_tld(self.url, as_object=True, fix_protocol=True).parsed_url.netloc.lower().lstrip("www.")
        except:
            return None

    def get_top_level(self):
        """Get only the top level domain from a URL.
        :param url: URL to parse
        :returns: The top level domain extracted from the URL
        """
        # TODO: Properly handle exception.
        try:
            return get_tld(self.url, as_object=True, fix_protocol=True).fld.lower()
        except:
            return None

    def check_if_shortened(self):
        if self.domain.lower() in SHORTENER_DOMAINS:
            self.is_shortened = True

        return self.is_shortened

    def unshorten(self):
        res = requests.head(self.url)
        if str(res.status_code).startswith("30"):
            return res.headers["Location"]

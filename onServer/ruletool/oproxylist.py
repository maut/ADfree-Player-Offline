[{
	"name": "crossdomain_youku",
	"find": "http:\/\/static\.youku\.com\/.*?q?(player|loaders?)(_[^.]+)?\.swf",
	"monitor": "http:\/\/v\.youku\.com\/crossdomain\.xml",
	"extra": "crossdomain"
}, {
	"name": "crossdomain_tudou",
	"find": ".*PortalPlayer[^\.]*\.swf",
	"monitor": "http:\/\/v\.youku\.com\/crossdomain\.xml",
	"extra": "crossdomain"
}, {
	"name": "crossdomain_tudou_sp",
	"find": ".*olc[^\.]*\.swf",
	"monitor": "http:\/\/v\.youku\.com\/crossdomain\.xml",
	"extra": "crossdomain"
}, {
	"name": "crossdomain_sohu",
	"find": "http:\/\/(tv\.sohu\.com\/|61\.135\.176\.223.*).*\/(main|PlayerShell)\.swf",
	"monitor": "http:\/\/(photocdn|live\.tv)\.sohu\.com\/crossdomain\.xml",
	"extra": "crossdomain"
}, {
	"name": "crossdomain_iqiyi|pps-1",
	"find": "https?:\/\/www\.iqiyi\.com\/(player\/(\d+\/Player|[a-z0-9]*|cupid\/.*\/(pps[\w]+|clear))|common\/flashplayer\/\d+\/(Main|Share)?Player_.*)\.swf",
	"monitor": "http:\/\/data\.video\.qiyi\.com\/crossdomain\.xml",
	"extra": "crossdomain"
}, {
	"name": "crossdomain_iqiyi|pps-2",
	"find": "https?:\/\/www\.iqiyi\.com\/player\/cupid\/common\/icon\.swf",
	"monitor": "http:\/\/sf\.video\.qiyi\.com\/crossdomain\.xml",
	"extra": "crossdomain"
},{
	"name": "yk.pp.navi.youku.com:80",
	"find": "",
	"monitor": "",
	"extra": "proxy"
}
]
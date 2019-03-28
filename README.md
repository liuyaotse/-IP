# -IP
首先在Upload_IP.py中填写阿里云的秘钥（在第10行，自己去阿里云申请）、需要解析的RecordId（RecordId在第28行填写，在这个网址中通过调试API获取。https://api.aliyun.com/#/?product=Alidns&api=DescribeDomainRecords）
接下来在37行修改你的域名。其他写到log.conf的东西都可以自己修改。
最后，在linux中设置定时任务即可。https://github.com/liuyaotse/Strategy/blob/master/%E4%BD%BF%E7%94%A8crontab%E5%AE%9A%E6%97%B6%E8%BF%90%E8%A1%8Cpython%E8%84%9A%E6%9C%AC
IP.conf是IP修改记录。 
log.conf是日志。我只在我认为可能出错的地方写了存到log.conf的代码，如果你要增加存log.conf的地方，可以自己调用WriteContent()。

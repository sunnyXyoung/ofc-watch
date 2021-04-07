# OurFloatingCastle Report Watcher

---

分析每一輪的浮游城戰報
順便看看團長到底作弊了幾次

# Distribute
1. `git clone https://github.com/Xialai-Kulimi/ofc-watch.git`
2. `cd ofc-watch`
3. `npm i`
4. `npm run build`

此時`ofc-watch/dist`資料夾就是可以部署的前端了。

# Generate JSON
1. 請先在`ofc-watch/python`下建立`.env`。
```angular2html
$ vim python/.env

watch-token=token
web-root=/path/to/your/web/root/

```

2. `python python/ana_data.py [round]`
e.g. `python python/ana_data.py 4` or `python python/ana_data.py 5`  
   此程序會生成可以直接被前端接收的資料，並且存放在`web-root/`，如果在執行時報錯請嘗試建立`web-root/[round]/`，如：`web-root/4/`。
   
3. `python python/get_match.py [round]`
抓戰報，並且存放在`web-root/ofc/`底下，如果在執行時報錯請嘗試建立`web-root/ofc/`
   
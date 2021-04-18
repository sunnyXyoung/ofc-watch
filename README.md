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
```JSON
 match: {
        startTime: 234566809898,
        endTime: 234567809898,
        location: "94ru -3",
        initCastle: [1, 2500],
        finalCastle: [1, 2400],
        id: "B_02",
        loot: [
          {
            floor: 1,
            name: "火龍頭",
            quality: "垃圾般的",
            type: "水龍頭",
            atk: "8787",
            def: "7414",
            minePower: "400",
            owner: "Kulimi"
          }
        ],
        atk_player: [
          {
            name: "Kulimi",
            role: "鍛造師",
            role2: "將軍",
            faction: "j6",
            kill: 456,
            killed: 0,
            assist: 2345,
            castleDamage: 4567,
            damage: 23414,
            damaged: 12456,
          }
        ],
        def_player: [
          {
            name: "Kulimi456",
            role: "戰鬥員",
            role2: "將軍",
            faction: "j6",
            kill: 456,
            killed: 0,
            assist: 2345,
            damage: 23414,
            damaged: 12456,
          }
        ],
        report_list: [
          {
            atk_f : "艾基爾",
            def_f: "吳",
            atk_name: "Kulimi2",
            atk_id: 20,
            def_name: "Kulimi",
            def_id: 1,
            dead: ["Kulimi2"],
            remarks: "城牆耗損了200點血量",
            time: 1617653222268.1222,
            id: 2
          }
        ],
      
      
      }
```
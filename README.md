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

player: {
        name: "Kulimi",
        role: "鍛造師",
        role2: "時裝設計師",
        id: 1,
        factions: [
          {
            name: "艾基爾",
            time: "40%"
          },
          {
            name: "吳",
            time: "60%"
          }
        ],
        max_money: 666666,
        max_money_last_time: 1234567,
        now_money: 10,
        now_money_last_time: 10,
        fightExp: 0,
        forgeExp: 0,
        mineExp: 0,
        times: 0,
        kill: 0,
        killed: 0,
        damage: 0,
        damaged: 0,
        castleDamage: 0,
        xp: 0,
        loot: [
            2,
            [
              {
                faction: "大麻神教",
                floor: 1,
                name: "火龍頭",
                quality: "垃圾般的",
                type: "水龍頭",
                atk: "8787",
                def: "7414",
                minePower: "400",
                times: "2"
              }
            ]
        ],
        report_summary: [
          {
            atk_f : "艾基爾",
            def_f: "吳",
            atk_name: "Kulimi2",
            atk_id: 20,
            def_name: "Kulimi",
            def_id: 1,
            floor: 0,
            spe: "kill",
            time: 1617653222268.1222,
            id: 2,
            match_id: "afsdfasdf"
          }
        ]
      }
```
<div align='center'>

  # 查牌子
  
  
  ✨ 一个基于 [hoshinobot](https://github.com/Ice-Cirno/HoshinoBot) 的插件 ✨
  
</div>

> *代码写的比较乱，请见谅*
### ⭐功能

主要是可以根据uid查询对应id所拥有的B站粉丝牌，找了很多查成分的插件都不包括粉丝牌查询，就写了这个。
查询后会自动在json中标注上次查询时间与共查询的次数（可以防止有人在群里一直查某个人导致刷屏）

### 🎞用途

1. 查询某人的DD程度
2. 表明自己的单推程度
3. ~~查询成分~~

### 📕用法
首先需要先获取cookie并填写到paiziconfig的cookie中
[点击这里](https://api.live.bilibili.com/xlive/web-ucenter/user/MedalWall?target_id=2)
↑用浏览器前往这里按F12，切到Network栏，然后刷新。
刷新后下方会有一个名字叫做MedalWall的文件，点开然后在右边找到“cookie:xxxx=xxxxxxxxxxxxxxxxx”的字样，复制下来即可。

放在一个文件夹里放入moudles并在_bot_.py里启用即可。

指令：查牌子[uid]
注*：[]不用打出来

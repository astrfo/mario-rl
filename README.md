# mario-rl

gym-super-mario-brosを使ってマリオのゲームやってみた

## 使用方法

```bash
pip install -r requirements.txt
python main.py
```

## 自分で遊んでみる

gym-super-mario-brosには自分で操作して遊ぶことができるらしい．

```bash
gym_super_mario_bros -m human
gym_super_mario_bros -e SuperMarioBros-4-2-v1 -m human #ステージの指定
```

### ステージの指定について

```tmp
SuperMarioBros-<world>-<stage>-v<version>
```

where:

`<world>` is a number in {1, 2, 3, 4, 5, 6, 7, 8} indicating the world  
`<stage>` is a number in {1, 2, 3, 4} indicating the stage within a world  
`<version>` is a number in {0, 1, 2, 3} specifying the ROM mode to use  
0: standard ROM  
1: downsampled ROM  
2: pixel ROM  
3: rectangle ROM  
For example, to play 4-2 on the downsampled ROM, you would use the environment id SuperMarioBros-4-2-v1.

詳しくみたい方は[こちら](https://github.com/Kautenja/gym-super-mario-bros)にどうぞ．

### 操作方法

```tmp
A: 左
D: 右
S: しゃがむ
O: ジャンプ
P: ファイヤー （ファイアマリオ時のみ）
```

## ランダム行動バージョン

```bash
gym_super_mario_bros -m random
```

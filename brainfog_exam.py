# 脳内プログラム
import random

# ワーキングメモリのクラス
class WorkingMemory:
    def __init__(self):
        self.memory = []
        self.energy = 100
    
    def add(self, sentence):
        # エネルギーを消費
        self.energy -= 1
        
        is_success = random.random() < self.energy / 100
        
        if not is_success:
            raise Exception("ワーキングメモリの追加に失敗しました。再試行してください。")
        self.memory.append(sentence)



working_memory = WorkingMemory()


# テストの問題文
sentences = [
    "問題1:","袋の中に","赤玉3個","青玉2個","白玉1個が","入っている。", "この中から", "玉を1個ずつ","同じ玉を戻さずに","2回取り出すとき、","2回とも","赤玉が出る確率を","求めなさい。"
]

for sentence in sentences:
    print(sentence)
    while True:
        try:
            # ワーキングメモリに文の一部を追加する
            succeed = working_memory.add(sentence)
            # 成功したら次へ
            break
        except Exception as e:
            print("エラー:", e)
            # ワーキングメモリへの追加に失敗した場合は再試行
            continue

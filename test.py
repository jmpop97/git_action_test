print("파일wjwkd")
with open("저장.txt",mode="w",encoding='utf-8') as f:
    f.write("저장완료")
    print("저장완료")
with open('저장.txt',mode="r",encoding='utf-8') as f:
    print(f)

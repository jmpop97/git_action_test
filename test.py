print("파일wnd")
with open("저장.txt",mode="w") as f:
    f.write("저장완료")
with open('저장.txt',mode="r") as f:
    print(f)

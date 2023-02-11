# By Praveen
def compute(word : list) -> list[list]:
    if len(word) <= 1:
        return [word]
    
    smallAns : list[list] = compute(word[1:])
    ans : list[list] = []
    for perm in smallAns:
        curr : list = perm[:]
        for i in range(0, len(curr) + 1):
            curr.insert(i, word[0])
            ans.append(curr)
            curr : list = perm[:]
    return ans

def main() -> None:
    if __name__ == "__main__":
        print(["".join(x) for x in compute(list("ABC"))])

main()
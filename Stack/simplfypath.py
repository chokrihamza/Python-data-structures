# /../dossier1/image.png/./ /

def simplfypath(s):
    stack=[]
    cur=""
    for c in s+"/":
        if c=="/":
            if cur=="..":
                if stack:stack.pop()
            elif cur!="" and cur !=".":
                stack.append(cur)
            cur=""

        else:
            cur+=c

    return "/"+"/".join(stack)

# test function

path1="/../doc1/doc2/.././/dossier1"

print(simplfypath(path1))

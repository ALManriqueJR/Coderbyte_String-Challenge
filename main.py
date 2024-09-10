def StringChallenge(strParam,num):
	lstAlf = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	strParam = strParam.lower()
	lstParam = list(strParam)

	dicioSpecial = {}

	for i in lstParam:
		if i.isalpha():
			continue
		else:
			pos = lstParam.index(i)
			dicioSpecial[pos] = i

	resp = []


	for i in lstParam:
		for j in lstAlf:
			if i == j :
				indexJ = lstAlf.index(j)

				if (indexJ + num) < 26:
					indexJ += num;
				else:
					aux = (indexJ + num) % 25
					indexJ = (indexJ + num) - aux * 25

				resp.append(lstAlf[indexJ])

	for x,y in dicioSpecial.items():
		resp.insert(x,y)

	strParam = ''.join(resp)
	strParam = strParam.title()

	return strParam


print(StringChallenge("Caesar Cipher",2))
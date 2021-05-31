num_of_words, num_of_teaching = map(int, input().split())
num_of_teaching -= 5

bit = {}
for i in range(26):
	bit[chr(ord('a') + i)] = 1 << i

def word_to_bit(word):
	result = 0
	for char in word:
		result |= bit[char]
	return result
	
words, remain = [], set()
poss, imposs = 0, 0

for _ in range(num_of_words):
	word = set(input()[4:-4]) - set(['a', 'n', 't', 'i', 'c'])
	if len(word) == 0:
		poss += 1
	elif len(word) > num_of_teaching:
		imposs += 1
	else:
		remain |= word
		words.append(word_to_bit(word))
remain = list(remain)

def teach(lst, mask, k):
	if k < 0:
		return 0
	elif k == 0:
		result = poss
		for word in words:
			if word & mask == 0:
				result += 1
		return result
	else:
		result = 0
		for i in range(len(lst) - k + 1):
			result = max(result, teach(lst[i+1:], mask ^ bit[lst[i]], k - 1))
		return result

if num_of_teaching < len(remain):
	print(teach(remain, ((1 << 26) - 1), num_of_teaching))
else:
	print(num_of_words - imposs)

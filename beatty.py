"""
Test cases
==========

Inputs:
    (string) str_n = "5"
Output:
    (string) "19"

Inputs:
    (string) str_n = "77"
Output:
    (string) "4208"
"""
r2_minus_1 = long(4142135623730950488016887242096980785696718753769480731766797379907324784621070388503875343276415727)


def answer(str_n):
    res = recur(long(str_n))
    return str(res)




def recur(n):
	if n == 0:
		return 0
	nprime = (n * r2_minus_1)//(10**100)
	return (nprime + n) * (nprime + n + 1) / 2 - nprime * (nprime + 1) - recur(nprime) #post algebraic manipulation, operates in log(n) time
	


def main():
	print answer("100") #test case


if __name__ == '__main__':
	main()
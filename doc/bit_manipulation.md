## Bit Manipulation 

| Operator | Use Case | Explanation | Example | Status|
| --- | ----- | -------- | ---- | ----- |
|*AND*| `a & b`| if a == b == 1, then a & b = 1, otherwise = 0| `1 & 1 = 1`, `1 & 0 = 0`,`0 & 1 = 0`, `0 & 0 = 0 `| OK | 
|*OR*| <code>`a | b`</code>| if a == 1 or b == 1, then `a | b = 1`, otherwise = 0| `1 | 1 = 1`, `1 | 0 = 1`,`0 & 1 = 1`, `0 & 0 = 0 `| OK | 
|*XOR*| `a ^ b`| if a == 1 or b == 1, then a ^ b = 0, otherwise = 0| `1 ^ 1 = 0`, `1 ^ 0 = 1`,`0 ^ 1 = 1`, `0 ^ 0 = 0`| OK | 
|*NOT*| `- a`| inverse || AGAIN | 
|*LEFT MOVE*| `a << b`| `left shift` a ( in binary) b times |`9 << 2 = 36`| OK |
|*RIGHT MOVE*| `a >> b`| `right shift` a ( in binary) b times |`9 >> 2 = 2`, `-9 >> 2 = -3`| AGAIN | 
|*RIGHT MOVE AND ADD 0*| `a >>> b`| `right shift` a ( in binary) b times, remove out-of-boundry bit, and add 0 left |`19 >>> 2 = 4`| AGAIN | 


## Ref 
- https://developer.mozilla.org/zh-TW/docs/Web/JavaScript/Obsolete_Pages/Obsolete_Pages/Obsolete_Pages/%E9%81%8B%E7%AE%97%E5%AD%90/%E4%BD%8D%E5%85%83%E9%81%8B%E7%AE%97%E5%AD%90
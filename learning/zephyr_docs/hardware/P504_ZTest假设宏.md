---
id: learning.zephyr-docs.hardware.ztestmac-1
title: ZTest假设宏
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assume.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第504章\_ZTest假设宏

原文：[group__ztest__assume](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assume.html)。读取日期：2026-10-13，`latest`。

本模块为 **Zephyr 测试框架（Zephyr Testing Framework，ZTest）**提供**假设（Assumption）**宏。假设不成立时，测试会标记为“跳过”（Skipped）。接口公开头文件为 `zephyr/ztest_assert.h`，仓库内位置为 `subsys/testsuite/ztest/include/zephyr/ztest_assert.h`。

> 译注：官方页面显示的构建机器绝对头文件路径在这里改为公开包含名。文中“直接比较、不转换”表示宏不额外强制转换操作数，C 语言自身的类型转换规则仍适用。

## 504.1\_共同的消息参数与展开规则

以下检查宏的 `...` 提供假设失败时打印的可选消息及格式化变量。展开调用基础宏 [`zassume`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assert.html#ga5a4319eec770be532f34acb86e022c48)；其中 `__VA_ARGS__` 表示可变参数，`#` 将参数变成字符串，`##` 用于预处理拼接，`NULL` 是空指针值。内部宏 `Z_ZTEST_IS_NULL` 检查指针是否为空，[`memcmp`](https://docs.zephyrproject.org/latest/doxygen/html/string_8h.html#ad8bfbfa1e4ad284ded921dd775735521) 按字节比较内存，[`strcmp`](https://docs.zephyrproject.org/latest/doxygen/html/string_8h.html#a11bd144d7d44914099a3aeddf1c8567d) 比较字符串内容。

内存比较入口 `zassume_mem_equal(...)` 是一个包装宏，它的 `...` 代表转交给内部宏的全部实参，具体形式见内存比较一节。

## 504.2\_闭区间和相等比较

[`zassume_between_inclusive`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assume.html#gacff02eeba8dd334b3727dbe2036617e3) 假设值 `a` 大于等于下限，且小于等于上限，包含两个边界。假设不成立时，测试会标记为“跳过”（Skipped）。

```c
#define zassume_between_inclusive(a, l, u, ...)
```

参数 `a` 为待比较值，`l`、`u` 分别为下限、上限。`...` 为假设失败时的可选消息及变量。

```c
zassume(((a) >= (l)) && ((a) <= (u)), #a " not between " #l " and " #u " inclusive",       \
        ##__VA_ARGS__)
```

[`zassume_equal`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assume.html#ga88c2a3153568a6f621b88dd6ceeb48d6) 假设`a` 等于 `b`。二者不经宏额外转换而直接比较。假设不成立时，测试会标记为“跳过”（Skipped）。

```c
#define zassume_equal(a, b, ...)
```

参数 `a`、`b` 是待比较的两个值。`...` 为假设失败时的可选消息及变量。

```c
zassume((a) == (b), #a " not equal to " #b, ##__VA_ARGS__)
```

[`zassume_equal_ptr`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assume.html#ga78d6fbbf5eb13b32a5164053811b6cca) 假设`a` 等于 `b`，比较前将二者转换为 `void *` 指针。假设不成立时，测试会标记为“跳过”（Skipped）。

```c
#define zassume_equal_ptr(a, b, ...)
```

参数 `a`、`b` 为待比较值。`...` 为假设失败时的可选消息及变量。

```c
zassume((void *)(a) == (void *)(b), #a " not equal to " #b, ##__VA_ARGS__)
```

## 504.3\_假条件与空指针

[`zassume_false`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assume.html#ga5acf4256e5af3afaed06da7400dc3ad5) 假设条件 `cond` 为假。假设不成立时，测试会标记为“跳过”（Skipped）。

```c
#define zassume_false(cond, ...)
```

参数 `cond` 为被检查条件。`...` 为假设失败时的可选消息及变量。

```c
zassume(!(cond), #cond " is true", ##__VA_ARGS__)
```

[`zassume_is_null`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assume.html#ga3c5b1814deb5974e8ba0af961b516fa0) 假设指针 `ptr` 为 `NULL`。假设不成立时，测试会标记为“跳过”（Skipped）。

```c
#define zassume_is_null(ptr, ...)
```

参数 `ptr` 为待比较指针。`...` 为假设失败时的可选消息及变量。

```c
zassume(Z_ZTEST_IS_NULL(ptr), #ptr " is not NULL", ##__VA_ARGS__)
```

## 504.4\_内存内容比较

[`zassume_mem_equal`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assume.html#ga62be45256399530167745e71226e4a37) 假设两个内存缓冲区具有相同内容。

```c
#define zassume_mem_equal(...)
```

这里 `...` 是传递给 [`zassume_mem_equal__`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assume.html#gaaed6045f194ead4ffe1dd72a6fa5175d) 的全部参数，详见后面的内部宏。

该宏调用最终执行内存比较的假设宏。**两次展开（Double Expansion）**允许某些参数由会展开成多个值的宏提供；原文以 ANSI-C99 的宏调用前参数展开规则说明这一设计。

```c
zassume_mem_equal__(__VA_ARGS__)
```

[`zassume_mem_equal__`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assume.html#gaaed6045f194ead4ffe1dd72a6fa5175d) 假设两个内存缓冲区具有相同内容。假设不成立时，测试会标记为“跳过”（Skipped）。

```c
#define zassume_mem_equal__(buf, exp, size, ...)
```

参数 `buf` 为待比较缓冲区，`exp` 为保存预期内容的缓冲区，`size` 为缓冲区大小。`...` 为假设失败时的可选消息及变量。

**注意：**这是用于第二次展开的内部宏（Internal Macro），正常入口见 [`zassume_mem_equal`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assume.html#ga62be45256399530167745e71226e4a37)。

```c
zassume(memcmp(buf, exp, size) == 0, #buf " not equal to " #exp, ##__VA_ARGS__)
```

## 504.5\_不相等、非空与状态检查

[`zassume_not_equal`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assume.html#ga0d90bb874c3135ffee870a4b61607853) 假设`a` 不等于 `b`。二者不经宏额外转换而直接比较。假设不成立时，测试会标记为“跳过”（Skipped）。

```c
#define zassume_not_equal(a, b, ...)
```

参数 `a`、`b` 为待比较值。`...` 为假设失败时的可选消息及变量。

```c
zassume((a) != (b), #a " equal to " #b, ##__VA_ARGS__)
```

[`zassume_not_null`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assume.html#ga24f4144edf5cef493c88872c7d56900e) 假设指针 `ptr` 不是 `NULL`。假设不成立时，测试会标记为“跳过”（Skipped）。

```c
#define zassume_not_null(ptr, ...)
```

参数 `ptr` 为待比较指针。`...` 为假设失败时的可选消息及变量。

```c
zassume(!Z_ZTEST_IS_NULL(ptr), #ptr " is NULL", ##__VA_ARGS__)
```

[`zassume_not_ok`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assume.html#ga539831d2f42cc991a8295b388ec12846) 假设`cond` 不为 `0`，即原文所称的失败状态。假设不成立时，测试会标记为“跳过”（Skipped）。

```c
#define zassume_not_ok(cond, ...)
```

参数 `cond` 为被检查条件。`...` 为假设失败时的可选消息及变量。

```c
zassume((cond) != 0, #cond " is zero", ##__VA_ARGS__)
```

[`zassume_ok`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assume.html#ga9c6d1c701dd2d50027bf5e24b7567ae4) 假设`cond` 为 `0`，即成功状态。假设不成立时，测试会标记为“跳过”（Skipped）。

```c
#define zassume_ok(cond, ...)
```

参数 `cond` 为被检查条件。`...` 为假设失败时的可选消息及变量。

```c
zassume((cond) == 0, #cond " is non-zero", ##__VA_ARGS__)
```

> 译注：`ok` 系列检查约定“零表示成功”，不要与检查布尔真值的 `true` 宏混淆。

## 504.6\_字符串与真条件

[`zassume_str_equal`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assume.html#ga33a9cd37d321f1a421a1328e67b04788) 假设两个字符串具有相同内容。假设不成立时，测试会标记为“跳过”（Skipped）。

```c
#define zassume_str_equal(s1, s2, ...)
```

参数 `s1` 为第一个字符串，`s2` 为第二个字符串。`...` 为假设失败时的可选消息及变量。

```c
zassume(strcmp(s1, s2) == 0, #s1 " not equal to " #s2, ##__VA_ARGS__)
```

> 译注：本宏的原文参数说明写作 expectation fails，译为假设检查失败；其展开仍调用 [`zassume`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assert.html#ga5a4319eec770be532f34acb86e022c48)。

[`zassume_true`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assume.html#ga6f5778ed8c1205126f7dcafb6eb26905) 假设条件 `cond` 为真。假设不成立时，测试会标记为“跳过”（Skipped）。

```c
#define zassume_true(cond, ...)
```

参数 `cond` 为被检查条件。`...` 为假设失败时的可选消息及变量。

```c
zassume(cond, #cond " is false", ##__VA_ARGS__)
```

## 504.7\_允许偏差

[`zassume_within`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assume.html#gad808c91e07e6c27b2e28ec7e04e03854) 假设`a` 位于 `b` 的允许偏差内；展开包含两侧边界。假设不成立时，测试会标记为“跳过”（Skipped）。

```c
#define zassume_within(a, b, d, ...)
```

参数 `a`、`b` 为待比较值，`d` 为偏差（Delta），检查区间为 `b - d` 至 `b + d`。`...` 为假设失败时的可选消息及变量。

```c
zassume(((a) >= ((b) - (d))) && ((a) <= ((b) + (d))), #a " not within " #b " +/- " #d,     \
        ##__VA_ARGS__)
```


---

[上一章：ZTest断言宏](P503_ZTest断言宏.md) · [下一章：ZTest预期检查宏](P505_ZTest预期检查宏.md) · [返回大纲](大纲.md)

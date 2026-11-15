---
id: learning.zephyr-docs.hardware.ztestmac-0
title: ZTest断言宏
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assert.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第503章\_ZTest断言宏

原文：[group__ztest__assert](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assert.html)。读取日期：2026-10-13，`latest`。

本模块为 **Zephyr 测试框架（Zephyr Testing Framework，ZTest）**提供**断言（Assertion）**宏。断言表达测试要求成立的条件；本页保留每个宏的参数、比较方式及官方展开。公开头文件为 `zephyr/ztest_assert.h`，仓库位置为 `subsys/testsuite/ztest/include/zephyr/ztest_assert.h`。

> 译注：原页包含指令显示官方构建机的绝对路径，这里改用公开头文件名。下文的“直接比较、不转换”沿用原文含义：宏不额外强制转换操作数，C 语言自身的通常算术转换规则仍适用。

## 503.1\_基础检查与可选消息

基础宏 `zassert(cond, default_msg, ...)` 把条件、默认消息和可选消息交给内部 `_zassert_va` 处理。`cond` 是被检查条件，`default_msg` 是默认消息；本页除内存比较包装宏外，各检查宏的 `...` 都是检查失败时要打印的**可选消息及格式化变量**。

```c
#define zassert(cond, default_msg, ...)
```

展开中 `__VA_ARGS__` 表示可变参数，`__VA_OPT__` 根据是否存在可变参数决定是否展开，[`COND_CODE_1`](../util_reference/P001_通用工具公共接口.md#ga358bc3e7669c860a98839a51cd526b20) 根据条件选择分支；`NULL` 是空指针值。后续展开中的 `#` 用于把参数转成字符串，`##` 用于预处理拼接，`Z_ZTEST_IS_NULL` 是内部空指针检查宏；[`memcmp`](https://docs.zephyrproject.org/latest/doxygen/html/string_8h.html#ad8bfbfa1e4ad284ded921dd775735521) 按字节比较内存，[`strcmp`](https://docs.zephyrproject.org/latest/doxygen/html/string_8h.html#a11bd144d7d44914099a3aeddf1c8567d) 比较字符串内容。

```c
_zassert_va(cond, default_msg, COND_CODE_1(__VA_OPT__(1), (__VA_ARGS__), (NULL)))
```

## 503.2\_闭区间、数值和指针相等

[`zassert_between_inclusive`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assert.html#ga2b6b41de3e4856b21458febab3261b91) 断言 `a` 大于等于下限 `l`，且小于等于上限 `u`，上下边界都包含在内。参数 `a` 是待比较值，`l`、`u` 分别为下限、上限，`...` 为失败消息及变量。

```c
#define zassert_between_inclusive(a, l, u, ...)
```

```c
zassert(((a) >= (l)) && ((a) <= (u)), #a " not between " #l " and " #u " inclusive",       \
        ##__VA_ARGS__)
```

[`zassert_equal`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assert.html#gacd075c7ee4dc2d64701bd3098a31b673) 断言 `a` 等于 `b`，二者不经宏额外转换而直接比较。`a`、`b` 为待比较的两个值，`...` 为失败消息及变量。

```c
#define zassert_equal(a, b, ...)
```

```c
zassert((a) == (b), #a " not equal to " #b, ##__VA_ARGS__)
```

[`zassert_equal_ptr`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assert.html#gabf20273fcba9cc45939a9f7db77f0bfc) 同样断言 `a` 等于 `b`，但比较前会将两个值转换为 `void *` 指针。`a`、`b` 为待比较值，`...` 为失败消息及变量。

```c
#define zassert_equal_ptr(a, b, ...)
```

```c
zassert((void *)(a) == (void *)(b), #a " not equal to " #b, ##__VA_ARGS__)
```

## 503.3\_假条件和空指针

[`zassert_false`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assert.html#ga7330d1794fb961e07ee40294019dead0) 断言条件 `cond` 为假；`...` 为失败消息及变量。

```c
#define zassert_false(cond, ...)
```

```c
zassert(!(cond), #cond " is true", ##__VA_ARGS__)
```

[`zassert_is_null`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assert.html#gac0839891fd8bb7313b98551465e04c19) 断言指针 `ptr` 为 `NULL`；`ptr` 为待比较指针，`...` 为失败消息及变量。

```c
#define zassert_is_null(ptr, ...)
```

```c
zassert(Z_ZTEST_IS_NULL(ptr), #ptr " is not NULL", ##__VA_ARGS__)
```

## 503.4\_内存缓冲区内容比较

[`zassert_mem_equal`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assert.html#gabbfcf6345172387326d35b5d0e2bb051) 断言两个内存缓冲区内容相同。它调用最终执行内存断言的宏，通过**两次展开（Double Expansion）**允许某些参数由会展开为多个值的宏提供。原文以 ANSI-C99 的宏调用前参数展开规则说明这一设计。

```c
#define zassert_mem_equal(...)
```

这里 `...` 表示转交给 [`zassert_mem_equal__`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assert.html#ga30e5fefa185944d3e949d4023c2eea27) 的全部实参，具体参数见下文。

```c
zassert_mem_equal__(__VA_ARGS__)
```

[`zassert_mem_equal__`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assert.html#ga30e5fefa185944d3e949d4023c2eea27) 是作为第二次展开使用的**内部宏（Internal Macro）**，断言两个缓冲区内容相同。正常入口见 [`zassert_mem_equal`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assert.html#gabbfcf6345172387326d35b5d0e2bb051)。

```c
#define zassert_mem_equal__(buf, exp, size, ...)
```

参数 `buf` 为待比较缓冲区，`exp` 为保存预期内容的缓冲区，`size` 为缓冲区大小，`...` 为失败消息及变量。展开使用 [`memcmp`](https://docs.zephyrproject.org/latest/doxygen/html/string_8h.html#ad8bfbfa1e4ad284ded921dd775735521) 比较指定大小的内存。

```c
zassert(memcmp(buf, exp, size) == 0, #buf " not equal to " #exp, ##__VA_ARGS__)
```

## 503.5\_不相等、非空与返回状态

[`zassert_not_equal`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assert.html#ga43f306bf33d5e837b8927df16b82a363) 断言 `a` 不等于 `b`。两值不经宏额外转换而直接比较；`a`、`b` 为待比较值，`...` 为失败消息及变量。

```c
#define zassert_not_equal(a, b, ...)
```

```c
zassert((a) != (b), #a " equal to " #b, ##__VA_ARGS__)
```

[`zassert_not_null`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assert.html#ga849adad4afe893a7ae3dc2fbe750dc00) 断言指针 `ptr` 不是 `NULL`；`...` 为失败消息及变量。

```c
#define zassert_not_null(ptr, ...)
```

```c
zassert(!Z_ZTEST_IS_NULL(ptr), #ptr " is NULL", ##__VA_ARGS__)
```

[`zassert_not_ok`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assert.html#gafe0e2609f77906ab0caddc31448a4fc8) 断言 `cond` 不为 `0`，即原文所称的失败状态。`cond` 是被检查条件，`...` 为失败消息及变量。

```c
#define zassert_not_ok(cond, ...)
```

```c
zassert((cond) != 0, #cond " is zero", ##__VA_ARGS__)
```

[`zassert_ok`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assert.html#gade40e2ec78ec813739e7725524fae7f0) 断言 `cond` 为 `0`，即成功状态。`cond` 是被检查条件，`...` 为失败消息及变量。

```c
#define zassert_ok(cond, ...)
```

```c
zassert((cond) == 0, #cond " is non-zero", ##__VA_ARGS__)
```

> 译注：`ok` 系列检查约定“零表示成功”，与判断布尔真值的 [`zassert_true`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assert.html#gaeebddde19012223e3d5e853a1dac3ac5) 方向不同。

## 503.6\_字符串、真条件与不可达位置

[`zassert_str_equal`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assert.html#ga382017945a8c409e885cad8d0909b197) 断言两个字符串内容相同。`s1` 为第一个字符串，`s2` 为第二个字符串，`...` 为失败时打印的可选消息及变量。

```c
#define zassert_str_equal(s1, s2, ...)
```

```c
zassert(strcmp(s1, s2) == 0, #s1 " not equal to " #s2, ##__VA_ARGS__)
```

> 译注：此宏的可选消息说明在原页写作 expectation fails，按当前断言接口译为检查失败，展开仍原样保留。

`zassert_true` 断言条件 `cond` 为真，`...` 为失败消息及变量。

```c
#define zassert_true(cond, ...)
```

```c
zassert(cond, #cond " is false", ##__VA_ARGS__)
```

[`zassert_unreachable`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assert.html#ga300684a6b56e73e2cad6fd7458541129) 断言执行流程不应到达此调用位置；`...` 为到达此处导致断言失败时的可选消息及变量。

```c
#define zassert_unreachable(...)
```

```c
zassert(0, "Reached unreachable code", ##__VA_ARGS__)
```

## 503.7\_允许偏差及另外两种基础检查

[`zassert_within`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assert.html#gacc930af1a66e8533c5eca9526e198b4b) 断言 `a` 在 `b` 的允许偏差 `d` 范围内；展开检查闭区间 `b - d` 至 `b + d`。`a`、`b` 是待比较值，`d` 是偏差（Delta），`...` 为失败消息及变量。

```c
#define zassert_within(a, b, d, ...)
```

```c
zassert(((a) >= ((b) - (d))) && ((a) <= ((b) + (d))), #a " not within " #b " +/- " #d,     \
        ##__VA_ARGS__)
```

原页同时列出**假设（Assumption）**基础宏 [`zassume`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assert.html#ga5a4319eec770be532f34acb86e022c48) 和**预期检查（Expectation）**基础宏 [`zexpect`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assert.html#ga7bd837a8164123e3a06795b9f87a308d)，只提供声明与展开，没有在本页给出独立参数说明。它们分别转交内部 `_zassume_va` 和 `_zexpect_va` 处理函数；专用检查宏见后续对应接口页。

```c
#define zassume(cond, default_msg, ...)
```

```c
_zassume_va(cond, default_msg, COND_CODE_1(__VA_OPT__(1), (__VA_ARGS__), (NULL)))
```

```c
#define zexpect(cond, default_msg, ...)
```

```c
_zexpect_va(cond, default_msg, COND_CODE_1(__VA_OPT__(1), (__VA_ARGS__), (NULL)))
```

---

[上一章：ZTest测试框架接口](P502_ZTest测试框架接口.md) · [下一章：ZTest假设宏](P504_ZTest假设宏.md) · [返回大纲](大纲.md)

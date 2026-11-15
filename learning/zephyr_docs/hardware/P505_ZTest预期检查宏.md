---
id: learning.zephyr-docs.hardware.ztestmac-2
title: ZTest预期检查宏
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__expect.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第505章\_ZTest预期检查宏

原文：[group__ztest__expect](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__expect.html)。读取日期：2026-10-13，`latest`。

本模块为 **Zephyr 测试框架（Zephyr Testing Framework，ZTest）**提供**预期检查（Expectation）**宏。预期不成立时，将测试标记为“失败”（Failed），但继续执行测试。接口公开头文件为 `zephyr/ztest_assert.h`，仓库内位置为 `subsys/testsuite/ztest/include/zephyr/ztest_assert.h`。

> 译注：官方页面显示的构建机器绝对头文件路径在这里改为公开包含名。文中“直接比较、不转换”表示宏不额外强制转换操作数，C 语言自身的类型转换规则仍适用。

## 505.1\_共同的消息参数与展开规则

以下检查宏的 `...` 提供预期失败时打印的可选消息及格式化变量。展开调用基础宏 [`zexpect`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assert.html#ga7bd837a8164123e3a06795b9f87a308d)；其中 `__VA_ARGS__` 表示可变参数，`#` 将参数变成字符串，`##` 用于预处理拼接，`NULL` 是空指针值。内部宏 `Z_ZTEST_IS_NULL` 检查指针是否为空，[`memcmp`](https://docs.zephyrproject.org/latest/doxygen/html/string_8h.html#ad8bfbfa1e4ad284ded921dd775735521) 按字节比较内存，[`strcmp`](https://docs.zephyrproject.org/latest/doxygen/html/string_8h.html#a11bd144d7d44914099a3aeddf1c8567d) 比较字符串内容。

## 505.2\_闭区间和相等比较

[`zexpect_between_inclusive`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__expect.html#gac37ebea6a9c71e3666a4911ceea5c913) 预期值 `a` 大于等于下限，且小于等于上限，包含两个边界。预期不成立时，将测试标记为“失败”（Failed），但继续执行测试。

```c
#define zexpect_between_inclusive(a, lower, upper, ...)
```

参数 `a` 为待比较值，`lower`、`upper` 分别为下限、上限。`...` 为预期失败时的可选消息及变量。

```c
zexpect(((a) >= (lower)) && ((a) <= (upper)),                                              \
        #a " not between " #lower " and " #upper " inclusive", ##__VA_ARGS__)
```

[`zexpect_equal`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__expect.html#ga5ba65dbf95c204ed60694c5757db247f) 预期`a` 等于 `b`。预期不成立时，将测试标记为“失败”（Failed），但继续执行测试。

```c
#define zexpect_equal(a, b, ...)
```

参数 `a`、`b` 是待比较的两个值。`...` 为预期失败时的可选消息及变量。

```c
zexpect((a) == (b), #a " not equal to " #b, ##__VA_ARGS__)
```

[`zexpect_equal_ptr`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__expect.html#gabf791d13c5781fc2215289d6dd925b3e) 预期`a` 等于 `b`，比较前将二者转换为 `void *` 指针。预期不成立时，将测试标记为“失败”（Failed），但继续执行测试。

```c
#define zexpect_equal_ptr(a, b, ...)
```

参数 `a`、`b` 为待比较值。`...` 为预期失败时的可选消息及变量。

```c
zexpect((void *)(a) == (void *)(b), #a " not equal to " #b, ##__VA_ARGS__)
```

## 505.3\_假条件与空指针

[`zexpect_false`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__expect.html#ga619bd320e39799414383a228dc2d8299) 预期条件 `cond` 为假。预期不成立时，将测试标记为“失败”（Failed），但继续执行测试。

```c
#define zexpect_false(cond, ...)
```

参数 `cond` 为被检查条件。`...` 为预期失败时的可选消息及变量。

```c
zexpect(!(cond), #cond " is true", ##__VA_ARGS__)
```

[`zexpect_is_null`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__expect.html#ga10b2c904f1c68b816eae2ad53e2b9f90) 预期指针 `ptr` 为 `NULL`。预期不成立时，将测试标记为“失败”（Failed），但继续执行测试。

```c
#define zexpect_is_null(ptr, ...)
```

参数 `ptr` 为待比较指针。`...` 为预期失败时的可选消息及变量。

```c
zexpect(Z_ZTEST_IS_NULL(ptr), #ptr " is not NULL", ##__VA_ARGS__)
```

## 505.4\_内存内容比较

[`zexpect_mem_equal`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__expect.html#gaee52264e5f92a606a2a85f5fbb0a85fb) 预期两个内存缓冲区具有相同内容。预期不成立时，将测试标记为“失败”（Failed），但继续执行测试。

```c
#define zexpect_mem_equal(buf, exp, size, ...)
```

参数 `buf` 是待比较缓冲区，`exp` 保存预期内容，`size` 为缓冲区大小。`...` 为预期失败时的可选消息及变量。

```c
zexpect(memcmp(buf, exp, size) == 0, #buf " not equal to " #exp, ##__VA_ARGS__)
```

## 505.5\_不相等、非空与状态检查

[`zexpect_not_equal`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__expect.html#ga31d83ab89828a03aebe0d0dc003f5232) 预期`a` 不等于 `b`。二者不经宏额外转换而直接比较。预期不成立时，将测试标记为“失败”（Failed），但继续执行测试。

```c
#define zexpect_not_equal(a, b, ...)
```

参数 `a`、`b` 为待比较值。`...` 为预期失败时的可选消息及变量。

```c
zexpect((a) != (b), #a " equal to " #b, ##__VA_ARGS__)
```

[`zexpect_not_null`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__expect.html#gaa51053fe2a07c6417db7952d7a594798) 预期指针 `ptr` 不是 `NULL`。预期不成立时，将测试标记为“失败”（Failed），但继续执行测试。

```c
#define zexpect_not_null(ptr, ...)
```

参数 `ptr` 为待比较指针。`...` 为预期失败时的可选消息及变量。

```c
zexpect(!Z_ZTEST_IS_NULL(ptr), #ptr " is NULL", ##__VA_ARGS__)
```

[`zexpect_not_ok`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__expect.html#gabde5406775f05d5fcd135eb926969004) 预期`cond` 不为 `0`，即原文所称的失败状态。预期不成立时，将测试标记为“失败”（Failed），但继续执行测试。

```c
#define zexpect_not_ok(cond, ...)
```

参数 `cond` 为被检查条件。`...` 为预期失败时的可选消息及变量。

```c
zexpect((cond) != 0, #cond " is zero", ##__VA_ARGS__)
```

[`zexpect_ok`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__expect.html#gaab325ee22058252c6a1c3243f3226657) 预期`cond` 为 `0`，即成功状态。预期不成立时，将测试标记为“失败”（Failed），但继续执行测试。

```c
#define zexpect_ok(cond, ...)
```

参数 `cond` 为被检查条件。`...` 为预期失败时的可选消息及变量。

```c
zexpect((cond) == 0, #cond " is non-zero", ##__VA_ARGS__)
```

> 译注：`ok` 系列检查约定“零表示成功”，不要与检查布尔真值的 `true` 宏混淆。

## 505.6\_字符串与真条件

[`zexpect_str_equal`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__expect.html#gacd5ef284610ca2027fc2e892243dfd38) 预期两个字符串具有相同内容。预期不成立时，将测试标记为“失败”（Failed），但继续执行测试。

```c
#define zexpect_str_equal(s1, s2, ...)
```

参数 `s1` 为第一个字符串，`s2` 为第二个字符串。`...` 为预期失败时的可选消息及变量。

```c
zexpect(strcmp(s1, s2) == 0, #s1 " not equal to " #s2, ##__VA_ARGS__)
```

[`zexpect_true`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__expect.html#gaef66b2764b6086dfbe8cbc933a8cfdc3) 预期条件 `cond` 为真。预期不成立时，将测试标记为“失败”（Failed），但继续执行测试。

```c
#define zexpect_true(cond, ...)
```

参数 `cond` 为被检查条件。`...` 为预期失败时的可选消息及变量。

```c
zexpect(cond, #cond " is false", ##__VA_ARGS__)
```

## 505.7\_允许偏差

[`zexpect_within`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__expect.html#ga907afb07269bbc444a3d8ffee46839b5) 预期`a` 位于 `b` 的允许偏差内；展开包含两侧边界。预期不成立时，将测试标记为“失败”（Failed），但继续执行测试。

```c
#define zexpect_within(a, b, delta, ...)
```

参数 `a`、`b` 为待比较值，`delta` 表示二者允许的差值（Delta），检查区间为 `b - delta` 至 `b + delta`。`...` 为预期失败时的可选消息及变量。

```c
zexpect(((a) >= ((b) - (delta))) && ((a) <= ((b) + (delta))),                              \
        #a " not within " #b " +/- " #delta, ##__VA_ARGS__)
```


---

[上一章：ZTest假设宏](P504_ZTest假设宏.md) · [下一章：ZTest模拟支持](P506_ZTest模拟支持.md) · [返回大纲](大纲.md)

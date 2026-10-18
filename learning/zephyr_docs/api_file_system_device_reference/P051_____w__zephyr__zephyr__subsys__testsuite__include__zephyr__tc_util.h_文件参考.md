---
id: learning.zephyr-docs.api-file-system-device-reference.page-51
title: ____w__zephyr__zephyr__subsys__testsuite__include__zephyr__tc_util.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/tc__util_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第51章\_\_\_\_\_w\_\_zephyr\_\_zephyr\_\_subsys\_\_testsuite\_\_include\_\_zephyr\_\_tc\_util.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/tc__util_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/kernel.h>
#include <string.h>
#include <zephyr/sys/printk.h>
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 51.1\_宏定义（Macros）

<a id="r_aec98e66470b575771ed484118095b692"></a>

```c
#define PRINT_DATA(fmt, ...)
```

相关声明：[PRINT_DATA](#aec98e66470b575771ed484118095b692)。

<a id="r_a91250f31fc327df207018b9c66493677"></a>

```c
#define TC_STR_HELPER(x)
```

相关声明：[TC_STR_HELPER](#a91250f31fc327df207018b9c66493677)。

<a id="r_acd142b5f39b0d6fe5216440432ef2c72"></a>

```c
#define TC_STR(x)
```

相关声明：[TC_STR](#acd142b5f39b0d6fe5216440432ef2c72)。

<a id="r_a82cdb6d03f070075b576cbe1dab5e71a"></a>

```c
#define TC_PRINT_RUNID do {} while (false)
```

相关声明：[TC_PRINT_RUNID](#a82cdb6d03f070075b576cbe1dab5e71a)、[false](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a65e9886d74aaee76545e83dd09011727)。

报告运行标识符（Run ID）。

<a id="r_a96f7bbefdafd3b13e9ee460477b13097"></a>

```c
#define TC_PRINT_RUNID_START do {} while (false)
```

相关声明：[TC_PRINT_RUNID_START](#a96f7bbefdafd3b13e9ee460477b13097)、[false](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a65e9886d74aaee76545e83dd09011727)。

在测试映像开始执行时报告运行标识符（Run ID）。

<a id="r_af72c5654279b3d1e227e8dec30411944"></a>

```c
#define PRINT_LINE
```

相关声明：[PRINT_LINE](#af72c5654279b3d1e227e8dec30411944)。

<a id="r_a5486258f1f34d3baeda92a74b63c27c3"></a>

```c
#define TASK_STACK_SIZE (1024 * 2)
```

相关声明：[TASK_STACK_SIZE](#a5486258f1f34d3baeda92a74b63c27c3)。

<a id="r_a8e446c4d4b1517a80c371ca370c56ac3"></a>

```c
#define FMT_ERROR "%s - %s@%d. "
```

相关声明：[FMT_ERROR](#a8e446c4d4b1517a80c371ca370c56ac3)。

<a id="r_afb66a88e5d1e781aeb5aa9739a8fe868"></a>

```c
#define TC_PASS 0
```

相关声明：[TC_PASS](#afb66a88e5d1e781aeb5aa9739a8fe868)。

<a id="r_a196c300c18de32c79d757131b579a3a5"></a>

```c
#define TC_FAIL 1
```

相关声明：[TC_FAIL](#a196c300c18de32c79d757131b579a3a5)。

<a id="r_abafb6d8cf1e1a3bb2247d5384d1d5461"></a>

```c
#define TC_SKIP 2
```

相关声明：[TC_SKIP](#abafb6d8cf1e1a3bb2247d5384d1d5461)。

<a id="r_ac0108c70de44b3186c7ead1c1430b3d1"></a>

```c
#define TC_FLAKY 3
```

相关声明：[TC_FLAKY](#ac0108c70de44b3186c7ead1c1430b3d1)。

<a id="r_a991995992ef5c23b7c6cf7138b394437"></a>

```c
#define TC_PASS_STR "PASS"
```

相关声明：[TC_PASS_STR](#a991995992ef5c23b7c6cf7138b394437)。

<a id="r_ac5103b154fa450c478c2bf3f520cb8ff"></a>

```c
#define TC_FAIL_STR "FAIL"
```

相关声明：[TC_FAIL_STR](#ac5103b154fa450c478c2bf3f520cb8ff)。

<a id="r_a586f060684ebfc5db4105a30370a41d0"></a>

```c
#define TC_SKIP_STR "SKIP"
```

相关声明：[TC_SKIP_STR](#a586f060684ebfc5db4105a30370a41d0)。

<a id="r_a584cf09eac3d2fa3758924cb843cdbf5"></a>

```c
#define TC_FLAKY_STR "FLAKY"
```

相关声明：[TC_FLAKY_STR](#a584cf09eac3d2fa3758924cb843cdbf5)。

<a id="r_a6fcd0e6c5448a9198cdaed1e88e86e1b"></a>

```c
#define TC_ERROR(fmt, ...)
```

相关声明：[TC_ERROR](#a6fcd0e6c5448a9198cdaed1e88e86e1b)。

<a id="r_a31562104efbbaec65655dc0b661c0164"></a>

```c
#define TC_PRINT(fmt, ...)
```

相关声明：[TC_PRINT](#a31562104efbbaec65655dc0b661c0164)。

<a id="r_a21b72e847828bb33f121df1f49d6049b"></a>

```c
#define TC_SUMMARY_PRINT(fmt, ...)
```

相关声明：[TC_SUMMARY_PRINT](#a21b72e847828bb33f121df1f49d6049b)。

<a id="r_a84a358e0dffa73ee8008c082863b0019"></a>

```c
#define TC_START_PRINT(name)
```

相关声明：[TC_START_PRINT](#a84a358e0dffa73ee8008c082863b0019)。

<a id="r_aa090341b412763239ae09ba1f7a52b3e"></a>

```c
#define TC_START(name)
```

相关声明：[TC_START](#aa090341b412763239ae09ba1f7a52b3e)。

<a id="r_a8efc6e62889487dc919facca8ec42ecf"></a>

```c
#define TC_END(result, fmt, ...)
```

相关声明：[TC_END](#a8efc6e62889487dc919facca8ec42ecf)。

<a id="r_a257c3ffdd1721ca67ec44f6b9e8d9641"></a>

```c
#define TC_END_PRINT(result, fmt, ...)
```

相关声明：[TC_END_PRINT](#a257c3ffdd1721ca67ec44f6b9e8d9641)。

<a id="r_a51a8593a108ecdec4e29cbe2169d3a6b"></a>

```c
#define TC_END_RESULT(result)
```

相关声明：[TC_END_RESULT](#a51a8593a108ecdec4e29cbe2169d3a6b)。

<a id="r_ada1b9d646eb10dd40f23667a19a57714"></a>

```c
#define TC_END_RESULT_CUSTOM(result, func)
```

相关声明：[TC_END_RESULT_CUSTOM](#ada1b9d646eb10dd40f23667a19a57714)。

<a id="r_a342b3d937894dfa380580b96b73664a4"></a>

```c
#define TC_SUITE_PRINT(fmt, ...)
```

相关声明：[TC_SUITE_PRINT](#a342b3d937894dfa380580b96b73664a4)。

<a id="r_a175563de07188c1cc549cf88b0e78575"></a>

```c
#define TC_SUITE_START(name)
```

相关声明：[TC_SUITE_START](#a175563de07188c1cc549cf88b0e78575)。

<a id="r_af972f5db041628380c3f8a66c1513bdc"></a>

```c
#define TC_SUITE_END(name, result)
```

相关声明：[TC_SUITE_END](#af972f5db041628380c3f8a66c1513bdc)。

<a id="r_a4aa57b8a67f3d67de8aec48a268a12ae"></a>

```c
#define TC_END_POST(result)
```

相关声明：[TC_END_POST](#a4aa57b8a67f3d67de8aec48a268a12ae)。

<a id="r_a3a7161b4346dd5e84a4a86d6ebdc0b9e"></a>

```c
#define TC_END_REPORT(result)
```

相关声明：[TC_END_REPORT](#a3a7161b4346dd5e84a4a86d6ebdc0b9e)。

<a id="r_aeae77e3905136ee851f1907cae75b9d9"></a>

```c
#define TC_CMD_DEFINE(name)
```

相关声明：[TC_CMD_DEFINE](#aeae77e3905136ee851f1907cae75b9d9)。

<a id="r_a44c72e8abf49266ead1bd1c97121e76b"></a>

```c
#define TC_CMD_ITEM(name)
```

相关声明：[TC_CMD_ITEM](#a44c72e8abf49266ead1bd1c97121e76b)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 51.2\_函数（Functions）

<a id="r_a9e2302e8d62cfefe7df86e62489efe29"></a>

```c
static const char * TC_RESULT_TO_STR (int result)
```

相关声明：[TC_RESULT_TO_STR](#a9e2302e8d62cfefe7df86e62489efe29)。

<a id="r_a497dd92db8a77681994baee1ba3f0847"></a>

```c
static void get_start_time_cyc (void)
```

相关声明：[get_start_time_cyc](#a497dd92db8a77681994baee1ba3f0847)。

<a id="r_ab6f8f2a5ffd8240715e1eef0dfd27907"></a>

```c
static void get_test_duration_ms (void)
```

相关声明：[get_test_duration_ms](#ab6f8f2a5ffd8240715e1eef0dfd27907)。

<a id="r_a30c304c5caa2145085e83fdbd5fa24e4"></a>

```c
static void print_nothing (const char *fmt,...)
```

相关声明：[print_nothing](#a30c304c5caa2145085e83fdbd5fa24e4)。

<a id="header-var-members"></a>
<a id="var-members"></a>

## 51.3\_变量（Variables）

<a id="r_ad3aec479c61df7656ae28f68aa4dc4a5"></a>

```c
static uint32_t tc_start_time
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[tc_start_time](#ad3aec479c61df7656ae28f68aa4dc4a5)。

<a id="r_a9bb8eafa6af5b875097421ba21a8dfc8"></a>

```c
static uint32_t tc_spend_time
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[tc_spend_time](#a9bb8eafa6af5b875097421ba21a8dfc8)。

## 51.4\_详细说明（Detailed Documentation）

<a id="a8e446c4d4b1517a80c371ca370c56ac3"></a>

### `FMT_ERROR`

```c
#define FMT_ERROR "%s - %s@%d. "
```

<a id="aec98e66470b575771ed484118095b692"></a>

### `PRINT_DATA`

```c
#define PRINT_DATA ( fmt, ... )
```

展开值（Value）：

```c
printk(fmt, ##__VA_ARGS__)
```

<a id="af72c5654279b3d1e227e8dec30411944"></a>

### `PRINT_LINE`

```c
#define PRINT_LINE
```

展开值（Value）：

```c
PRINT_DATA(                                                        \
        "============================================================" \
        "=======\n")
```

<a id="a5486258f1f34d3baeda92a74b63c27c3"></a>

### `TASK_STACK_SIZE`

```c
#define TASK_STACK_SIZE (1024 * 2)
```

<a id="aeae77e3905136ee851f1907cae75b9d9"></a>

### `TC_CMD_DEFINE`

```c
#define TC_CMD_DEFINE ( name)
```

展开值（Value）：

```c
int cmd_##name(int argc, char *argv[])          \
{                                               \
        TC_START(__func__);                     \
        name();                                 \
        TC_END_RESULT(TC_PASS);                 \
        return 0;                               \
}
```

<a id="a44c72e8abf49266ead1bd1c97121e76b"></a>

### `TC_CMD_ITEM`

```c
#define TC_CMD_ITEM ( name)
```

展开值（Value）：

```c
{STRINGIFY(name), cmd_##name, "none"}
```

<a id="a8efc6e62889487dc919facca8ec42ecf"></a>

### `TC_END`

```c
#define TC_END ( result, fmt, ... )
```

展开值（Value）：

```c
PRINT_DATA(fmt, ##__VA_ARGS__)
```

<a id="a4aa57b8a67f3d67de8aec48a268a12ae"></a>

### `TC_END_POST`

```c
#define TC_END_POST ( result)
```

<a id="a257c3ffdd1721ca67ec44f6b9e8d9641"></a>

### `TC_END_PRINT`

```c
#define TC_END_PRINT ( result, fmt, ... )
```

展开值（Value）：

```c
print_nothing(fmt)
```

<a id="a3a7161b4346dd5e84a4a86d6ebdc0b9e"></a>

### `TC_END_REPORT`

```c
#define TC_END_REPORT ( result)
```

展开值（Value）：

```c
do {                                                    \
        PRINT_LINE;                                         \
        TC_PRINT_RUNID;                                         \
        TC_END(result,                                      \
               "PROJECT EXECUTION %s\n",               \
               (result) == TC_PASS ? "SUCCESSFUL" : "FAILED");  \
        TC_END_POST(result);                                    \
} while (false)
```

<a id="a51a8593a108ecdec4e29cbe2169d3a6b"></a>

### `TC_END_RESULT`

```c
#define TC_END_RESULT ( result)
```

展开值（Value）：

```c
Z_TC_END_RESULT((result), __func__)
```

<a id="ada1b9d646eb10dd40f23667a19a57714"></a>

### `TC_END_RESULT_CUSTOM`

```c
#define TC_END_RESULT_CUSTOM ( result, func )
```

展开值（Value）：

```c
Z_TC_END_RESULT((result), func)
```

<a id="a6fcd0e6c5448a9198cdaed1e88e86e1b"></a>

### `TC_ERROR`

```c
#define TC_ERROR ( fmt, ... )
```

展开值（Value）：

```c
do {                                                 \
        PRINT_DATA(FMT_ERROR, "FAIL", __func__, __LINE__); \
        PRINT_DATA(fmt, ##__VA_ARGS__);                  \
} while (false)
```

<a id="a196c300c18de32c79d757131b579a3a5"></a>

### `TC_FAIL`

```c
#define TC_FAIL 1
```

<a id="ac5103b154fa450c478c2bf3f520cb8ff"></a>

### `TC_FAIL_STR`

```c
#define TC_FAIL_STR "FAIL"
```

<a id="ac0108c70de44b3186c7ead1c1430b3d1"></a>

### `TC_FLAKY`

```c
#define TC_FLAKY 3
```

<a id="a584cf09eac3d2fa3758924cb843cdbf5"></a>

### `TC_FLAKY_STR`

```c
#define TC_FLAKY_STR "FLAKY"
```

<a id="afb66a88e5d1e781aeb5aa9739a8fe868"></a>

### `TC_PASS`

```c
#define TC_PASS 0
```

<a id="a991995992ef5c23b7c6cf7138b394437"></a>

### `TC_PASS_STR`

```c
#define TC_PASS_STR "PASS"
```

<a id="a31562104efbbaec65655dc0b661c0164"></a>

### `TC_PRINT`

```c
#define TC_PRINT ( fmt, ... )
```

展开值（Value）：

```c
print_nothing(fmt, ##__VA_ARGS__)
```

<a id="a82cdb6d03f070075b576cbe1dab5e71a"></a>

### `TC_PRINT_RUNID`

```c
#define TC_PRINT_RUNID do {} while (false)
```

报告运行标识符（Run ID）。

定义 C 预处理器（CPP）符号 `TC_RUNID` 时，例如由编译环境定义，调用此项会打印字符串 `RunID: <TC_RUNID>`；`TC_END_REPORT()` 也会调用它。

主要用于自动执行多个测试用例时，验证运行的是预期映像，因为目标设备有时未能正确烧录或复位。

`TC_RUNID` 可以是任意字符串，它会转换为字符串字面量（string literal）。

<a id="a96f7bbefdafd3b13e9ee460477b13097"></a>

### `TC_PRINT_RUNID_START`

```c
#define TC_PRINT_RUNID_START do {} while (false)
```

在测试映像开始执行时报告运行标识符（Run ID）。

在一次运行开始时输出，与 `TC_PRINT_RUNID` 相对应，使本次运行的输出由两个运行标识符标记（Run ID markers）包围。如果上一次运行的输出尚未处理完就观察到新的开始标记，日志解析器即可判断设备已重新启动、待处理输出已经过时，无须依赖可选的启动横幅（boot banner）。

定义 `TC_RUNID` 时打印 `RunID started: <TC_RUNID>`，否则不打印任何内容。

<a id="abafb6d8cf1e1a3bb2247d5384d1d5461"></a>

### `TC_SKIP`

```c
#define TC_SKIP 2
```

<a id="a586f060684ebfc5db4105a30370a41d0"></a>

### `TC_SKIP_STR`

```c
#define TC_SKIP_STR "SKIP"
```

<a id="aa090341b412763239ae09ba1f7a52b3e"></a>

### `TC_START`

```c
#define TC_START ( name)
```

展开值（Value）：

```c
do {                                                            \
        TC_START_PRINT(name);                   \
} while (0)
```

<a id="a84a358e0dffa73ee8008c082863b0019"></a>

### `TC_START_PRINT`

```c
#define TC_START_PRINT ( name)
```

展开值（Value）：

```c
print_nothing(name)
```

<a id="acd142b5f39b0d6fe5216440432ef2c72"></a>

### `TC_STR`

```c
#define TC_STR ( x)
```

展开值（Value）：

```c
TC_STR_HELPER(x)
```

<a id="a91250f31fc327df207018b9c66493677"></a>

### `TC_STR_HELPER`

```c
#define TC_STR_HELPER ( x)
```

展开值（Value）：

```c
#x
```

<a id="af972f5db041628380c3f8a66c1513bdc"></a>

### `TC_SUITE_END`

```c
#define TC_SUITE_END ( name, result )
```

展开值（Value）：

```c
do {                                                            \
        if (result != TC_FAIL) {                                \
                TC_SUITE_PRINT("TESTSUITE %s succeeded\n", name);       \
        } else {                                                \
                TC_SUITE_PRINT("TESTSUITE %s failed.\n", name); \
        }                                                       \
} while (false)
```

<a id="a342b3d937894dfa380580b96b73664a4"></a>

### `TC_SUITE_PRINT`

```c
#define TC_SUITE_PRINT ( fmt, ... )
```

展开值（Value）：

```c
PRINT_DATA(fmt, ##__VA_ARGS__)
```

<a id="a175563de07188c1cc549cf88b0e78575"></a>

### `TC_SUITE_START`

```c
#define TC_SUITE_START ( name)
```

展开值（Value）：

```c
do {                                                    \
        TC_SUITE_PRINT("Running TESTSUITE %s\n", name); \
        PRINT_LINE;                                     \
} while (false)
```

<a id="a21b72e847828bb33f121df1f49d6049b"></a>

### `TC_SUMMARY_PRINT`

```c
#define TC_SUMMARY_PRINT ( fmt, ... )
```

展开值（Value）：

```c
PRINT_DATA(fmt, ##__VA_ARGS__)
```

<a id="a497dd92db8a77681994baee1ba3f0847"></a>

### `get_start_time_cyc()`

```c
void get_start_time_cyc ( void )
```

声明属性：`inline`、`static`。

<a id="ab6f8f2a5ffd8240715e1eef0dfd27907"></a>

### `get_test_duration_ms()`

```c
void get_test_duration_ms ( void )
```

声明属性：`inline`、`static`。

<a id="a30c304c5caa2145085e83fdbd5fa24e4"></a>

### `print_nothing()`

```c
void print_nothing ( const char * fmt, ... )
```

声明属性：`inline`、`static`。

<a id="a9e2302e8d62cfefe7df86e62489efe29"></a>

### `TC_RESULT_TO_STR()`

```c
const char * TC_RESULT_TO_STR ( int result)
```

声明属性：`inline`、`static`。

<a id="a9bb8eafa6af5b875097421ba21a8dfc8"></a>

### `tc_spend_time`

```c
uint32_t tc_spend_time
```

声明属性：`static`。

<a id="ad3aec479c61df7656ae28f68aa4dc4a5"></a>

### `tc_start_time`

```c
uint32_t tc_start_time
```

声明属性：`static`。


## 51.5\_原页交叉引用（Cross References）

- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [string.h](../api_source_supplement_reference/P216_string.h_源码浏览.md)
- [zephyr/sys/printk.h](../api_source_runtime_reference/P051_printk.h_源码浏览.md)
- [查看此文件的源码。](../api_source_architecture_reference/P021_tc_util.h_源码浏览.md)
- [false](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a65e9886d74aaee76545e83dd09011727)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [printk](https://docs.zephyrproject.org/latest/doxygen/html/printk_8h.html#a1bce54a738ce2d9dd6d95ee842ec237c)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="aprintk_8h_html_a1bce54a738ce2d9dd6d95ee842ec237c"></a>
<a id="atc__util_8h_html_aec98e66470b575771ed484118095b692"></a>
<a id="atc__util_8h_html_afb66a88e5d1e781aeb5aa9739a8fe868"></a>
<a id="atc__util_8h_html_a30c304c5caa2145085e83fdbd5fa24e4"></a>
<a id="atc__util_8h_html_a82cdb6d03f070075b576cbe1dab5e71a"></a>
<a id="atc__util_8h_html_af72c5654279b3d1e227e8dec30411944"></a>
<a id="atc__util_8h_html_a8e446c4d4b1517a80c371ca370c56ac3"></a>
<a id="atc__util_8h_html_a91250f31fc327df207018b9c66493677"></a>
<a id="atc__util_8h_html_a196c300c18de32c79d757131b579a3a5"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>
<a id="doc-var-members"></a>
<a id="header-doc-var-members"></a>

---

[上一章](P050_zephyr__llext__symbol.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P052_zephyr__bluetooth__testing.h_文件参考.md)

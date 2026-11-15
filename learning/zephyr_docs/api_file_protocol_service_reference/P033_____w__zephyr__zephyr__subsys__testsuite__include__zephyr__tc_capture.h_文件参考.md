---
id: learning.zephyr-docs.api-file-protocol-service-reference.page-33
title: ____w__zephyr__zephyr__subsys__testsuite__include__zephyr__tc_capture.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/tc__capture_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第33章\_\_\_\_\_w\_\_zephyr\_\_zephyr\_\_subsys\_\_testsuite\_\_include\_\_zephyr\_\_tc\_capture.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/tc__capture_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

测试输出捕获（Test Output Capture）的辅助接口。

<a id="details"></a>

```c
#include <stdbool.h>
#include <stddef.h>
```

查看此文件的源码。

测试输出捕获辅助工具（Test Output Capture Helper）。将测试生成的文本诊断输出捕获到内存缓冲区（In-memory Buffer），便于断言检查，无需每个测试自行连接日志后端（Log Backend）或 `printk` 钩子。两条输出路径均透明处理：通过包装 `printk` 字符输出钩子，捕获 `printk()` 输出以及经 `printk` 路由的 `CONFIG_LOG_MODE_MINIMAL` 日志；完整日志输出，即使用真实后端模式的 `CONFIG_LOG`，通过专用日志后端捕获。典型用法见原始示例。

原页内嵌的符号说明：`zassert_true(cond, ...)` 断言条件为真，定义位于 `ztest_assert.h:298`；`tc_capture_stop(void)` 停止捕获；`tc_capture_start(void)` 开始捕获；`tc_capture_contains(const char *substr)` 检查捕获输出是否包含子串。

**注意（Note）：**捕获日志输出时，消息必须在调用 `tc_capture_stop()` 之前到达后端。应使用 `CONFIG_LOG_MODE_IMMEDIATE`，或通过其他方式刷新日志，避免遗漏延迟消息（Deferred Messages）。

```c
tc_capture_start();
do_something_that_prints();
tc_capture_stop();
zassert_true(tc_capture_contains("expected text"));
```

<a id="header-func-members"></a>
<a id="func-members"></a>

## 33.1\_函数（Functions）

<a id="r_ad98361ae538dba0ba74614de75d951bb"></a>

```c
void tc_capture_start (void)
```

相关声明：[tc_capture_start](#ad98361ae538dba0ba74614de75d951bb)。

开始捕获测试输出（Test Output）。

<a id="r_ac2625e49dd53df7deec771032bcce292"></a>

```c
void tc_capture_stop (void)
```

相关声明：[tc_capture_stop](#ac2625e49dd53df7deec771032bcce292)。

停止捕获测试输出（Test Output）。

<a id="r_ae4d70b8a2ff709bed3a955b1b9ed612d"></a>

```c
bool tc_capture_contains (const char *substr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[tc_capture_contains](#ae4d70b8a2ff709bed3a955b1b9ed612d)。

检查捕获的输出（Captured Output）是否包含子串（Substring）。

<a id="r_acf7be87c335c18979f438fd944d31f17"></a>

```c
size_t tc_capture_get (char *dst, size_t size)
```

相关声明：[tc_capture_get](#acf7be87c335c18979f438fd944d31f17)。

将捕获的输出（Captured Output）复制到调用者提供的缓冲区。

<a id="r_afd40b7a2fc58f3e27c03fe3eae59a582"></a>

```c
void tc_capture_clear (void)
```

相关声明：[tc_capture_clear](#afd40b7a2fc58f3e27c03fe3eae59a582)。

丢弃全部已捕获输出（Captured Output），但不停止捕获。

## 33.2\_详细说明（Detailed Documentation）

<a id="afd40b7a2fc58f3e27c03fe3eae59a582"></a>

### `tc_capture_clear()`

```c
void tc_capture_clear ( void )
```

丢弃全部已捕获输出（Captured Output），但不停止捕获。

<a id="ae4d70b8a2ff709bed3a955b1b9ed612d"></a>

### `tc_capture_contains()`

```c
bool tc_capture_contains ( const char * substr)
```

检查捕获的输出（Captured Output）是否包含子串（Substring）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `substr` | 要搜索的 NUL 结尾子串（NUL-terminated Substring）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `true` | 捕获的输出（Captured Output）中存在 `substr` 时。 |
| `false` | 其他情况。 |

<a id="acf7be87c335c18979f438fd944d31f17"></a>

### `tc_capture_get()`

```c
size_t tc_capture_get ( char * dst, size_t size )
```

将捕获的输出（Captured Output）复制到调用者提供的缓冲区。

副本始终以 NUL 结尾（除非 `size` 为 `0`），并按 `size` 截断以适应缓冲区。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dst` | 目标缓冲区。 |
| `size` | `dst` 的大小，单位为字节（Bytes）。 |

**返回（Returns）**：**返回值（Returns）：**复制的字节数，不包含 NUL 终止符（Terminator）。

<a id="ad98361ae538dba0ba74614de75d951bb"></a>

### `tc_capture_start()`

```c
void tc_capture_start ( void )
```

开始捕获测试输出（Test Output）。

清除此前捕获的数据，并开始将 `printk` 和日志输出记录到内部捕获缓冲区（Capture Buffer）。捕获持续到调用 `tc_capture_stop()` 为止。输出仍转发到正常控制台，因此常规测试日志不受影响。

<a id="ac2625e49dd53df7deec771032bcce292"></a>

### `tc_capture_stop()`

```c
void tc_capture_stop ( void )
```

停止捕获测试输出（Test Output）。

恢复正常输出路径（Output Path）。捕获的数据仍可通过 `tc_capture_contains()` 和 `tc_capture_get()` 检查，直到下次调用 `tc_capture_start()` 或 `tc_capture_clear()`。


## 33.3\_原页交叉引用（Cross References）

- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P855_tc_capture.h_源码浏览.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [printk()](https://docs.zephyrproject.org/latest/doxygen/html/printk_8h.html#a1bce54a738ce2d9dd6d95ee842ec237c)
- [CONFIG_LOG_MODE_MINIMAL](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG_MODE_MINIMAL)
- [CONFIG_LOG](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG)
- [zassert_true](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assert.html#gaeebddde19012223e3d5e853a1dac3ac5)
- [CONFIG_LOG_MODE_IMMEDIATE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG_MODE_IMMEDIATE)
- [true](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7)
- [false](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a65e9886d74aaee76545e83dd09011727)

<a id="header-details"></a>
<a id="agroup__ztest__assert_html_gaeebddde19012223e3d5e853a1dac3ac5"></a>
<a id="atc__capture_8h_html_ac2625e49dd53df7deec771032bcce292"></a>
<a id="atc__capture_8h_html_ad98361ae538dba0ba74614de75d951bb"></a>
<a id="atc__capture_8h_html_ae4d70b8a2ff709bed3a955b1b9ed612d"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P032_zephyr__dt-bindings__clock__stm32_common_clocks.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P034_zephyr__net__wifi_utils.h_文件参考.md)

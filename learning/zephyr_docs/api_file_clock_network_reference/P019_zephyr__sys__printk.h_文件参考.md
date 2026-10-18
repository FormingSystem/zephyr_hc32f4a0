---
id: learning.zephyr-docs.api-file-clock-network-reference.page-19
title: zephyr__sys__printk.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/printk_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第19章\_zephyr\_\_sys\_\_printk.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/printk_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/toolchain.h>
#include <stddef.h>
#include <stdarg.h>
#include <inttypes.h>
```

查看此文件的源码。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 19.1\_函数（Functions）

<a id="r_a1bce54a738ce2d9dd6d95ee842ec237c"></a>

```c
void printk (const char *fmt,...)
```

相关声明：[printk](#a1bce54a738ce2d9dd6d95ee842ec237c)。

打印内核调试消息（Kernel Debugging Message）。

<a id="r_a9b5fa01884b98d143218af0cd0ffe841"></a>

```c
void vprintk (const char *fmt, va_list ap)
```

相关声明：[vprintk](#a9b5fa01884b98d143218af0cd0ffe841)。

打印内核调试消息（Kernel Debugging Message），va_list 版本。

<a id="r_a2cf2f614c79e9e798eaffad1b47fb365"></a>

```c
void printk_unlocked (const char *fmt,...)
```

相关声明：[printk_unlocked](#a2cf2f614c79e9e798eaffad1b47fb365)。

不获取 printk 锁而输出字符串。

<a id="r_ae8424da1d9d23bcfa739790545b058fc"></a>

```c
void vprintk_unlocked (const char *fmt, va_list ap)
```

相关声明：[vprintk_unlocked](#ae8424da1d9d23bcfa739790545b058fc)。

完全不加锁而输出字符串，va_list 版本。

<a id="r_a4cc4b043259c5bb605c17702c988a68c"></a>

```c
void printk_panic (void)
```

相关声明：[printk_panic](#a4cc4b043259c5bb605c17702c988a68c)。

停止 printk() 获取其锁，供崩溃报告（Crash Reporting）使用。

<a id="r_a0b0af71688f7e9170103d771d4e1eab2"></a>

```c
int snprintk (char *str, size_t size, const char *fmt,...)
```

相关声明：[snprintk](#a0b0af71688f7e9170103d771d4e1eab2)。

将内核调试消息（Kernel Debugging Message）打印到缓冲区。

<a id="r_ae824cc3368607ee5d45f860a1389794a"></a>

```c
int vsnprintk (char *str, size_t size, const char *fmt, va_list ap)
```

相关声明：[vsnprintk](#ae824cc3368607ee5d45f860a1389794a)。

将内核调试消息（Kernel Debugging Message）打印到缓冲区，va_list 版本。

## 19.2\_详细说明（Detailed Documentation）

<a id="a1bce54a738ce2d9dd6d95ee842ec237c"></a>

### `printk()`

```c
void printk ( const char * fmt, ... )
```

打印内核调试消息（Kernel Debugging Message）。

此例程向系统控制台打印内核调试消息（Kernel Debugging Message），立即输出，不进行互斥或缓冲（Mutual Exclusion or Buffering）。

支持一组基本的转换说明符（Conversion Specifier）字符：

- 有符号十进制（Signed Decimal）：%d、%i。
- 无符号十进制（Unsigned Decimal）：%u。
- 无符号十六进制（Unsigned Hexadecimal）：%x；%X 按 %x 处理。
- 指针（Pointer）：%p。
- 字符串（String）：%s。
- 字符（Character）：%c。
- 百分号（Percent）：%%。

支持字段宽度（Field Width），可带或不带前导零。支持长度属性 h、hh、l、ll 和 z。但 lld 与 lli 仅在整数值可由 long 容纳时打印，否则打印 ERR。完整的 64 位值可以用 llx 打印。不支持标志和精度属性（Flags and Precision Attributes）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `fmt` | 格式字符串（Format String）。 |
| `...` | 可选格式参数列表（Format Arguments）。 |

<a id="a4cc4b043259c5bb605c17702c988a68c"></a>

### `printk_panic()`

```c
void printk_panic ( void )
```

停止 printk() 获取其锁，供崩溃报告（Crash Reporting）使用。

调用后，printk() 的行为相当于所有调用方都使用 printk_unlocked()。一旦进入致命错误处理（Fatal Error Handling），就不能再信任锁：出错上下文可能持锁终止，或锁可能归属于永不再运行的 CPU，后续 printk() 因此可能永久阻塞。单个调用点无法修复此问题，因为失败后执行到的代码并不知道系统处于崩溃状态。

由致命错误处理路径（Fatal Error Path）调用。这是单向变更，在系统剩余生命周期内持续生效。

<a id="a2cf2f614c79e9e798eaffad1b47fb365"></a>

### `printk_unlocked()`

```c
void printk_unlocked ( const char * fmt, ... )
```

不获取 printk 锁而输出字符串。

输出与 printk() 相同，但从不获取自旋锁（Spinlock），并绕过日志子系统和用户模式缓冲区；文本直接进入平台的字符输出钩子（Character Output Hook）。

供无法获取锁的调用方使用：持锁者已终止的崩溃、从 printk() 内部重入的输出，或自旋锁所需原子操作尚不可用的早期启动阶段。输出可能与并发 printk() 交错，但可以避免挂死或丢失输出。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `fmt` | 格式字符串（Format String）。 |
| `...` | 可选格式参数列表（Format Arguments）。 |

**说明（Note）**：注意（Note）：仅限内核上下文（Kernel Context）；是否无锁及无锁程度取决于输出钩子（Output Hook）。

<a id="a0b0af71688f7e9170103d771d4e1eab2"></a>

### `snprintk()`

```c
int snprintk ( char * str, size_t size, const char * fmt, ... )
```

将内核调试消息（Kernel Debugging Message）打印到缓冲区。

按 printk() 的方式格式化，但写入 str 而非控制台。放不下时截断输出；只要 size 不为零，就以 NUL 终止。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `str` | 待写入缓冲区（Buffer）。 |
| `size` | 缓冲区大小，单位为字节。 |
| `fmt` | 格式字符串（Format String）。 |
| `...` | 可选格式参数列表（Format Arguments）。 |

**返回（Returns）**：返回值（Returns）：如果容量足够本应写入的字符数，不含终止 NUL。返回值大于或等于 size 表示输出被截断。

<a id="a9b5fa01884b98d143218af0cd0ffe841"></a>

### `vprintk()`

```c
void vprintk ( const char * fmt, va_list ap )
```

打印内核调试消息（Kernel Debugging Message），va_list 版本。

输出格式参见 printk()。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `fmt` | 格式字符串（Format String）。 |
| `ap` | 格式化参数（Format Arguments）。 |

<a id="ae8424da1d9d23bcfa739790545b058fc"></a>

### `vprintk_unlocked()`

```c
void vprintk_unlocked ( const char * fmt, va_list ap )
```

完全不加锁而输出字符串，va_list 版本。

适用场景及所放弃的保证参见 printk_unlocked()。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `fmt` | 格式字符串（Format String）。 |
| `ap` | 格式化参数（Format Arguments）。 |

<a id="ae824cc3368607ee5d45f860a1389794a"></a>

### `vsnprintk()`

```c
int vsnprintk ( char * str, size_t size, const char * fmt, va_list ap )
```

将内核调试消息（Kernel Debugging Message）打印到缓冲区，va_list 版本。

格式化和缓冲区处理参见 snprintk()。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `str` | 待写入缓冲区（Buffer）。 |
| `size` | 缓冲区大小，单位为字节。 |
| `fmt` | 格式字符串（Format String）。 |
| `ap` | 格式化参数（Format Arguments）。 |

**返回（Returns）**：返回值（Returns）：如果容量足够本应写入的字符数，不含终止 NUL。


## 19.3\_原页交叉引用（Cross References）

- [zephyr/toolchain.h](../api_source_compiler_device_reference/P023_toolchain.h_源码浏览.md)
- [inttypes.h](../api_source_http_wifi_reference/P005_inttypes.h_源码浏览.md)
- [查看此文件的源码。](../api_source_runtime_reference/P051_printk.h_源码浏览.md)

<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P018_zephyr__net__mqtt.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P020_zephyr__dt-bindings__gpio__realtek-rts5817-gpio.h_文件参考.md)

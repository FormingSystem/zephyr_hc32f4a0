---
id: learning.zephyr-docs.shell-remote-reference.page-4
title: 远端Shell命令行头文件参考
kind: reference
status: maintained
domains: [zephyr, kernel, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/shell__remote__cli_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_远端Shell命令行头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/shell__remote__cli_8h.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入远端Shell接口、命令行接口与消息数据结构。源码跟踪译注与官方原文分开标示。

远端Shell客户端（Remote Shell Client）的API。

<a id="details"></a>

```c
#include <zephyr/sys/cbprintf.h>
#include <zephyr/shell/shell.h>
```

查看此文件的源码。

远端Shell客户端（Remote Shell Client）的API。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 4.1\_宏定义（Macros）

<a id="r_abecb5928ee628306857bd473bb18684e"></a>

```c
#define SHELL_REMOTE_CLI_ALIGN sizeof(long long)
```

相关声明：[SHELL_REMOTE_CLI_ALIGN](#abecb5928ee628306857bd473bb18684e)。

远端Shell命令行接口（CLI）所用cbprintf包的对齐（Alignment）。

<a id="r_a6b59d1cfc325f0ef68d1ffc725199755"></a>

```c
#define SHELL_REMOTE_CLI_FPRINTF(_sh, _color, ...)
```

相关声明：[SHELL_REMOTE_CLI_FPRINTF](#a6b59d1cfc325f0ef68d1ffc725199755)。

向远端Shell打印格式化字符串（Formatted String）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 4.2\_函数（Functions）

<a id="r_a60806c208a7a319faf4f9467e4d55946"></a>

```c
void shell_remote_cli_cbpprintf (const struct shell *sh, enum shell_vt100_color color, void *package, size_t len)
```

相关声明：[shell_remote_cli_cbpprintf](#a60806c208a7a319faf4f9467e4d55946)、[shell](../shell_core_reference/P004_Shell实例结构.md)、[shell_vt100_color](../shell_core_reference/P001_Shell核心接口.md#ga6dcf569be711db32286fb1ef2dcf36d2)。

向远端Shell打印格式化字符串（Formatted String）。

<a id="r_a851c444b07279f370d3a62ab6ce71d3d"></a>

```c
void shell_remote_cmd_process (void)
```

相关声明：[shell_remote_cmd_process](#a851c444b07279f370d3a62ab6ce71d3d)。

禁用CONFIG_MULTITHREADING时，在主执行上下文（Main Context）中处理远端消息。

## 4.3\_详细说明（Detailed Documentation）

<a id="abecb5928ee628306857bd473bb18684e"></a>

### `SHELL_REMOTE_CLI_ALIGN`

```c
#define SHELL_REMOTE_CLI_ALIGN sizeof(long long)
```

远端Shell命令行接口（CLI）所用cbprintf包的对齐（Alignment）。

<a id="a6b59d1cfc325f0ef68d1ffc725199755"></a>

### `SHELL_REMOTE_CLI_FPRINTF`

```c
#define SHELL_REMOTE_CLI_FPRINTF ( _sh, _color, ... )
```

展开值（Value）：

```c
do {                                                                                       \
        int _plen;                                                                         \
        void *_pkg;                                                                        \
        uint32_t _options =                                                                \
                CBPRINTF_PACKAGE_ADD_RO_STR_POS | CBPRINTF_PACKAGE_ADD_RW_STR_POS;         \
        CBPRINTF_STATIC_PACKAGE(NULL, 0, _plen, SHELL_REMOTE_CLI_ALIGN, _options,          \
                                __VA_ARGS__);                                              \
        _pkg = __builtin_alloca_with_align(_plen, 8);                                      \
        CBPRINTF_STATIC_PACKAGE(_pkg, _plen, _plen, SHELL_REMOTE_CLI_ALIGN, _options,      \
                                __VA_ARGS__);                                              \
        shell_remote_cli_cbpprintf(_sh, _color, _pkg, _plen);                              \
} while (0)
```

向远端Shell打印格式化字符串（Formatted String）。

此宏使用静态打包（Static Packaging）构建包，所需空间在栈（Stack）上分配。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_sh` | 打印目标Shell。 |
| `_color` | 文本颜色（Text Color）。 |
| `...` | 格式化字符串（Formatted String）。 |

<a id="a60806c208a7a319faf4f9467e4d55946"></a>

### `shell_remote_cli_cbpprintf()`

```c
void shell_remote_cli_cbpprintf ( const struct shell * sh, enum shell_vt100_color color, void * package, size_t len )
```

向远端Shell打印格式化字符串（Formatted String）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] sh` | Shell实例指针。 |
| `[in] color` | 打印文本的颜色（Printed Text Color）。 |
| `[in] package` | 包指针（Package Pointer）。 |
| `[in] len` | 包长度（Package Length）。 |

<a id="a851c444b07279f370d3a62ab6ce71d3d"></a>

### `shell_remote_cmd_process()`

```c
void shell_remote_cmd_process ( void )
```

禁用CONFIG_MULTITHREADING时，在主执行上下文（Main Context）中处理远端消息。

## 4.4\_源码定位与版本边界

源码定位：[include/zephyr/shell/shell_remote_cli.h](../../../include/zephyr/shell/shell_remote_cli.h)、[subsys/shell/shell_remote_cli.c](../../../subsys/shell/shell_remote_cli.c)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：以下源码跟踪译注独立于官方正文，依据来源记录中登记的官方main文件。

> 译注——源码核对：FPRINTF宏先计算包大小，在当前栈上分配空间，再静态打包并同步调用cbpprintf。包内字符串的转换与复制在发送实现中处理；不能从临时包地址推导出它可在宏结束后长期保存。

> 译注——源码核对：SHELL_REMOTE_CLI_ALIGN定义为sizeof(long long)，而__builtin_alloca_with_align调用中的8是编译器内建函数的对齐参数，单位为位，见[GCC栈分配内建函数说明](https://gcc.gnu.org/onlinedocs/gcc/Stack-Allocation.html)。原始宏保留，不能将这个8直接解释为8字节对齐保证。

> 译注——源码核对：禁用多线程时，shell_remote_cmd_process用于从主执行上下文处理暂存消息。启用多线程时，当前实现按配置使用工作项或专用线程；调用者应遵守接口的配置条件。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 4.5\_原页交叉引用（Cross References）

- [zephyr/sys/cbprintf.h](../cbprintf_reference/P006_回调格式化输出头文件源码.md)
- [zephyr/shell/shell.h](../shell_core_reference/P003_Shell核心头文件源码.md)
- [查看此文件的源码](P005_远端Shell命令行头文件源码.md)
- [shell](../shell_core_reference/P004_Shell实例结构.md)
- [shell_vt100_color](../shell_core_reference/P001_Shell核心接口.md#ga6dcf569be711db32286fb1ef2dcf36d2)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [CBPRINTF_PACKAGE_ADD_RO_STR_POS](../cbprintf_reference/P013_格式化包创建标志.md#ga406facc18bf99afe16d453253d042dbb)
- [CBPRINTF_PACKAGE_ADD_RW_STR_POS](../cbprintf_reference/P013_格式化包创建标志.md#gac6ac59dda3a1a8a4572c1012b4adcbaa)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__CBPRINTF__PACKAGE__FLAGS_html_ga406facc18bf99afe16d453253d042dbb"></a>
<a id="agroup__CBPRINTF__PACKAGE__FLAGS_html_gac6ac59dda3a1a8a4572c1012b4adcbaa"></a>
<a id="ashell__remote__cli_8h_html_abecb5928ee628306857bd473bb18684e"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P003_远端Shell头文件源码.md) · [返回大纲](大纲.md) · [下一章](P005_远端Shell命令行头文件源码.md)

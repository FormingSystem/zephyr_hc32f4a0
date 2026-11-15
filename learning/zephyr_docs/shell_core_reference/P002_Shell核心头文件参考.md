---
id: learning.zephyr-docs.shell-core-reference.page-2
title: Shell核心头文件参考
kind: reference
status: maintained
domains: [zephyr, shell, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/shell_2shell_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_Shell核心头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/shell_2shell_8h.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入Shell核心接口、实例与传输数据结构和完整头文件源码。源码跟踪译注与官方原文分开标示。

Shell子系统（Shell Subsystem）的头文件。

<a id="details"></a>

```c
#include <zephyr/kernel.h>
#include <zephyr/shell/shell_types.h>
#include <zephyr/shell/shell_history.h>
#include <zephyr/shell/shell_fprintf.h>
#include <zephyr/shell/shell_log_backend.h>
#include <zephyr/shell/shell_string_conv.h>
#include <zephyr/logging/log_instance.h>
#include <zephyr/logging/log.h>
#include <zephyr/sys/iterable_sections.h>
#include <zephyr/sys/util.h>
#include <zephyr/toolchain.h>
```

查看此文件的源码。

Shell子系统（Shell Subsystem）的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 2.1\_数据结构（Data Structures）

<a id="r_shell_5Fcmd_5Fentry"></a>

```c
union shell_cmd_entry
```

相关声明：[shell_cmd_entry](P011_Shell命令条目联合体.md)。

Shell命令描述符（Command Descriptor）。

<a id="r_shell_5Fstatic_5Fargs"></a>

```c
struct shell_static_args
```

相关声明：[shell_static_args](P007_Shell命令参数约束.md)。

Shell命令的参数数量约束（Argument Count Constraints）与远端路由（Remote Routing）。

<a id="r_shell_5Fstatic_5Fentry"></a>

```c
struct shell_static_entry
```

相关声明：[shell_static_entry](P008_Shell静态命令条目.md)。

Shell静态命令描述符（Static Command Descriptor）。

<a id="r_shell_5Fcmd_5Fhelp"></a>

```c
struct shell_cmd_help
```

相关声明：[shell_cmd_help](P006_Shell命令帮助结构.md)。

Shell结构化帮助描述符（Structured Help Descriptor）。

<a id="r_shell_5Ftransport_5Fapi"></a>

```c
struct shell_transport_api
```

相关声明：[shell_transport_api](P010_Shell传输接口结构.md)。

统一的Shell传输接口（Transport Interface）。

<a id="r_shell_5Ftransport"></a>

```c
struct shell_transport
```

相关声明：[shell_transport](P009_Shell传输实例.md)。

Shell传输实例（Transport Instance）。

<a id="r_shell_5Fctx"></a>

```c
struct shell_ctx
```

相关声明：[shell_ctx](P005_Shell运行上下文.md)。

Shell实例上下文（Instance Context）。

<a id="r_shell"></a>

```c
struct shell
```

相关声明：[shell](P004_Shell实例结构.md)。

Shell实例内部结构（Instance Internals）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 2.2\_宏定义（Macros）

<a id="r_ga2b64d0c6e086ea227e85fe50312896f7"></a>

```c
#define SHELL_OPT_ARG_RAW (0xFE)
```

相关声明：[SHELL_OPT_ARG_RAW](P001_Shell核心接口.md#ga2b64d0c6e086ea227e85fe50312896f7)。

表示将所有可选参数作为一个未经格式处理的参数（Unformatted Argument）的标志。

<a id="r_ga0e2b3ac54184ae15f13e2024df1ac69b"></a>

```c
#define SHELL_OPT_ARG_CHECK_SKIP (0xFF)
```

相关声明：[SHELL_OPT_ARG_CHECK_SKIP](P001_Shell核心接口.md#ga0e2b3ac54184ae15f13e2024df1ac69b)。

表示可选参数数量不受限制的标志。

<a id="r_gaba166d98da7258a2a50abc94c1b744c8"></a>

```c
#define SHELL_OPT_ARG_MAX (0xFD)
```

相关声明：[SHELL_OPT_ARG_MAX](P001_Shell核心接口.md#gaba166d98da7258a2a50abc94c1b744c8)。

表示可校验的最大可选参数数量的标志。

<a id="r_ga1e66e9bc319d9c028e404f05022f8a6e"></a>

```c
#define SHELL_CMD_FLAG_REMOTE_ROOT BIT(0)
```

相关声明：[SHELL_CMD_FLAG_REMOTE_ROOT](P001_Shell核心接口.md#ga1e66e9bc319d9c028e404f05022f8a6e)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

表示远端根命令（Root Remote Command）的标志。

<a id="r_gae3da8b6143ccbf46a08806296cd0bc9e"></a>

```c
#define SHELL_CMD_FLAG_REMOTE_SUBCMD BIT(1)
```

相关声明：[SHELL_CMD_FLAG_REMOTE_SUBCMD](P001_Shell核心接口.md#gae3da8b6143ccbf46a08806296cd0bc9e)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

表示远端子命令（Remote Subcommand）的标志。

<a id="r_gacf66d1ef4c3ae7d18a5f0668c667ed77"></a>

```c
#define SHELL_HELP(_description, _usage)
```

相关声明：[SHELL_HELP](P001_Shell核心接口.md#gacf66d1ef4c3ae7d18a5f0668c667ed77)。

内联创建结构化帮助（Structured Help）的辅助宏。

<a id="r_gae8a8bbcbb842027c02a319b3fb976a3d"></a>

```c
#define SHELL_CMD_ARG_REGISTER(syntax, subcmd, help, handler, mandatory, optional)
```

相关声明：[SHELL_CMD_ARG_REGISTER](P001_Shell核心接口.md#gae8a8bbcbb842027c02a319b3fb976a3d)。

定义并添加带必需参数数量约束的根命令（Root Command，第0级）的宏。

<a id="r_ga6a3ed4ea9051ac138d22cc39134fb2e5"></a>

```c
#define SHELL_COND_CMD_ARG_REGISTER(flag, syntax, subcmd, help, handler, mandatory, optional)
```

相关声明：[SHELL_COND_CMD_ARG_REGISTER](P001_Shell核心接口.md#ga6a3ed4ea9051ac138d22cc39134fb2e5)。

定义并添加带必需参数数量约束的条件根命令（Conditional Root Command，第0级）的宏。

<a id="r_ga06060b98eb505300a3dcc8f922a8e7ab"></a>

```c
#define SHELL_CMD_REGISTER(syntax, subcmd, help, handler)
```

相关声明：[SHELL_CMD_REGISTER](P001_Shell核心接口.md#ga06060b98eb505300a3dcc8f922a8e7ab)。

定义并添加带参数根命令（Root Command，第0级）的宏。

<a id="r_ga62782121ece6af076407c94935ec94e4"></a>

```c
#define SHELL_COND_CMD_REGISTER(flag, syntax, subcmd, help, handler)
```

相关声明：[SHELL_COND_CMD_REGISTER](P001_Shell核心接口.md#ga62782121ece6af076407c94935ec94e4)。

定义并添加带参数条件根命令（Conditional Root Command，第0级）的宏。

<a id="r_gacb2d1a969368efdbeec704ee6e962dee"></a>

```c
#define SHELL_STATIC_SUBCMD_SET_CREATE(name, ...)
```

相关声明：[SHELL_STATIC_SUBCMD_SET_CREATE](P001_Shell核心接口.md#gacb2d1a969368efdbeec704ee6e962dee)。

创建子命令集合（Subcommand Set）的宏。

<a id="r_ga1e314886b70ee2e7e0763cd945a1a988"></a>

```c
#define SHELL_SUBCMD_SET_CREATE(_name, _parent)
```

相关声明：[SHELL_SUBCMD_SET_CREATE](P001_Shell核心接口.md#ga1e314886b70ee2e7e0763cd945a1a988)。

创建子命令集合（Subcommand Set）。

<a id="r_gab1b643efbaee748be0256e904642e310"></a>

```c
#define SHELL_SUBCMD_COND_ADD(_flag, _parent, _syntax, _subcmd, _help, _handler, _mand, _opt)
```

相关声明：[SHELL_SUBCMD_COND_ADD](P001_Shell核心接口.md#gab1b643efbaee748be0256e904642e310)。

按条件向子命令集合添加命令。

<a id="r_ga85b0afcacd3831bf5c724590765e035f"></a>

```c
#define SHELL_SUBCMD_ADD(_parent, _syntax, _subcmd, _help, _handler, _mand, _opt)
```

相关声明：[SHELL_SUBCMD_ADD](P001_Shell核心接口.md#ga85b0afcacd3831bf5c724590765e035f)。

向子命令集合添加命令。

<a id="r_ga4f7a3432f76541eb226a426507e10174"></a>

```c
#define SHELL_SUBCMD_SET_END {0}
```

相关声明：[SHELL_SUBCMD_SET_END](P001_Shell核心接口.md#ga4f7a3432f76541eb226a426507e10174)。

定义子命令集合结束标记（Ending Subcommands Set）。

<a id="r_gafa6d91c36c36eb68d3f241ed0c7e7131"></a>

```c
#define SHELL_DYNAMIC_CMD_CREATE(name, get)
```

相关声明：[SHELL_DYNAMIC_CMD_CREATE](P001_Shell核心接口.md#gafa6d91c36c36eb68d3f241ed0c7e7131)。

创建动态条目（Dynamic Entry）的宏。

<a id="r_gad762c496a2ced65069b6d1d02a4d925c"></a>

```c
#define SHELL_CMD_ARG(syntax, subcmd, help, handler, mand, opt)
```

相关声明：[SHELL_CMD_ARG](P001_Shell核心接口.md#gad762c496a2ced65069b6d1d02a4d925c)。

初始化带参数的Shell命令。

<a id="r_ga68229f89484c3459d77cebb450ee1f24"></a>

```c
#define SHELL_COND_CMD_ARG(flag, syntax, subcmd, help, handler, mand, opt)
```

相关声明：[SHELL_COND_CMD_ARG](P001_Shell核心接口.md#ga68229f89484c3459d77cebb450ee1f24)。

按条件初始化带参数的Shell命令。

<a id="r_ga18657f55b8fc37a84660f040a89186bf"></a>

```c
#define SHELL_EXPR_CMD_ARG(_expr, _syntax, _subcmd, _help, _handler, _mand, _opt, _remote_cmd, _remote_id)
```

相关声明：[SHELL_EXPR_CMD_ARG](P001_Shell核心接口.md#ga18657f55b8fc37a84660f040a89186bf)。

编译期表达式结果非零时，初始化带参数的条件Shell命令。

<a id="r_ga24ade9db85af9a8776a45ba0084f4cca"></a>

```c
#define SHELL_CMD(_syntax, _subcmd, _help, _handler)
```

相关声明：[SHELL_CMD](P001_Shell核心接口.md#ga24ade9db85af9a8776a45ba0084f4cca)。

初始化Shell命令。

<a id="r_ga6e27d86443067df4792623f1a04d1ee1"></a>

```c
#define SHELL_COND_CMD(_flag, _syntax, _subcmd, _help, _handler)
```

相关声明：[SHELL_COND_CMD](P001_Shell核心接口.md#ga6e27d86443067df4792623f1a04d1ee1)。

按条件初始化Shell命令。

<a id="r_ga59a835edbd7db3acdcb204248c0cf5fd"></a>

```c
#define SHELL_EXPR_CMD(_expr, _syntax, _subcmd, _help, _handler)
```

相关声明：[SHELL_EXPR_CMD](P001_Shell核心接口.md#ga59a835edbd7db3acdcb204248c0cf5fd)。

编译期表达式结果非零时初始化Shell命令。

<a id="r_ga401e19cf8ec8601b8a96fe8e95a2b4d2"></a>

```c
#define SHELL_SUBCMD_DICT_SET_CREATE(_name, _handler, ...)
```

相关声明：[SHELL_SUBCMD_DICT_SET_CREATE](P001_Shell核心接口.md#ga401e19cf8ec8601b8a96fe8e95a2b4d2)。

初始化Shell字典命令（Dictionary Commands）。

<a id="r_ga158405143b49e4888cb135fec83ad22c"></a>

```c
#define SHELL_DEFINE(_name, _prompt, _transport_iface, _log_queue_size, _log_timeout, _shell_flag)
```

相关声明：[SHELL_DEFINE](P001_Shell核心接口.md#ga158405143b49e4888cb135fec83ad22c)。

定义Shell实例（Shell Instance）的宏。

<a id="r_ga4c3a7db0c2bdbf36bbf72302a04bb44d"></a>

```c
#define SHELL_NORMAL SHELL_VT100_COLOR_DEFAULT
```

相关声明：[SHELL_NORMAL](P001_Shell核心接口.md#ga4c3a7db0c2bdbf36bbf72302a04bb44d)、[SHELL_VT100_COLOR_DEFAULT](P001_Shell核心接口.md#gga6dcf569be711db32286fb1ef2dcf36d2a32de6063c44948beeb8501fed9b7d18e)。

用于shell_fprintf函数的终端默认文本颜色（Default Text Color）。

<a id="r_gaac0ea96fbb5885432dca93174c9ad4e6"></a>

```c
#define SHELL_INFO SHELL_VT100_COLOR_GREEN
```

相关声明：[SHELL_INFO](P001_Shell核心接口.md#gaac0ea96fbb5885432dca93174c9ad4e6)、[SHELL_VT100_COLOR_GREEN](P001_Shell核心接口.md#gga6dcf569be711db32286fb1ef2dcf36d2ac6fce9bc89ceb0043697b26cca380c8a)。

用于shell_fprintf函数的绿色文本（Green Text）。

<a id="r_gacc7c6e7b1fc65cc350353cc166da528b"></a>

```c
#define SHELL_OPTION SHELL_VT100_COLOR_CYAN
```

相关声明：[SHELL_OPTION](P001_Shell核心接口.md#gacc7c6e7b1fc65cc350353cc166da528b)、[SHELL_VT100_COLOR_CYAN](P001_Shell核心接口.md#gga6dcf569be711db32286fb1ef2dcf36d2a618a6789463b1980f1086ee128c65972)。

用于shell_fprintf函数的青色文本（Cyan Text）。

<a id="r_ga118dd6829e092423a85e2b6de07f8dd3"></a>

```c
#define SHELL_WARNING SHELL_VT100_COLOR_YELLOW
```

相关声明：[SHELL_WARNING](P001_Shell核心接口.md#ga118dd6829e092423a85e2b6de07f8dd3)、[SHELL_VT100_COLOR_YELLOW](P001_Shell核心接口.md#gga6dcf569be711db32286fb1ef2dcf36d2adb8fbc39eddceb95f523eed8d5c5bf7d)。

用于shell_fprintf函数的黄色文本（Yellow Text）。

<a id="r_ga7664f5e184e9b41ac92e033f7b8d885d"></a>

```c
#define SHELL_ERROR SHELL_VT100_COLOR_RED
```

相关声明：[SHELL_ERROR](P001_Shell核心接口.md#ga7664f5e184e9b41ac92e033f7b8d885d)、[SHELL_VT100_COLOR_RED](P001_Shell核心接口.md#gga6dcf569be711db32286fb1ef2dcf36d2a6f6be6e431dc8e905c5734b4e9c32af4)。

用于shell_fprintf函数的红色文本（Red Text）。

<a id="r_ga1fd1671311b112f0c87ab2dafd801105"></a>

```c
#define shell_fprintf(sh, color, fmt, ...)
```

相关声明：[shell_fprintf](P001_Shell核心接口.md#ga1fd1671311b112f0c87ab2dafd801105)。

类似printf的函数，向Shell发送格式化数据流（Formatted Data Stream）。

<a id="r_ga9382959c41fe6850c2daa51306b3c5fd"></a>

```c
#define shell_info(_sh, _ft, ...)
```

相关声明：[shell_info](P001_Shell核心接口.md#ga9382959c41fe6850c2daa51306b3c5fd)。

向Shell打印信息消息（Info Message）。

<a id="r_ga2285d8085d3696bf1c568213d31dabc7"></a>

```c
#define shell_fprintf_info(_sh, _ft, ...)
```

相关声明：[shell_fprintf_info](P001_Shell核心接口.md#ga2285d8085d3696bf1c568213d31dabc7)。

向Shell打印信息消息（Info Message）。

<a id="r_ga3126019b2100d1ccb2d4dc5efb7d8228"></a>

```c
#define shell_print(_sh, _ft, ...)
```

相关声明：[shell_print](P001_Shell核心接口.md#ga3126019b2100d1ccb2d4dc5efb7d8228)。

向Shell打印普通消息（Normal Message）。

<a id="r_gafe3749d6ed0867052d74365c40a702fc"></a>

```c
#define shell_fprintf_normal(_sh, _ft, ...)
```

相关声明：[shell_fprintf_normal](P001_Shell核心接口.md#gafe3749d6ed0867052d74365c40a702fc)。

向Shell打印普通消息（Normal Message）。

<a id="r_ga3d886cfd7b4340b2e71a92bd7c4534d9"></a>

```c
#define shell_warn(_sh, _ft, ...)
```

相关声明：[shell_warn](P001_Shell核心接口.md#ga3d886cfd7b4340b2e71a92bd7c4534d9)。

向Shell打印警告消息（Warning Message）。

<a id="r_ga214fff4fc56f5a90c4063dad9c233f1b"></a>

```c
#define shell_fprintf_warn(_sh, _ft, ...)
```

相关声明：[shell_fprintf_warn](P001_Shell核心接口.md#ga214fff4fc56f5a90c4063dad9c233f1b)。

向Shell打印警告消息（Warning Message）。

<a id="r_ga408141c02209a9549cb9063f24ef3731"></a>

```c
#define shell_error(_sh, _ft, ...)
```

相关声明：[shell_error](P001_Shell核心接口.md#ga408141c02209a9549cb9063f24ef3731)。

向Shell打印错误消息（Error Message）。

<a id="r_gac32c42fb696c2198c73c2c73087cdfc3"></a>

```c
#define shell_fprintf_error(_sh, _ft, ...)
```

相关声明：[shell_fprintf_error](P001_Shell核心接口.md#gac32c42fb696c2198c73c2c73087cdfc3)。

向Shell打印错误消息（Error Message）。

<a id="r_ga3be3ecccd6ce1954883c5959c39c7927"></a>

```c
#define SHELL_CMD_HELP_PRINTED (1)
```

相关声明：[SHELL_CMD_HELP_PRINTED](P001_Shell核心接口.md#ga3be3ecccd6ce1954883c5959c39c7927)。

已打印命令帮助（Command Help）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 2.3\_类型定义（Typedefs）

<a id="r_gafc042f32bac2fdd4cbde9f943e29b008"></a>

```c
typedef void(* shell_dynamic_get) (size_t idx, struct shell_static_entry *entry)
```

相关声明：[shell_dynamic_get](P001_Shell核心接口.md#gafc042f32bac2fdd4cbde9f943e29b008)、[shell_static_entry](P008_Shell静态命令条目.md)。

Shell动态命令描述符（Dynamic Command Descriptor）。

<a id="r_gaa2b8cf8ac78b8355408ef94958ebdc70"></a>

```c
typedef bool(* shell_device_filter_t) (const struct device *dev)
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[shell_device_filter_t](P001_Shell核心接口.md#gaa2b8cf8ac78b8355408ef94958ebdc70)、[device](../device_reference/P002_设备对象结构.md)。

用于shell_device_filter的过滤回调类型（Filter Callback Type）。

<a id="r_ga331e7d19b9b0755486596f5ffc598338"></a>

```c
typedef int(* shell_cmd_handler) (const struct shell *sh, size_t argc, char **argv)
```

相关声明：[shell_cmd_handler](P001_Shell核心接口.md#ga331e7d19b9b0755486596f5ffc598338)、[shell](P004_Shell实例结构.md)。

Shell命令处理函数原型（Command Handler Prototype）。

<a id="r_ga182f247052041f1236d13726589885e2"></a>

```c
typedef int(* shell_dict_cmd_handler) (const struct shell *sh, size_t argc, char **argv, void *data)
```

相关声明：[shell_dict_cmd_handler](P001_Shell核心接口.md#ga182f247052041f1236d13726589885e2)、[shell](P004_Shell实例结构.md)。

Shell字典命令处理函数原型（Dictionary Command Handler Prototype）。

<a id="r_ga265807c2d8eba7b9ea633968627e085d"></a>

```c
typedef void(* shell_transport_handler_t) (enum shell_transport_evt evt, void *context)
```

相关声明：[shell_transport_handler_t](P001_Shell核心接口.md#ga265807c2d8eba7b9ea633968627e085d)。

Shell传输事件处理回调（Transport Event Handler Callback）。

<a id="r_ga0844a0ce151551d3ccf45d507e5bab25"></a>

```c
typedef void(* shell_uninit_cb_t) (const struct shell *sh, int res)
```

相关声明：[shell_uninit_cb_t](P001_Shell核心接口.md#ga0844a0ce151551d3ccf45d507e5bab25)、[shell](P004_Shell实例结构.md)。

Shell反初始化完成回调（Uninitialization Completion Callback）。

<a id="r_gacaddbcd6e84f377f39a5d69398996557"></a>

```c
typedef void(* shell_bypass_cb_t) (const struct shell *sh, uint8_t *data, size_t len, void *user_data)
```

相关声明：[shell_bypass_cb_t](P001_Shell核心接口.md#gacaddbcd6e84f377f39a5d69398996557)、[shell](P004_Shell实例结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

旁路回调（Bypass Callback）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 2.4\_枚举（Enumerations）

<a id="r_ga56bf30741f9ec7a6d94e5c18c2858948"></a>

```c
enum shell_flag { SHELL_FLAG_CRLF_DEFAULT = (1<<0) , SHELL_FLAG_OLF_CRLF = (1<<1) }
```

相关声明：[shell_flag](P001_Shell核心接口.md#ga56bf30741f9ec7a6d94e5c18c2858948)、[SHELL_FLAG_CRLF_DEFAULT](P001_Shell核心接口.md#gga56bf30741f9ec7a6d94e5c18c2858948a343ee559d6259111dbab529a283b23ab)、[SHELL_FLAG_OLF_CRLF](P001_Shell核心接口.md#gga56bf30741f9ec7a6d94e5c18c2858948ab6fec7b615b6de79e1d00d4117615446)。

设置Shell输出换行序列（Output Newline Sequence）的标志。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 2.5\_函数（Functions）

<a id="r_ga571db3aa3e024a09e82b117a74d6f248"></a>

```c
const struct device * shell_device_lookup (size_t idx, const char *prefix)
```

相关声明：[device](../device_reference/P002_设备对象结构.md)、[shell_device_lookup](P001_Shell核心接口.md#ga571db3aa3e024a09e82b117a74d6f248)。

按索引取得匹配的设备。（原文在matches后未给出匹配对象，参数说明见下文。）

<a id="r_ga8e83709f5e75d4cea51f42f41bb4e20f"></a>

```c
const struct device * shell_device_lookup_all (size_t idx, const char *prefix)
```

相关声明：[device](../device_reference/P002_设备对象结构.md)、[shell_device_lookup_all](P001_Shell核心接口.md#ga8e83709f5e75d4cea51f42f41bb4e20f)。

按索引取得匹配的设备。（原文在matches后未给出匹配对象，参数说明见下文。）

<a id="r_ga9f2994f2d6a55521a3e162a81299e4c3"></a>

```c
const struct device * shell_device_lookup_non_ready (size_t idx, const char *prefix)
```

相关声明：[device](../device_reference/P002_设备对象结构.md)、[shell_device_lookup_non_ready](P001_Shell核心接口.md#ga9f2994f2d6a55521a3e162a81299e4c3)。

按索引取得匹配的、未初始化设备。（原文在matches后未给出匹配对象，参数说明见下文。）

<a id="r_gae2a8e3d44a9bf5eb55be80833ac6eb5d"></a>

```c
const struct device * shell_device_filter (size_t idx, shell_device_filter_t filter)
```

相关声明：[device](../device_reference/P002_设备对象结构.md)、[shell_device_filter](P001_Shell核心接口.md#gae2a8e3d44a9bf5eb55be80833ac6eb5d)、[shell_device_filter_t](P001_Shell核心接口.md#gaa2b8cf8ac78b8355408ef94958ebdc70)。

根据索引与过滤器（Filter）取得设备。

<a id="r_ga7fb40045dc0a27c175e37a6c9cd84b53"></a>

```c
const struct device * shell_device_get_binding (const char *name)
```

相关声明：[device](../device_reference/P002_设备对象结构.md)、[shell_device_get_binding](P001_Shell核心接口.md#ga7fb40045dc0a27c175e37a6c9cd84b53)。

通过device::name字段或标签（Label）取得设备引用。

<a id="r_ga919147e222fe10ce14ab3c3a5c5a94e3"></a>

```c
const struct device * shell_device_get_binding_all (const char *name)
```

相关声明：[device](../device_reference/P002_设备对象结构.md)、[shell_device_get_binding_all](P001_Shell核心接口.md#ga919147e222fe10ce14ab3c3a5c5a94e3)。

通过device::name字段或标签（Label）取得设备引用。

<a id="r_ga061bf2530269ebf20d8e006dace5e33b"></a>

```c
static bool shell_help_is_structured (const char *help)
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[shell_help_is_structured](P001_Shell核心接口.md#ga061bf2530269ebf20d8e006dace5e33b)。

检查帮助字符串是否为结构化帮助（Structured Help）。

<a id="r_ga8764ff11603855a10419c48e46e8221c"></a>

```c
int shell_init (const struct shell *sh, const void *transport_config, struct shell_backend_config_flags cfg_flags, bool log_backend, uint32_t init_log_level)
```

相关声明：[shell_init](P001_Shell核心接口.md#ga8764ff11603855a10419c48e46e8221c)、[shell](P004_Shell实例结构.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[log_backend](../log_backend_reference/P004_日志后端结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

初始化传输层（Transport Layer）和Shell内部状态的函数。

<a id="r_ga07e76646c5065218464aa8ce78b75af3"></a>

```c
void shell_uninit (const struct shell *sh, shell_uninit_cb_t cb)
```

相关声明：[shell_uninit](P001_Shell核心接口.md#ga07e76646c5065218464aa8ce78b75af3)、[shell](P004_Shell实例结构.md)、[shell_uninit_cb_t](P001_Shell核心接口.md#ga0844a0ce151551d3ccf45d507e5bab25)。

反初始化传输层和Shell内部状态。

<a id="r_gad386d4e8077103e7976f25996fcc3132"></a>

```c
int shell_start (const struct shell *sh)
```

相关声明：[shell_start](P001_Shell核心接口.md#gad386d4e8077103e7976f25996fcc3132)、[shell](P004_Shell实例结构.md)。

启动Shell处理的函数。

<a id="r_gad27754d0beb31bc501f28f9ef26a362c"></a>

```c
int shell_stop (const struct shell *sh)
```

相关声明：[shell_stop](P001_Shell核心接口.md#gad27754d0beb31bc501f28f9ef26a362c)、[shell](P004_Shell实例结构.md)。

停止Shell处理的函数。

<a id="r_ga74a1c4edd803cad14c893fc9816e534f"></a>

```c
void shell_vfprintf (const struct shell *sh, enum shell_vt100_color color, const char *fmt, va_list args)
```

相关声明：[shell_vfprintf](P001_Shell核心接口.md#ga74a1c4edd803cad14c893fc9816e534f)、[shell](P004_Shell实例结构.md)、[shell_vt100_color](P001_Shell核心接口.md#ga6dcf569be711db32286fb1ef2dcf36d2)。

类似vprintf的函数，向Shell发送格式化数据流。

<a id="r_ga706aebd24cbdb7f14b9a324515414ecf"></a>

```c
void shell_cbpprintf (const struct shell *sh, enum shell_vt100_color color, void *package)
```

相关声明：[shell_cbpprintf](P001_Shell核心接口.md#ga706aebd24cbdb7f14b9a324515414ecf)、[shell](P004_Shell实例结构.md)、[shell_vt100_color](P001_Shell核心接口.md#ga6dcf569be711db32286fb1ef2dcf36d2)。

将cbprintf包格式化后以数据流形式发送到Shell的函数。

<a id="r_ga0b6e69b499c153ae8f7ba256d445f09d"></a>

```c
void shell_hexdump_line (const struct shell *sh, unsigned int offset, const uint8_t *data, size_t len)
```

相关声明：[shell_hexdump_line](P001_Shell核心接口.md#ga0b6e69b499c153ae8f7ba256d445f09d)、[shell](P004_Shell实例结构.md)、[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

以十六进制格式（Hexadecimal Format）打印一行数据。

<a id="r_gaeeba0b483974205c54e364d509badd42"></a>

```c
void shell_hexdump (const struct shell *sh, const uint8_t *data, size_t len)
```

相关声明：[shell_hexdump](P001_Shell核心接口.md#gaeeba0b483974205c54e364d509badd42)、[shell](P004_Shell实例结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

以十六进制格式打印数据。

<a id="r_ga7e66389d0faf15a2a7c31c68cdd9c36c"></a>

```c
void shell_process (const struct shell *sh)
```

相关声明：[shell_process](P001_Shell核心接口.md#ga7e66389d0faf15a2a7c31c68cdd9c36c)、[shell](P004_Shell实例结构.md)。

传输接口中有数据就绪时应执行的处理函数（Process Function）。

<a id="r_ga2113b7227b155755a7ab8a928f7ae499"></a>

```c
int shell_prompt_change (const struct shell *sh, const char *prompt)
```

相关声明：[shell_prompt_change](P001_Shell核心接口.md#ga2113b7227b155755a7ab8a928f7ae499)、[shell](P004_Shell实例结构.md)。

更改显示的Shell提示符（Prompt）。

<a id="r_ga9e4911ff2c3a07fa70711ddac83701d6"></a>

```c
static void shell_help (const struct shell *sh)
```

相关声明：[shell_help](P001_Shell核心接口.md#ga9e4911ff2c3a07fa70711ddac83701d6)、[shell](P004_Shell实例结构.md)。

打印当前命令的帮助。

<a id="r_gabfb6a1f1f53f90365de349348015311e"></a>

```c
int shell_execute_cmd (const struct shell *sh, const char *cmd)
```

相关声明：[shell_execute_cmd](P001_Shell核心接口.md#gabfb6a1f1f53f90365de349348015311e)、[shell](P004_Shell实例结构.md)、[cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)。

执行命令（Execute Command）。

<a id="r_ga768c606f2d50f24e9b607ba0a341686d"></a>

```c
int shell_set_root_cmd (const char *cmd)
```

相关声明：[shell_set_root_cmd](P001_Shell核心接口.md#ga768c606f2d50f24e9b607ba0a341686d)、[cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)。

为所有Shell实例设置根命令（Root Command）。

<a id="r_ga4d51d4dbb22bed5d040deabc7ab6dc9d"></a>

```c
void shell_set_bypass (const struct shell *sh, shell_bypass_cb_t bypass, void *user_data)
```

相关声明：[shell_set_bypass](P001_Shell核心接口.md#ga4d51d4dbb22bed5d040deabc7ab6dc9d)、[shell](P004_Shell实例结构.md)、[shell_bypass_cb_t](P001_Shell核心接口.md#gacaddbcd6e84f377f39a5d69398996557)。

设置旁路回调（Bypass Callback）。

<a id="r_ga79369ddfea2dc2cb5813c5eb5c67634a"></a>

```c
bool shell_ready (const struct shell *sh)
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[shell_ready](P001_Shell核心接口.md#ga79369ddfea2dc2cb5813c5eb5c67634a)、[shell](P004_Shell实例结构.md)。

取得Shell是否已就绪、能够执行命令的状态。

<a id="r_gaf1f41d8b6cd430357d593ab0fc5adfeb"></a>

```c
int shell_insert_mode_set (const struct shell *sh, bool val)
```

相关声明：[shell_insert_mode_set](P001_Shell核心接口.md#gaf1f41d8b6cd430357d593ab0fc5adfeb)、[shell](P004_Shell实例结构.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

允许应用控制文本插入模式（Insert Mode）。

<a id="r_ga7d5873456ba43ebd3cc86d25e3f4a72c"></a>

```c
int shell_use_colors_set (const struct shell *sh, bool val)
```

相关声明：[shell_use_colors_set](P001_Shell核心接口.md#ga7d5873456ba43ebd3cc86d25e3f4a72c)、[shell](P004_Shell实例结构.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

允许应用控制终端输出是否使用彩色语法（Colored Syntax）。

<a id="r_ga80ff4b3b4cc62e543fd510c14f55b42a"></a>

```c
int shell_use_vt100_set (const struct shell *sh, bool val)
```

相关声明：[shell_use_vt100_set](P001_Shell核心接口.md#ga80ff4b3b4cc62e543fd510c14f55b42a)、[shell](P004_Shell实例结构.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

允许应用控制终端是否使用VT100命令。

<a id="r_gad53881371bbaedfd3ef3ecf219706fd1"></a>

```c
int shell_echo_set (const struct shell *sh, bool val)
```

相关声明：[shell_echo_set](P001_Shell核心接口.md#gad53881371bbaedfd3ef3ecf219706fd1)、[shell](P004_Shell实例结构.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

允许应用控制是否回显用户输入（Echo）。

<a id="r_ga86fade2757d04c9220d5912a4ee540a0"></a>

```c
int shell_obscure_set (const struct shell *sh, bool obscure)
```

相关声明：[shell_obscure_set](P001_Shell核心接口.md#ga86fade2757d04c9220d5912a4ee540a0)、[shell](P004_Shell实例结构.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

允许应用控制是否用星号遮蔽用户输入（Obscure），可用于实现口令输入。

<a id="r_ga2df2997c4b04f3246c22f43b274a353b"></a>

```c
int shell_mode_delete_set (const struct shell *sh, bool val)
```

相关声明：[shell_mode_delete_set](P001_Shell核心接口.md#ga2df2997c4b04f3246c22f43b274a353b)、[shell](P004_Shell实例结构.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

允许应用控制Delete键执行退格（Backspace）还是删除（Delete）。

<a id="r_ga54dc053c92641bc9b9736bc2d61140f7"></a>

```c
int shell_get_return_value (const struct shell *sh)
```

相关声明：[shell_get_return_value](P001_Shell核心接口.md#ga54dc053c92641bc9b9736bc2d61140f7)、[shell](P004_Shell实例结构.md)。

取得最近一次执行的Shell命令的返回值。

<a id="r_ga313068db9c3b9972ca4129085d8605d5"></a>

```c
void shell_readline_prompt_set (const struct shell *sh, const char *prompt)
```

相关声明：[shell_readline_prompt_set](P001_Shell核心接口.md#ga313068db9c3b9972ca4129085d8605d5)、[shell](P004_Shell实例结构.md)。

为下一次shell_readline调用设置提示字符串（Prompt String）。

<a id="r_ga05b2eb80f3484216ef2e1d4bf9492453"></a>

```c
int shell_readline (const struct shell *sh, uint8_t *buf, size_t len, k_timeout_t timeout)
```

相关声明：[shell_readline](P001_Shell核心接口.md#ga05b2eb80f3484216ef2e1d4bf9492453)、[shell](P004_Shell实例结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

从Shell读取一行输入。

## 2.6\_源码定位与版本边界

源码定位：[include/zephyr/shell/shell.h](../../../include/zephyr/shell/shell.h)、[subsys/shell/shell.c](../../../subsys/shell/shell.c)、[subsys/shell/shell_utils.c](../../../subsys/shell/shell_utils.c)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：以下源码跟踪译注独立于官方正文。源码与公开接口按本次官方快照核对，未将隐藏的内部条目补造为公开说明。

> 译注——源码核对：命令注册中的mandatory包含命令名称本身；optional可使用原文规定的特殊标志。条件宏与表达式宏控制命令是否存在，原宏展开保留，用来核对处理函数和子命令在不同配置下的去留。

> 译注——源码核对：动态命令回调应按索引填入条目、保证语法名称按字母顺序排序，并在没有更多条目时将syntax设为NULL。返回指针或空条目的含义应遵守该回调协议，不能用未初始化字段代替结束标记。

> 译注——源码核对：shell_execute_cmd禁止在Shell命令上下文内调用，而shell_readline要求从Shell线程的命令处理函数调用。二者调用条件不同；异步旁路（Bypass）与同步读行也有明确的互斥使用条件。

> 译注——源码核对：readline提示字符串不会被复制，必须有效到读行返回；返回后提示设置会自动清除。缓冲区容量包含NUL终止字符，成功返回的长度不含该字符。

> 译注——源码核对：字符串转换成功时保留err原值，应预先初始化错误变量。返回0或false既可能是有效结果，也可能是失败时的返回值，需要同时检查err。

> 译注——源码核对：shell和shell_ctx原页只给出结构用途，内部字段由Doxygen隐藏；本册对应页如实保留这个公开范围，完整可见布局另见头文件源码。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 2.7\_原页交叉引用（Cross References）

- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [zephyr/shell/shell_types.h](../shell_util_reference/P008_Shell类型头文件源码.md)
- [zephyr/shell/shell_history.h](../shell_util_reference/P004_Shell命令历史头文件源码.md)
- [zephyr/shell/shell_fprintf.h](../shell_util_reference/P002_Shell格式化输出头文件源码.md)
- [zephyr/shell/shell_log_backend.h](../shell_backend_reference/P014_Shell日志后端头文件源码.md)
- [zephyr/shell/shell_string_conv.h](../shell_util_reference/P006_Shell字符串转换头文件源码.md)
- [zephyr/logging/log_instance.h](../log_internal_reference/P004_日志实例头文件源码.md)
- [zephyr/logging/log.h](../log_core_reference/P004_日志公共头文件源码.md)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P003_可遍历段辅助头文件源码.md)
- [zephyr/sys/util.h](../util_reference/P003_通用工具头文件源码.md)
- [zephyr/toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h_source.html)
- [查看此文件的源码](P003_Shell核心头文件源码.md)
- [shell_cmd_entry](P011_Shell命令条目联合体.md)
- [shell_static_args](P007_Shell命令参数约束.md)
- [shell_static_entry](P008_Shell静态命令条目.md)
- [shell_cmd_help](P006_Shell命令帮助结构.md)
- [shell_transport_api](P010_Shell传输接口结构.md)
- [shell_transport](P009_Shell传输实例.md)
- [shell_ctx](P005_Shell运行上下文.md)
- [shell](P004_Shell实例结构.md)
- [SHELL_OPT_ARG_RAW](P001_Shell核心接口.md#ga2b64d0c6e086ea227e85fe50312896f7)
- [SHELL_OPT_ARG_CHECK_SKIP](P001_Shell核心接口.md#ga0e2b3ac54184ae15f13e2024df1ac69b)
- [SHELL_OPT_ARG_MAX](P001_Shell核心接口.md#gaba166d98da7258a2a50abc94c1b744c8)
- [SHELL_CMD_FLAG_REMOTE_ROOT](P001_Shell核心接口.md#ga1e66e9bc319d9c028e404f05022f8a6e)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [SHELL_CMD_FLAG_REMOTE_SUBCMD](P001_Shell核心接口.md#gae3da8b6143ccbf46a08806296cd0bc9e)
- [SHELL_HELP](P001_Shell核心接口.md#gacf66d1ef4c3ae7d18a5f0668c667ed77)
- [SHELL_CMD_ARG_REGISTER](P001_Shell核心接口.md#gae8a8bbcbb842027c02a319b3fb976a3d)
- [SHELL_COND_CMD_ARG_REGISTER](P001_Shell核心接口.md#ga6a3ed4ea9051ac138d22cc39134fb2e5)
- [SHELL_CMD_REGISTER](P001_Shell核心接口.md#ga06060b98eb505300a3dcc8f922a8e7ab)
- [SHELL_COND_CMD_REGISTER](P001_Shell核心接口.md#ga62782121ece6af076407c94935ec94e4)
- [SHELL_STATIC_SUBCMD_SET_CREATE](P001_Shell核心接口.md#gacb2d1a969368efdbeec704ee6e962dee)
- [SHELL_SUBCMD_SET_CREATE](P001_Shell核心接口.md#ga1e314886b70ee2e7e0763cd945a1a988)
- [SHELL_SUBCMD_COND_ADD](P001_Shell核心接口.md#gab1b643efbaee748be0256e904642e310)
- [SHELL_SUBCMD_ADD](P001_Shell核心接口.md#ga85b0afcacd3831bf5c724590765e035f)
- [SHELL_SUBCMD_SET_END](P001_Shell核心接口.md#ga4f7a3432f76541eb226a426507e10174)
- [SHELL_DYNAMIC_CMD_CREATE](P001_Shell核心接口.md#gafa6d91c36c36eb68d3f241ed0c7e7131)
- [SHELL_CMD_ARG](P001_Shell核心接口.md#gad762c496a2ced65069b6d1d02a4d925c)
- [SHELL_COND_CMD_ARG](P001_Shell核心接口.md#ga68229f89484c3459d77cebb450ee1f24)
- [SHELL_EXPR_CMD_ARG](P001_Shell核心接口.md#ga18657f55b8fc37a84660f040a89186bf)
- [SHELL_CMD](P001_Shell核心接口.md#ga24ade9db85af9a8776a45ba0084f4cca)
- [SHELL_COND_CMD](P001_Shell核心接口.md#ga6e27d86443067df4792623f1a04d1ee1)
- [SHELL_EXPR_CMD](P001_Shell核心接口.md#ga59a835edbd7db3acdcb204248c0cf5fd)
- [SHELL_SUBCMD_DICT_SET_CREATE](P001_Shell核心接口.md#ga401e19cf8ec8601b8a96fe8e95a2b4d2)
- [SHELL_DEFINE](P001_Shell核心接口.md#ga158405143b49e4888cb135fec83ad22c)
- [SHELL_NORMAL](P001_Shell核心接口.md#ga4c3a7db0c2bdbf36bbf72302a04bb44d)
- [SHELL_VT100_COLOR_DEFAULT](P001_Shell核心接口.md#gga6dcf569be711db32286fb1ef2dcf36d2a32de6063c44948beeb8501fed9b7d18e)
- [SHELL_INFO](P001_Shell核心接口.md#gaac0ea96fbb5885432dca93174c9ad4e6)
- [SHELL_VT100_COLOR_GREEN](P001_Shell核心接口.md#gga6dcf569be711db32286fb1ef2dcf36d2ac6fce9bc89ceb0043697b26cca380c8a)
- [SHELL_OPTION](P001_Shell核心接口.md#gacc7c6e7b1fc65cc350353cc166da528b)
- [SHELL_VT100_COLOR_CYAN](P001_Shell核心接口.md#gga6dcf569be711db32286fb1ef2dcf36d2a618a6789463b1980f1086ee128c65972)
- [SHELL_WARNING](P001_Shell核心接口.md#ga118dd6829e092423a85e2b6de07f8dd3)
- [SHELL_VT100_COLOR_YELLOW](P001_Shell核心接口.md#gga6dcf569be711db32286fb1ef2dcf36d2adb8fbc39eddceb95f523eed8d5c5bf7d)
- [SHELL_ERROR](P001_Shell核心接口.md#ga7664f5e184e9b41ac92e033f7b8d885d)
- [SHELL_VT100_COLOR_RED](P001_Shell核心接口.md#gga6dcf569be711db32286fb1ef2dcf36d2a6f6be6e431dc8e905c5734b4e9c32af4)
- [shell_fprintf](P001_Shell核心接口.md#ga1fd1671311b112f0c87ab2dafd801105)
- [shell_info](P001_Shell核心接口.md#ga9382959c41fe6850c2daa51306b3c5fd)
- [shell_fprintf_info](P001_Shell核心接口.md#ga2285d8085d3696bf1c568213d31dabc7)
- [shell_print](P001_Shell核心接口.md#ga3126019b2100d1ccb2d4dc5efb7d8228)
- [shell_fprintf_normal](P001_Shell核心接口.md#gafe3749d6ed0867052d74365c40a702fc)
- [shell_warn](P001_Shell核心接口.md#ga3d886cfd7b4340b2e71a92bd7c4534d9)
- [shell_fprintf_warn](P001_Shell核心接口.md#ga214fff4fc56f5a90c4063dad9c233f1b)
- [shell_error](P001_Shell核心接口.md#ga408141c02209a9549cb9063f24ef3731)
- [shell_fprintf_error](P001_Shell核心接口.md#gac32c42fb696c2198c73c2c73087cdfc3)
- [SHELL_CMD_HELP_PRINTED](P001_Shell核心接口.md#ga3be3ecccd6ce1954883c5959c39c7927)
- [shell_dynamic_get](P001_Shell核心接口.md#gafc042f32bac2fdd4cbde9f943e29b008)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [shell_device_filter_t](P001_Shell核心接口.md#gaa2b8cf8ac78b8355408ef94958ebdc70)
- [device](../device_reference/P002_设备对象结构.md)
- [shell_cmd_handler](P001_Shell核心接口.md#ga331e7d19b9b0755486596f5ffc598338)
- [shell_dict_cmd_handler](P001_Shell核心接口.md#ga182f247052041f1236d13726589885e2)
- [shell_transport_handler_t](P001_Shell核心接口.md#ga265807c2d8eba7b9ea633968627e085d)
- [shell_uninit_cb_t](P001_Shell核心接口.md#ga0844a0ce151551d3ccf45d507e5bab25)
- [shell_bypass_cb_t](P001_Shell核心接口.md#gacaddbcd6e84f377f39a5d69398996557)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [shell_flag](P001_Shell核心接口.md#ga56bf30741f9ec7a6d94e5c18c2858948)
- [SHELL_FLAG_CRLF_DEFAULT](P001_Shell核心接口.md#gga56bf30741f9ec7a6d94e5c18c2858948a343ee559d6259111dbab529a283b23ab)
- [SHELL_FLAG_OLF_CRLF](P001_Shell核心接口.md#gga56bf30741f9ec7a6d94e5c18c2858948ab6fec7b615b6de79e1d00d4117615446)
- [shell_device_lookup](P001_Shell核心接口.md#ga571db3aa3e024a09e82b117a74d6f248)
- [shell_device_lookup_all](P001_Shell核心接口.md#ga8e83709f5e75d4cea51f42f41bb4e20f)
- [shell_device_lookup_non_ready](P001_Shell核心接口.md#ga9f2994f2d6a55521a3e162a81299e4c3)
- [shell_device_filter](P001_Shell核心接口.md#gae2a8e3d44a9bf5eb55be80833ac6eb5d)
- [shell_device_get_binding](P001_Shell核心接口.md#ga7fb40045dc0a27c175e37a6c9cd84b53)
- [device::name](../device_reference/P002_设备对象结构.md#a1e74e8d3b0b1a981c67e1d0284ccac3d)
- [shell_device_get_binding_all](P001_Shell核心接口.md#ga919147e222fe10ce14ab3c3a5c5a94e3)
- [shell_help_is_structured](P001_Shell核心接口.md#ga061bf2530269ebf20d8e006dace5e33b)
- [shell_init](P001_Shell核心接口.md#ga8764ff11603855a10419c48e46e8221c)
- [log_backend](../log_backend_reference/P004_日志后端结构.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [shell_uninit](P001_Shell核心接口.md#ga07e76646c5065218464aa8ce78b75af3)
- [shell_start](P001_Shell核心接口.md#gad386d4e8077103e7976f25996fcc3132)
- [shell_stop](P001_Shell核心接口.md#gad27754d0beb31bc501f28f9ef26a362c)
- [shell_vfprintf](P001_Shell核心接口.md#ga74a1c4edd803cad14c893fc9816e534f)
- [shell_vt100_color](P001_Shell核心接口.md#ga6dcf569be711db32286fb1ef2dcf36d2)
- [shell_cbpprintf](P001_Shell核心接口.md#ga706aebd24cbdb7f14b9a324515414ecf)
- [shell_hexdump_line](P001_Shell核心接口.md#ga0b6e69b499c153ae8f7ba256d445f09d)
- [unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)
- [shell_hexdump](P001_Shell核心接口.md#gaeeba0b483974205c54e364d509badd42)
- [shell_process](P001_Shell核心接口.md#ga7e66389d0faf15a2a7c31c68cdd9c36c)
- [shell_prompt_change](P001_Shell核心接口.md#ga2113b7227b155755a7ab8a928f7ae499)
- [shell_help](P001_Shell核心接口.md#ga9e4911ff2c3a07fa70711ddac83701d6)
- [shell_execute_cmd](P001_Shell核心接口.md#gabfb6a1f1f53f90365de349348015311e)
- [cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)
- [shell_set_root_cmd](P001_Shell核心接口.md#ga768c606f2d50f24e9b607ba0a341686d)
- [shell_set_bypass](P001_Shell核心接口.md#ga4d51d4dbb22bed5d040deabc7ab6dc9d)
- [shell_ready](P001_Shell核心接口.md#ga79369ddfea2dc2cb5813c5eb5c67634a)
- [shell_insert_mode_set](P001_Shell核心接口.md#gaf1f41d8b6cd430357d593ab0fc5adfeb)
- [shell_use_colors_set](P001_Shell核心接口.md#ga7d5873456ba43ebd3cc86d25e3f4a72c)
- [shell_use_vt100_set](P001_Shell核心接口.md#ga80ff4b3b4cc62e543fd510c14f55b42a)
- [shell_echo_set](P001_Shell核心接口.md#gad53881371bbaedfd3ef3ecf219706fd1)
- [shell_obscure_set](P001_Shell核心接口.md#ga86fade2757d04c9220d5912a4ee540a0)
- [shell_mode_delete_set](P001_Shell核心接口.md#ga2df2997c4b04f3246c22f43b274a353b)
- [shell_get_return_value](P001_Shell核心接口.md#ga54dc053c92641bc9b9736bc2d61140f7)
- [shell_readline_prompt_set](P001_Shell核心接口.md#ga313068db9c3b9972ca4129085d8605d5)
- [shell_readline](P001_Shell核心接口.md#ga05b2eb80f3484216ef2e1d4bf9492453)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)

<a id="header-details"></a>

---

[上一章](P001_Shell核心接口.md) · [返回大纲](大纲.md) · [下一章](P003_Shell核心头文件源码.md)

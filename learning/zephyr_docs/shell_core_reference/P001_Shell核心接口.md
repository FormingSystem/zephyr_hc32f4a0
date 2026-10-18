---
id: learning.zephyr-docs.shell-core-reference.page-1
title: Shell核心接口
kind: reference
status: maintained
domains: [zephyr, shell, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__shell__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_Shell核心接口

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__shell__api.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入Shell核心接口、实例与传输数据结构和完整头文件源码。源码跟踪译注与官方原文分开标示。

<a id="details"></a>

引入版本（Since）：1.14；接口版本（Version）：1.0.0。

<a id="header-groups"></a>
<a id="groups"></a>

## 1.1\_主题（Topics）

<a id="r_shell_5Fbackends"></a>

相关声明：[Shell后端（Shell Backends）](../shell_backend_reference/P001_Shell后端目录.md)。

将Shell实例连接到通信通道（Communication Channel）的传输后端（Transport Backend）。

<a id="r_shell_5Fremote"></a>

相关声明：[Shell remote](../shell_remote_reference/P001_远端Shell接口.md)。

远端Shell API（Shell Remote API）。

<a id="header-files"></a>
<a id="files"></a>

## 1.2\_文件（Files）

<a id="r_shell_2Eh"></a>

```c
file shell.h
```

相关声明：[shell.h](P002_Shell核心头文件参考.md)。

Shell子系统（Shell Subsystem）的头文件。

<a id="r_shell_5Fstring_5Fconv_2Eh"></a>

```c
file shell_string_conv.h
```

相关声明：[shell_string_conv.h](../shell_util_reference/P005_Shell字符串转换头文件参考.md)。

Shell字符串转换辅助函数（String Conversion Helpers）的头文件。

<a id="r_shell_5Ftypes_2Eh"></a>

```c
file shell_types.h
```

相关声明：[shell_types.h](../shell_util_reference/P007_Shell类型头文件参考.md)。

Shell终端类型与颜色（Terminal Types and Colors）的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 1.3\_数据结构（Data Structures）

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

## 1.4\_宏定义（Macros）

<a id="r_ga2b64d0c6e086ea227e85fe50312896f7"></a>

```c
#define SHELL_OPT_ARG_RAW (0xFE)
```

相关声明：[SHELL_OPT_ARG_RAW](#ga2b64d0c6e086ea227e85fe50312896f7)。

表示将所有可选参数作为一个未经格式处理的参数（Unformatted Argument）的标志。

<a id="r_ga0e2b3ac54184ae15f13e2024df1ac69b"></a>

```c
#define SHELL_OPT_ARG_CHECK_SKIP (0xFF)
```

相关声明：[SHELL_OPT_ARG_CHECK_SKIP](#ga0e2b3ac54184ae15f13e2024df1ac69b)。

表示可选参数数量不受限制的标志。

<a id="r_gaba166d98da7258a2a50abc94c1b744c8"></a>

```c
#define SHELL_OPT_ARG_MAX (0xFD)
```

相关声明：[SHELL_OPT_ARG_MAX](#gaba166d98da7258a2a50abc94c1b744c8)。

表示可校验的最大可选参数数量的标志。

<a id="r_ga1e66e9bc319d9c028e404f05022f8a6e"></a>

```c
#define SHELL_CMD_FLAG_REMOTE_ROOT BIT(0)
```

相关声明：[SHELL_CMD_FLAG_REMOTE_ROOT](#ga1e66e9bc319d9c028e404f05022f8a6e)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

表示远端根命令（Root Remote Command）的标志。

<a id="r_gae3da8b6143ccbf46a08806296cd0bc9e"></a>

```c
#define SHELL_CMD_FLAG_REMOTE_SUBCMD BIT(1)
```

相关声明：[SHELL_CMD_FLAG_REMOTE_SUBCMD](#gae3da8b6143ccbf46a08806296cd0bc9e)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

表示远端子命令（Remote Subcommand）的标志。

<a id="r_gacf66d1ef4c3ae7d18a5f0668c667ed77"></a>

```c
#define SHELL_HELP(_description, _usage)
```

相关声明：[SHELL_HELP](#gacf66d1ef4c3ae7d18a5f0668c667ed77)。

内联创建结构化帮助（Structured Help）的辅助宏。

<a id="r_gae8a8bbcbb842027c02a319b3fb976a3d"></a>

```c
#define SHELL_CMD_ARG_REGISTER(syntax, subcmd, help, handler, mandatory, optional)
```

相关声明：[SHELL_CMD_ARG_REGISTER](#gae8a8bbcbb842027c02a319b3fb976a3d)。

定义并添加带必需参数数量约束的根命令（Root Command，第0级）的宏。

<a id="r_ga6a3ed4ea9051ac138d22cc39134fb2e5"></a>

```c
#define SHELL_COND_CMD_ARG_REGISTER(flag, syntax, subcmd, help, handler, mandatory, optional)
```

相关声明：[SHELL_COND_CMD_ARG_REGISTER](#ga6a3ed4ea9051ac138d22cc39134fb2e5)。

定义并添加带必需参数数量约束的条件根命令（Conditional Root Command，第0级）的宏。

<a id="r_ga06060b98eb505300a3dcc8f922a8e7ab"></a>

```c
#define SHELL_CMD_REGISTER(syntax, subcmd, help, handler)
```

相关声明：[SHELL_CMD_REGISTER](#ga06060b98eb505300a3dcc8f922a8e7ab)。

定义并添加带参数根命令（Root Command，第0级）的宏。

<a id="r_ga62782121ece6af076407c94935ec94e4"></a>

```c
#define SHELL_COND_CMD_REGISTER(flag, syntax, subcmd, help, handler)
```

相关声明：[SHELL_COND_CMD_REGISTER](#ga62782121ece6af076407c94935ec94e4)。

定义并添加带参数条件根命令（Conditional Root Command，第0级）的宏。

<a id="r_gacb2d1a969368efdbeec704ee6e962dee"></a>

```c
#define SHELL_STATIC_SUBCMD_SET_CREATE(name, ...)
```

相关声明：[SHELL_STATIC_SUBCMD_SET_CREATE](#gacb2d1a969368efdbeec704ee6e962dee)。

创建子命令集合（Subcommand Set）的宏。

<a id="r_ga1e314886b70ee2e7e0763cd945a1a988"></a>

```c
#define SHELL_SUBCMD_SET_CREATE(_name, _parent)
```

相关声明：[SHELL_SUBCMD_SET_CREATE](#ga1e314886b70ee2e7e0763cd945a1a988)。

创建子命令集合（Subcommand Set）。

<a id="r_gab1b643efbaee748be0256e904642e310"></a>

```c
#define SHELL_SUBCMD_COND_ADD(_flag, _parent, _syntax, _subcmd, _help, _handler, _mand, _opt)
```

相关声明：[SHELL_SUBCMD_COND_ADD](#gab1b643efbaee748be0256e904642e310)。

按条件向子命令集合添加命令。

<a id="r_ga85b0afcacd3831bf5c724590765e035f"></a>

```c
#define SHELL_SUBCMD_ADD(_parent, _syntax, _subcmd, _help, _handler, _mand, _opt)
```

相关声明：[SHELL_SUBCMD_ADD](#ga85b0afcacd3831bf5c724590765e035f)。

向子命令集合添加命令。

<a id="r_ga4f7a3432f76541eb226a426507e10174"></a>

```c
#define SHELL_SUBCMD_SET_END {0}
```

相关声明：[SHELL_SUBCMD_SET_END](#ga4f7a3432f76541eb226a426507e10174)。

定义子命令集合结束标记（Ending Subcommands Set）。

<a id="r_gafa6d91c36c36eb68d3f241ed0c7e7131"></a>

```c
#define SHELL_DYNAMIC_CMD_CREATE(name, get)
```

相关声明：[SHELL_DYNAMIC_CMD_CREATE](#gafa6d91c36c36eb68d3f241ed0c7e7131)。

创建动态条目（Dynamic Entry）的宏。

<a id="r_gad762c496a2ced65069b6d1d02a4d925c"></a>

```c
#define SHELL_CMD_ARG(syntax, subcmd, help, handler, mand, opt)
```

相关声明：[SHELL_CMD_ARG](#gad762c496a2ced65069b6d1d02a4d925c)。

初始化带参数的Shell命令。

<a id="r_ga68229f89484c3459d77cebb450ee1f24"></a>

```c
#define SHELL_COND_CMD_ARG(flag, syntax, subcmd, help, handler, mand, opt)
```

相关声明：[SHELL_COND_CMD_ARG](#ga68229f89484c3459d77cebb450ee1f24)。

按条件初始化带参数的Shell命令。

<a id="r_ga18657f55b8fc37a84660f040a89186bf"></a>

```c
#define SHELL_EXPR_CMD_ARG(_expr, _syntax, _subcmd, _help, _handler, _mand, _opt, _remote_cmd, _remote_id)
```

相关声明：[SHELL_EXPR_CMD_ARG](#ga18657f55b8fc37a84660f040a89186bf)。

编译期表达式结果非零时，初始化带参数的条件Shell命令。

<a id="r_ga24ade9db85af9a8776a45ba0084f4cca"></a>

```c
#define SHELL_CMD(_syntax, _subcmd, _help, _handler)
```

相关声明：[SHELL_CMD](#ga24ade9db85af9a8776a45ba0084f4cca)。

初始化Shell命令。

<a id="r_ga6e27d86443067df4792623f1a04d1ee1"></a>

```c
#define SHELL_COND_CMD(_flag, _syntax, _subcmd, _help, _handler)
```

相关声明：[SHELL_COND_CMD](#ga6e27d86443067df4792623f1a04d1ee1)。

按条件初始化Shell命令。

<a id="r_ga59a835edbd7db3acdcb204248c0cf5fd"></a>

```c
#define SHELL_EXPR_CMD(_expr, _syntax, _subcmd, _help, _handler)
```

相关声明：[SHELL_EXPR_CMD](#ga59a835edbd7db3acdcb204248c0cf5fd)。

编译期表达式结果非零时初始化Shell命令。

<a id="r_ga401e19cf8ec8601b8a96fe8e95a2b4d2"></a>

```c
#define SHELL_SUBCMD_DICT_SET_CREATE(_name, _handler, ...)
```

相关声明：[SHELL_SUBCMD_DICT_SET_CREATE](#ga401e19cf8ec8601b8a96fe8e95a2b4d2)。

初始化Shell字典命令（Dictionary Commands）。

<a id="r_ga158405143b49e4888cb135fec83ad22c"></a>

```c
#define SHELL_DEFINE(_name, _prompt, _transport_iface, _log_queue_size, _log_timeout, _shell_flag)
```

相关声明：[SHELL_DEFINE](#ga158405143b49e4888cb135fec83ad22c)。

定义Shell实例（Shell Instance）的宏。

<a id="r_ga4c3a7db0c2bdbf36bbf72302a04bb44d"></a>

```c
#define SHELL_NORMAL SHELL_VT100_COLOR_DEFAULT
```

相关声明：[SHELL_NORMAL](#ga4c3a7db0c2bdbf36bbf72302a04bb44d)、[SHELL_VT100_COLOR_DEFAULT](#gga6dcf569be711db32286fb1ef2dcf36d2a32de6063c44948beeb8501fed9b7d18e)。

用于shell_fprintf函数的终端默认文本颜色（Default Text Color）。

<a id="r_gaac0ea96fbb5885432dca93174c9ad4e6"></a>

```c
#define SHELL_INFO SHELL_VT100_COLOR_GREEN
```

相关声明：[SHELL_INFO](#gaac0ea96fbb5885432dca93174c9ad4e6)、[SHELL_VT100_COLOR_GREEN](#gga6dcf569be711db32286fb1ef2dcf36d2ac6fce9bc89ceb0043697b26cca380c8a)。

用于shell_fprintf函数的绿色文本（Green Text）。

<a id="r_gacc7c6e7b1fc65cc350353cc166da528b"></a>

```c
#define SHELL_OPTION SHELL_VT100_COLOR_CYAN
```

相关声明：[SHELL_OPTION](#gacc7c6e7b1fc65cc350353cc166da528b)、[SHELL_VT100_COLOR_CYAN](#gga6dcf569be711db32286fb1ef2dcf36d2a618a6789463b1980f1086ee128c65972)。

用于shell_fprintf函数的青色文本（Cyan Text）。

<a id="r_ga118dd6829e092423a85e2b6de07f8dd3"></a>

```c
#define SHELL_WARNING SHELL_VT100_COLOR_YELLOW
```

相关声明：[SHELL_WARNING](#ga118dd6829e092423a85e2b6de07f8dd3)、[SHELL_VT100_COLOR_YELLOW](#gga6dcf569be711db32286fb1ef2dcf36d2adb8fbc39eddceb95f523eed8d5c5bf7d)。

用于shell_fprintf函数的黄色文本（Yellow Text）。

<a id="r_ga7664f5e184e9b41ac92e033f7b8d885d"></a>

```c
#define SHELL_ERROR SHELL_VT100_COLOR_RED
```

相关声明：[SHELL_ERROR](#ga7664f5e184e9b41ac92e033f7b8d885d)、[SHELL_VT100_COLOR_RED](#gga6dcf569be711db32286fb1ef2dcf36d2a6f6be6e431dc8e905c5734b4e9c32af4)。

用于shell_fprintf函数的红色文本（Red Text）。

<a id="r_ga1fd1671311b112f0c87ab2dafd801105"></a>

```c
#define shell_fprintf(sh, color, fmt, ...)
```

相关声明：[shell_fprintf](#ga1fd1671311b112f0c87ab2dafd801105)。

类似printf的函数，向Shell发送格式化数据流（Formatted Data Stream）。

<a id="r_ga9382959c41fe6850c2daa51306b3c5fd"></a>

```c
#define shell_info(_sh, _ft, ...)
```

相关声明：[shell_info](#ga9382959c41fe6850c2daa51306b3c5fd)。

向Shell打印信息消息（Info Message）。

<a id="r_ga2285d8085d3696bf1c568213d31dabc7"></a>

```c
#define shell_fprintf_info(_sh, _ft, ...)
```

相关声明：[shell_fprintf_info](#ga2285d8085d3696bf1c568213d31dabc7)。

向Shell打印信息消息（Info Message）。

<a id="r_ga3126019b2100d1ccb2d4dc5efb7d8228"></a>

```c
#define shell_print(_sh, _ft, ...)
```

相关声明：[shell_print](#ga3126019b2100d1ccb2d4dc5efb7d8228)。

向Shell打印普通消息（Normal Message）。

<a id="r_gafe3749d6ed0867052d74365c40a702fc"></a>

```c
#define shell_fprintf_normal(_sh, _ft, ...)
```

相关声明：[shell_fprintf_normal](#gafe3749d6ed0867052d74365c40a702fc)。

向Shell打印普通消息（Normal Message）。

<a id="r_ga3d886cfd7b4340b2e71a92bd7c4534d9"></a>

```c
#define shell_warn(_sh, _ft, ...)
```

相关声明：[shell_warn](#ga3d886cfd7b4340b2e71a92bd7c4534d9)。

向Shell打印警告消息（Warning Message）。

<a id="r_ga214fff4fc56f5a90c4063dad9c233f1b"></a>

```c
#define shell_fprintf_warn(_sh, _ft, ...)
```

相关声明：[shell_fprintf_warn](#ga214fff4fc56f5a90c4063dad9c233f1b)。

向Shell打印警告消息（Warning Message）。

<a id="r_ga408141c02209a9549cb9063f24ef3731"></a>

```c
#define shell_error(_sh, _ft, ...)
```

相关声明：[shell_error](#ga408141c02209a9549cb9063f24ef3731)。

向Shell打印错误消息（Error Message）。

<a id="r_gac32c42fb696c2198c73c2c73087cdfc3"></a>

```c
#define shell_fprintf_error(_sh, _ft, ...)
```

相关声明：[shell_fprintf_error](#gac32c42fb696c2198c73c2c73087cdfc3)。

向Shell打印错误消息（Error Message）。

<a id="r_ga3be3ecccd6ce1954883c5959c39c7927"></a>

```c
#define SHELL_CMD_HELP_PRINTED (1)
```

相关声明：[SHELL_CMD_HELP_PRINTED](#ga3be3ecccd6ce1954883c5959c39c7927)。

已打印命令帮助（Command Help）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 1.5\_类型定义（Typedefs）

<a id="r_gafc042f32bac2fdd4cbde9f943e29b008"></a>

```c
typedef void(* shell_dynamic_get) (size_t idx, struct shell_static_entry *entry)
```

相关声明：[shell_dynamic_get](#gafc042f32bac2fdd4cbde9f943e29b008)、[shell_static_entry](P008_Shell静态命令条目.md)。

Shell动态命令描述符（Dynamic Command Descriptor）。

<a id="r_gaa2b8cf8ac78b8355408ef94958ebdc70"></a>

```c
typedef bool(* shell_device_filter_t) (const struct device *dev)
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[shell_device_filter_t](#gaa2b8cf8ac78b8355408ef94958ebdc70)、[device](../device_reference/P002_设备对象结构.md)。

用于shell_device_filter的过滤回调类型（Filter Callback Type）。

<a id="r_ga331e7d19b9b0755486596f5ffc598338"></a>

```c
typedef int(* shell_cmd_handler) (const struct shell *sh, size_t argc, char **argv)
```

相关声明：[shell_cmd_handler](#ga331e7d19b9b0755486596f5ffc598338)、[shell](P004_Shell实例结构.md)。

Shell命令处理函数原型（Command Handler Prototype）。

<a id="r_ga182f247052041f1236d13726589885e2"></a>

```c
typedef int(* shell_dict_cmd_handler) (const struct shell *sh, size_t argc, char **argv, void *data)
```

相关声明：[shell_dict_cmd_handler](#ga182f247052041f1236d13726589885e2)、[shell](P004_Shell实例结构.md)。

Shell字典命令处理函数原型（Dictionary Command Handler Prototype）。

<a id="r_ga265807c2d8eba7b9ea633968627e085d"></a>

```c
typedef void(* shell_transport_handler_t) (enum shell_transport_evt evt, void *context)
```

相关声明：[shell_transport_handler_t](#ga265807c2d8eba7b9ea633968627e085d)。

Shell传输事件处理回调（Transport Event Handler Callback）。

<a id="r_ga0844a0ce151551d3ccf45d507e5bab25"></a>

```c
typedef void(* shell_uninit_cb_t) (const struct shell *sh, int res)
```

相关声明：[shell_uninit_cb_t](#ga0844a0ce151551d3ccf45d507e5bab25)、[shell](P004_Shell实例结构.md)。

Shell反初始化完成回调（Uninitialization Completion Callback）。

<a id="r_gacaddbcd6e84f377f39a5d69398996557"></a>

```c
typedef void(* shell_bypass_cb_t) (const struct shell *sh, uint8_t *data, size_t len, void *user_data)
```

相关声明：[shell_bypass_cb_t](#gacaddbcd6e84f377f39a5d69398996557)、[shell](P004_Shell实例结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

旁路回调（Bypass Callback）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 1.6\_枚举（Enumerations）

<a id="r_ga56bf30741f9ec7a6d94e5c18c2858948"></a>

```c
enum shell_flag { SHELL_FLAG_CRLF_DEFAULT = (1<<0) , SHELL_FLAG_OLF_CRLF = (1<<1) }
```

相关声明：[shell_flag](#ga56bf30741f9ec7a6d94e5c18c2858948)、[SHELL_FLAG_CRLF_DEFAULT](#gga56bf30741f9ec7a6d94e5c18c2858948a343ee559d6259111dbab529a283b23ab)、[SHELL_FLAG_OLF_CRLF](#gga56bf30741f9ec7a6d94e5c18c2858948ab6fec7b615b6de79e1d00d4117615446)。

设置Shell输出换行序列（Output Newline Sequence）的标志。

<a id="r_ga6dcf569be711db32286fb1ef2dcf36d2"></a>

```c
enum shell_vt100_color { SHELL_VT100_COLOR_BLACK , SHELL_VT100_COLOR_RED , SHELL_VT100_COLOR_GREEN , SHELL_VT100_COLOR_YELLOW , SHELL_VT100_COLOR_BLUE , SHELL_VT100_COLOR_MAGENTA , SHELL_VT100_COLOR_CYAN , SHELL_VT100_COLOR_WHITE , SHELL_VT100_COLOR_DEFAULT }
```

相关声明：[shell_vt100_color](#ga6dcf569be711db32286fb1ef2dcf36d2)、[SHELL_VT100_COLOR_BLACK](#gga6dcf569be711db32286fb1ef2dcf36d2a52be3094dd0400eba48c686b0b4e57c6)、[SHELL_VT100_COLOR_RED](#gga6dcf569be711db32286fb1ef2dcf36d2a6f6be6e431dc8e905c5734b4e9c32af4)、[SHELL_VT100_COLOR_GREEN](#gga6dcf569be711db32286fb1ef2dcf36d2ac6fce9bc89ceb0043697b26cca380c8a)、[SHELL_VT100_COLOR_YELLOW](#gga6dcf569be711db32286fb1ef2dcf36d2adb8fbc39eddceb95f523eed8d5c5bf7d)、[SHELL_VT100_COLOR_BLUE](#gga6dcf569be711db32286fb1ef2dcf36d2ace5b01755eec4567f0dc65e48143e33d)、[SHELL_VT100_COLOR_MAGENTA](#gga6dcf569be711db32286fb1ef2dcf36d2a85c738dbb19eccc90adba2e4a131140a)、[SHELL_VT100_COLOR_CYAN](#gga6dcf569be711db32286fb1ef2dcf36d2a618a6789463b1980f1086ee128c65972)、[SHELL_VT100_COLOR_WHITE](#gga6dcf569be711db32286fb1ef2dcf36d2a20523afc967f7f3bc0af645255b0b28c)、[SHELL_VT100_COLOR_DEFAULT](#gga6dcf569be711db32286fb1ef2dcf36d2a32de6063c44948beeb8501fed9b7d18e)。

Shell输出可用的文本颜色（Text Colors）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 1.7\_函数（Functions）

<a id="r_ga571db3aa3e024a09e82b117a74d6f248"></a>

```c
const struct device * shell_device_lookup (size_t idx, const char *prefix)
```

相关声明：[device](../device_reference/P002_设备对象结构.md)、[shell_device_lookup](#ga571db3aa3e024a09e82b117a74d6f248)。

按索引取得匹配的设备。（原文在matches后未给出匹配对象，参数说明见下文。）

<a id="r_ga8e83709f5e75d4cea51f42f41bb4e20f"></a>

```c
const struct device * shell_device_lookup_all (size_t idx, const char *prefix)
```

相关声明：[device](../device_reference/P002_设备对象结构.md)、[shell_device_lookup_all](#ga8e83709f5e75d4cea51f42f41bb4e20f)。

按索引取得匹配的设备。（原文在matches后未给出匹配对象，参数说明见下文。）

<a id="r_ga9f2994f2d6a55521a3e162a81299e4c3"></a>

```c
const struct device * shell_device_lookup_non_ready (size_t idx, const char *prefix)
```

相关声明：[device](../device_reference/P002_设备对象结构.md)、[shell_device_lookup_non_ready](#ga9f2994f2d6a55521a3e162a81299e4c3)。

按索引取得匹配的、未初始化设备。（原文在matches后未给出匹配对象，参数说明见下文。）

<a id="r_gae2a8e3d44a9bf5eb55be80833ac6eb5d"></a>

```c
const struct device * shell_device_filter (size_t idx, shell_device_filter_t filter)
```

相关声明：[device](../device_reference/P002_设备对象结构.md)、[shell_device_filter](#gae2a8e3d44a9bf5eb55be80833ac6eb5d)、[shell_device_filter_t](#gaa2b8cf8ac78b8355408ef94958ebdc70)。

根据索引与过滤器（Filter）取得设备。

<a id="r_ga7fb40045dc0a27c175e37a6c9cd84b53"></a>

```c
const struct device * shell_device_get_binding (const char *name)
```

相关声明：[device](../device_reference/P002_设备对象结构.md)、[shell_device_get_binding](#ga7fb40045dc0a27c175e37a6c9cd84b53)。

通过device::name字段或标签（Label）取得设备引用。

<a id="r_ga919147e222fe10ce14ab3c3a5c5a94e3"></a>

```c
const struct device * shell_device_get_binding_all (const char *name)
```

相关声明：[device](../device_reference/P002_设备对象结构.md)、[shell_device_get_binding_all](#ga919147e222fe10ce14ab3c3a5c5a94e3)。

通过device::name字段或标签（Label）取得设备引用。

<a id="r_ga061bf2530269ebf20d8e006dace5e33b"></a>

```c
static bool shell_help_is_structured (const char *help)
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[shell_help_is_structured](#ga061bf2530269ebf20d8e006dace5e33b)。

检查帮助字符串是否为结构化帮助（Structured Help）。

<a id="r_ga8764ff11603855a10419c48e46e8221c"></a>

```c
int shell_init (const struct shell *sh, const void *transport_config, struct shell_backend_config_flags cfg_flags, bool log_backend, uint32_t init_log_level)
```

相关声明：[shell_init](#ga8764ff11603855a10419c48e46e8221c)、[shell](P004_Shell实例结构.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[log_backend](../log_backend_reference/P004_日志后端结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

初始化传输层（Transport Layer）和Shell内部状态的函数。

<a id="r_ga07e76646c5065218464aa8ce78b75af3"></a>

```c
void shell_uninit (const struct shell *sh, shell_uninit_cb_t cb)
```

相关声明：[shell_uninit](#ga07e76646c5065218464aa8ce78b75af3)、[shell](P004_Shell实例结构.md)、[shell_uninit_cb_t](#ga0844a0ce151551d3ccf45d507e5bab25)。

反初始化传输层和Shell内部状态。

<a id="r_gad386d4e8077103e7976f25996fcc3132"></a>

```c
int shell_start (const struct shell *sh)
```

相关声明：[shell_start](#gad386d4e8077103e7976f25996fcc3132)、[shell](P004_Shell实例结构.md)。

启动Shell处理的函数。

<a id="r_gad27754d0beb31bc501f28f9ef26a362c"></a>

```c
int shell_stop (const struct shell *sh)
```

相关声明：[shell_stop](#gad27754d0beb31bc501f28f9ef26a362c)、[shell](P004_Shell实例结构.md)。

停止Shell处理的函数。

<a id="r_ga74a1c4edd803cad14c893fc9816e534f"></a>

```c
void shell_vfprintf (const struct shell *sh, enum shell_vt100_color color, const char *fmt, va_list args)
```

相关声明：[shell_vfprintf](#ga74a1c4edd803cad14c893fc9816e534f)、[shell](P004_Shell实例结构.md)、[shell_vt100_color](#ga6dcf569be711db32286fb1ef2dcf36d2)。

类似vprintf的函数，向Shell发送格式化数据流。

<a id="r_ga706aebd24cbdb7f14b9a324515414ecf"></a>

```c
void shell_cbpprintf (const struct shell *sh, enum shell_vt100_color color, void *package)
```

相关声明：[shell_cbpprintf](#ga706aebd24cbdb7f14b9a324515414ecf)、[shell](P004_Shell实例结构.md)、[shell_vt100_color](#ga6dcf569be711db32286fb1ef2dcf36d2)。

将cbprintf包格式化后以数据流形式发送到Shell的函数。

<a id="r_ga0b6e69b499c153ae8f7ba256d445f09d"></a>

```c
void shell_hexdump_line (const struct shell *sh, unsigned int offset, const uint8_t *data, size_t len)
```

相关声明：[shell_hexdump_line](#ga0b6e69b499c153ae8f7ba256d445f09d)、[shell](P004_Shell实例结构.md)、[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

以十六进制格式（Hexadecimal Format）打印一行数据。

<a id="r_gaeeba0b483974205c54e364d509badd42"></a>

```c
void shell_hexdump (const struct shell *sh, const uint8_t *data, size_t len)
```

相关声明：[shell_hexdump](#gaeeba0b483974205c54e364d509badd42)、[shell](P004_Shell实例结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

以十六进制格式打印数据。

<a id="r_ga7e66389d0faf15a2a7c31c68cdd9c36c"></a>

```c
void shell_process (const struct shell *sh)
```

相关声明：[shell_process](#ga7e66389d0faf15a2a7c31c68cdd9c36c)、[shell](P004_Shell实例结构.md)。

传输接口中有数据就绪时应执行的处理函数（Process Function）。

<a id="r_ga2113b7227b155755a7ab8a928f7ae499"></a>

```c
int shell_prompt_change (const struct shell *sh, const char *prompt)
```

相关声明：[shell_prompt_change](#ga2113b7227b155755a7ab8a928f7ae499)、[shell](P004_Shell实例结构.md)。

更改显示的Shell提示符（Prompt）。

<a id="r_ga9e4911ff2c3a07fa70711ddac83701d6"></a>

```c
static void shell_help (const struct shell *sh)
```

相关声明：[shell_help](#ga9e4911ff2c3a07fa70711ddac83701d6)、[shell](P004_Shell实例结构.md)。

打印当前命令的帮助。

<a id="r_gabfb6a1f1f53f90365de349348015311e"></a>

```c
int shell_execute_cmd (const struct shell *sh, const char *cmd)
```

相关声明：[shell_execute_cmd](#gabfb6a1f1f53f90365de349348015311e)、[shell](P004_Shell实例结构.md)、[cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)。

执行命令（Execute Command）。

<a id="r_ga768c606f2d50f24e9b607ba0a341686d"></a>

```c
int shell_set_root_cmd (const char *cmd)
```

相关声明：[shell_set_root_cmd](#ga768c606f2d50f24e9b607ba0a341686d)、[cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)。

为所有Shell实例设置根命令（Root Command）。

<a id="r_ga4d51d4dbb22bed5d040deabc7ab6dc9d"></a>

```c
void shell_set_bypass (const struct shell *sh, shell_bypass_cb_t bypass, void *user_data)
```

相关声明：[shell_set_bypass](#ga4d51d4dbb22bed5d040deabc7ab6dc9d)、[shell](P004_Shell实例结构.md)、[shell_bypass_cb_t](#gacaddbcd6e84f377f39a5d69398996557)。

设置旁路回调（Bypass Callback）。

<a id="r_ga79369ddfea2dc2cb5813c5eb5c67634a"></a>

```c
bool shell_ready (const struct shell *sh)
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[shell_ready](#ga79369ddfea2dc2cb5813c5eb5c67634a)、[shell](P004_Shell实例结构.md)。

取得Shell是否已就绪、能够执行命令的状态。

<a id="r_gaf1f41d8b6cd430357d593ab0fc5adfeb"></a>

```c
int shell_insert_mode_set (const struct shell *sh, bool val)
```

相关声明：[shell_insert_mode_set](#gaf1f41d8b6cd430357d593ab0fc5adfeb)、[shell](P004_Shell实例结构.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

允许应用控制文本插入模式（Insert Mode）。

<a id="r_ga7d5873456ba43ebd3cc86d25e3f4a72c"></a>

```c
int shell_use_colors_set (const struct shell *sh, bool val)
```

相关声明：[shell_use_colors_set](#ga7d5873456ba43ebd3cc86d25e3f4a72c)、[shell](P004_Shell实例结构.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

允许应用控制终端输出是否使用彩色语法（Colored Syntax）。

<a id="r_ga80ff4b3b4cc62e543fd510c14f55b42a"></a>

```c
int shell_use_vt100_set (const struct shell *sh, bool val)
```

相关声明：[shell_use_vt100_set](#ga80ff4b3b4cc62e543fd510c14f55b42a)、[shell](P004_Shell实例结构.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

允许应用控制终端是否使用VT100命令。

<a id="r_gad53881371bbaedfd3ef3ecf219706fd1"></a>

```c
int shell_echo_set (const struct shell *sh, bool val)
```

相关声明：[shell_echo_set](#gad53881371bbaedfd3ef3ecf219706fd1)、[shell](P004_Shell实例结构.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

允许应用控制是否回显用户输入（Echo）。

<a id="r_ga86fade2757d04c9220d5912a4ee540a0"></a>

```c
int shell_obscure_set (const struct shell *sh, bool obscure)
```

相关声明：[shell_obscure_set](#ga86fade2757d04c9220d5912a4ee540a0)、[shell](P004_Shell实例结构.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

允许应用控制是否用星号遮蔽用户输入（Obscure），可用于实现口令输入。

<a id="r_ga2df2997c4b04f3246c22f43b274a353b"></a>

```c
int shell_mode_delete_set (const struct shell *sh, bool val)
```

相关声明：[shell_mode_delete_set](#ga2df2997c4b04f3246c22f43b274a353b)、[shell](P004_Shell实例结构.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

允许应用控制Delete键执行退格（Backspace）还是删除（Delete）。

<a id="r_ga54dc053c92641bc9b9736bc2d61140f7"></a>

```c
int shell_get_return_value (const struct shell *sh)
```

相关声明：[shell_get_return_value](#ga54dc053c92641bc9b9736bc2d61140f7)、[shell](P004_Shell实例结构.md)。

取得最近一次执行的Shell命令的返回值。

<a id="r_ga313068db9c3b9972ca4129085d8605d5"></a>

```c
void shell_readline_prompt_set (const struct shell *sh, const char *prompt)
```

相关声明：[shell_readline_prompt_set](#ga313068db9c3b9972ca4129085d8605d5)、[shell](P004_Shell实例结构.md)。

为下一次shell_readline调用设置提示字符串（Prompt String）。

<a id="r_ga05b2eb80f3484216ef2e1d4bf9492453"></a>

```c
int shell_readline (const struct shell *sh, uint8_t *buf, size_t len, k_timeout_t timeout)
```

相关声明：[shell_readline](#ga05b2eb80f3484216ef2e1d4bf9492453)、[shell](P004_Shell实例结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

从Shell读取一行输入。

<a id="r_ga2a3fc802d8a4d13e49024ee5546d62a6"></a>

```c
long shell_strtol (const char *str, int base, int *err)
```

相关声明：[shell_strtol](#ga2a3fc802d8a4d13e49024ee5546d62a6)。

将字符串转换为long，并检查错误。

<a id="r_gac7928525a22e053d1dea44995c8198b9"></a>

```c
unsigned long shell_strtoul (const char *str, int base, int *err)
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[shell_strtoul](#gac7928525a22e053d1dea44995c8198b9)。

将字符串转换为unsigned long，并检查错误。

<a id="r_ga635c05cc9a2e84b6438402334587d537"></a>

```c
unsigned long long shell_strtoull (const char *str, int base, int *err)
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[shell_strtoull](#ga635c05cc9a2e84b6438402334587d537)。

将字符串转换为unsigned long long，并检查错误。

<a id="r_gaabc3fbdfdc2c3cbd4cd41dc97309aea4"></a>

```c
bool shell_strtobool (const char *str, int base, int *err)
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[shell_strtobool](#gaabc3fbdfdc2c3cbd4cd41dc97309aea4)。

将字符串转换为布尔值（Boolean），并检查错误。

## 1.8\_详细说明（Detailed Documentation）

<a id="ga24ade9db85af9a8776a45ba0084f4cca"></a>

### `SHELL_CMD`

```c
#define SHELL_CMD ( _syntax, _subcmd, _help, _handler )
```

```c
#include <zephyr/shell/shell.h>
```

展开值（Value）：

```c
SHELL_CMD_ARG(_syntax, _subcmd, _help, _handler, 0, 0)
```

初始化Shell命令。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] _syntax` | 命令语法名称（Command Syntax），例如history。 |
| `[in] _subcmd` | 子命令数组（Subcommands Array）的指针。 |
| `[in] _help` | 命令帮助字符串（Help String）的指针。 |
| `[in] _handler` | 处理函数（Handler）的指针。 |

<a id="gad762c496a2ced65069b6d1d02a4d925c"></a>

### `SHELL_CMD_ARG`

```c
#define SHELL_CMD_ARG ( syntax, subcmd, help, handler, mand, opt )
```

```c
#include <zephyr/shell/shell.h>
```

展开值（Value）：

```c
SHELL_EXPR_CMD_ARG(1, syntax, subcmd, help, handler, mand, opt, 0, 0)
```

初始化带参数的Shell命令。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] syntax` | 命令语法名称（Command Syntax），例如history。 |
| `[in] subcmd` | 子命令数组（Subcommands Array）的指针。 |
| `[in] help` | 命令帮助字符串的指针；结构化帮助使用SHELL_HELP。 |
| `[in] handler` | 处理函数（Handler）的指针。 |
| `[in] mand` | 必需参数（Mandatory Arguments）的数量，包含命令名称。 |
| `[in] opt` | 可选参数（Optional Arguments）的数量。 |

说明（Note）：以错误的参数数量调用命令时，Shell会打印错误消息，不会调用命令处理函数。

<a id="gae8a8bbcbb842027c02a319b3fb976a3d"></a>

### `SHELL_CMD_ARG_REGISTER`

```c
#define SHELL_CMD_ARG_REGISTER ( syntax, subcmd, help, handler, mandatory, optional )
```

```c
#include <zephyr/shell/shell.h>
```

展开值（Value）：

```c
static const struct shell_static_entry UTIL_CAT(_shell_, syntax) = \
SHELL_CMD_ARG(syntax, subcmd, help, handler, mandatory, optional); \
static const TYPE_SECTION_ITERABLE(union shell_cmd_entry,          \
        UTIL_CAT(shell_cmd_, syntax), shell_root_cmds,             \
        UTIL_CAT(shell_cmd_, syntax)                               \
) = {                                                              \
        .entry = &UTIL_CAT(_shell_, syntax)                        \
}
```

定义并添加带必需参数数量约束的根命令（Root Command，第0级）的宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] syntax` | 命令语法名称（Command Syntax），例如history。 |
| `[in] subcmd` | 子命令数组（Subcommands Array）的指针。 |
| `[in] help` | 命令帮助字符串的指针；结构化帮助使用SHELL_HELP。 |
| `[in] handler` | 处理函数（Handler）的指针。 |
| `[in] mandatory` | 必需参数（Mandatory Arguments）的数量，包含命令名称。 |
| `[in] optional` | 可选参数（Optional Arguments）的数量。 |

说明（Note）：每个根命令必须具有唯一的语法名称。以错误的参数数量调用命令时，Shell会打印错误消息，不会调用命令处理函数。

<a id="ga1e66e9bc319d9c028e404f05022f8a6e"></a>

### `SHELL_CMD_FLAG_REMOTE_ROOT`

```c
#define SHELL_CMD_FLAG_REMOTE_ROOT BIT(0)
```

```c
#include <zephyr/shell/shell.h>
```

表示远端根命令（Root Remote Command）的标志。

<a id="gae3da8b6143ccbf46a08806296cd0bc9e"></a>

### `SHELL_CMD_FLAG_REMOTE_SUBCMD`

```c
#define SHELL_CMD_FLAG_REMOTE_SUBCMD BIT(1)
```

```c
#include <zephyr/shell/shell.h>
```

表示远端子命令（Remote Subcommand）的标志。

<a id="ga3be3ecccd6ce1954883c5959c39c7927"></a>

### `SHELL_CMD_HELP_PRINTED`

```c
#define SHELL_CMD_HELP_PRINTED (1)
```

```c
#include <zephyr/shell/shell.h>
```

已打印命令帮助（Command Help）。

<a id="ga06060b98eb505300a3dcc8f922a8e7ab"></a>

### `SHELL_CMD_REGISTER`

```c
#define SHELL_CMD_REGISTER ( syntax, subcmd, help, handler )
```

```c
#include <zephyr/shell/shell.h>
```

展开值（Value）：

```c
SHELL_CMD_ARG_REGISTER(syntax, subcmd, help, handler, 0, 0)
```

定义并添加带参数根命令（Root Command，第0级）的宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] syntax` | 命令语法名称（Command Syntax），例如history。 |
| `[in] subcmd` | 子命令数组（Subcommands Array）的指针。 |
| `[in] help` | 命令帮助字符串的指针；结构化帮助使用SHELL_HELP。 |
| `[in] handler` | 处理函数（Handler）的指针。 |

说明（Note）：所有根命令必须使用不同的名称。

<a id="ga6e27d86443067df4792623f1a04d1ee1"></a>

### `SHELL_COND_CMD`

```c
#define SHELL_COND_CMD ( _flag, _syntax, _subcmd, _help, _handler )
```

```c
#include <zephyr/shell/shell.h>
```

展开值（Value）：

```c
SHELL_COND_CMD_ARG(_flag, _syntax, _subcmd, _help, _handler, 0, 0)
```

按条件初始化Shell命令。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] _flag` | 编译期标志（Compile-time Flag）。仅当标志存在且等于1时，命令才存在。 |
| `[in] _syntax` | 命令语法名称（Command Syntax），例如history。 |
| `[in] _subcmd` | 子命令数组（Subcommands Array）的指针。 |
| `[in] _help` | 命令帮助字符串（Help String）的指针。 |
| `[in] _handler` | 处理函数（Handler）的指针。 |

另见（See Also）：SHELL_COND_CMD_ARG。

<a id="ga68229f89484c3459d77cebb450ee1f24"></a>

### `SHELL_COND_CMD_ARG`

```c
#define SHELL_COND_CMD_ARG ( flag, syntax, subcmd, help, handler, mand, opt )
```

```c
#include <zephyr/shell/shell.h>
```

展开值（Value）：

```c
SHELL_EXPR_CMD_ARG(IS_ENABLED(flag), syntax, subcmd, help, \
                  handler, mand, opt, 0, 0)
```

按条件初始化带参数的Shell命令。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] flag` | 编译期标志（Compile-time Flag）。仅当标志存在且等于1时，命令才存在。 |
| `[in] syntax` | 命令语法名称（Command Syntax），例如history。 |
| `[in] subcmd` | 子命令数组（Subcommands Array）的指针。 |
| `[in] help` | 命令帮助字符串的指针；结构化帮助使用SHELL_HELP。 |
| `[in] handler` | 处理函数（Handler）的指针。 |
| `[in] mand` | 必需参数（Mandatory Arguments）的数量，包含命令名称。 |
| `[in] opt` | 可选参数（Optional Arguments）的数量。 |

另见（See Also）：SHELL_CMD_ARG。根据标志创建有效条目或Shell会忽略的空命令（Empty Command）。它可替代包围命令注册和处理函数的#ifdef。即使命令被禁用，空结构仍存在于Flash中，但子命令和处理函数会移除。宏内部会处理标志未定义的情况，因此应直接传入标志，不加包装，例如SHELL_COND_CMD_ARG(CONFIG_FOO, ...)。

<a id="ga6a3ed4ea9051ac138d22cc39134fb2e5"></a>

### `SHELL_COND_CMD_ARG_REGISTER`

```c
#define SHELL_COND_CMD_ARG_REGISTER ( flag, syntax, subcmd, help, handler, mandatory, optional )
```

```c
#include <zephyr/shell/shell.h>
```

展开值（Value）：

```c
COND_CODE_1(\
        flag, \
        (\
        SHELL_CMD_ARG_REGISTER(syntax, subcmd, help, handler, \
                                mandatory, optional) \
        ), \
        (\
        static shell_cmd_handler dummy_##syntax##_handler __unused = \
                                                        handler;\
        static const union shell_cmd_entry *dummy_subcmd_##syntax \
                __unused = subcmd\
        ) \
)
```

定义并添加带必需参数数量约束的条件根命令（Conditional Root Command，第0级）的宏。

此宏可创建按条件存在的命令，替代包围命令注册与处理函数的#ifdef。命令禁用时，其处理函数和子命令会从应用中移除。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] flag` | 编译期标志（Compile-time Flag）。仅当标志存在且等于1时，命令才存在。 |
| `[in] syntax` | 命令语法名称（Command Syntax），例如history。 |
| `[in] subcmd` | 子命令数组（Subcommands Array）的指针。 |
| `[in] help` | 命令帮助字符串的指针；结构化帮助使用SHELL_HELP。 |
| `[in] handler` | 处理函数（Handler）的指针。 |
| `[in] mandatory` | 必需参数（Mandatory Arguments）的数量，包含命令名称。 |
| `[in] optional` | 可选参数（Optional Arguments）的数量。 |

另见（See Also）：详细说明参见SHELL_CMD_ARG_REGISTER。

<a id="ga62782121ece6af076407c94935ec94e4"></a>

### `SHELL_COND_CMD_REGISTER`

```c
#define SHELL_COND_CMD_REGISTER ( flag, syntax, subcmd, help, handler )
```

```c
#include <zephyr/shell/shell.h>
```

展开值（Value）：

```c
SHELL_COND_CMD_ARG_REGISTER(flag, syntax, subcmd, help, handler, 0, 0)
```

定义并添加带参数条件根命令（Conditional Root Command，第0级）的宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] flag` | 编译期标志（Compile-time Flag）。仅当标志存在且等于1时，命令才存在。 |
| `[in] syntax` | 命令语法名称（Command Syntax），例如history。 |
| `[in] subcmd` | 子命令数组（Subcommands Array）的指针。 |
| `[in] help` | 命令帮助字符串的指针；结构化帮助使用SHELL_HELP。 |
| `[in] handler` | 处理函数（Handler）的指针。 |

另见（See Also）：SHELL_COND_CMD_ARG_REGISTER。

<a id="ga158405143b49e4888cb135fec83ad22c"></a>

### `SHELL_DEFINE`

```c
#define SHELL_DEFINE ( _name, _prompt, _transport_iface, _log_queue_size, _log_timeout, _shell_flag )
```

```c
#include <zephyr/shell/shell.h>
```

展开值（Value）：

```c
static uint8_t _name##_out_buffer[CONFIG_SHELL_PRINTF_BUFF_SIZE];                          \
Z_SHELL_LOG_BACKEND_DEFINE(_name, _name##_out_buffer, CONFIG_SHELL_PRINTF_BUFF_SIZE,       \
                           _log_queue_size, _log_timeout);                                 \
Z_SHELL_DEFINE(_name, _prompt, _transport_iface, _name##_out_buffer,                       \
               Z_SHELL_LOG_BACKEND_PTR(_name), _shell_flag)
```

定义Shell实例（Shell Instance）的宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] _name` | 实例名称（Instance Name）。 |
| `[in] _prompt` | Shell默认提示字符串（Default Prompt String）。 |
| `[in] _transport_iface` | 传输接口（Transport Interface）的指针。 |
| `[in] _log_queue_size` | 日志处理队列大小（Logger Processing Queue Size）。 |
| `[in] _log_timeout` | 日志队列满时，日志线程等待的超时时间，单位为毫秒。队列已满时，日志线程会先阻塞指定时长，再丢弃日志消息。 |
| `[in] _shell_flag` | Shell输出换行序列（Output Newline Sequence）。 |

<a id="gafa6d91c36c36eb68d3f241ed0c7e7131"></a>

### `SHELL_DYNAMIC_CMD_CREATE`

```c
#define SHELL_DYNAMIC_CMD_CREATE ( name, get )
```

```c
#include <zephyr/shell/shell.h>
```

展开值（Value）：

```c
static const TYPE_SECTION_ITERABLE(union shell_cmd_entry, name,         \
        shell_dynamic_subcmds, name) =                                  \
{                                                                       \
        .dynamic_get = get                                              \
}
```

创建动态条目（Dynamic Entry）的宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] name` | 动态条目的名称（Dynamic Entry Name）。 |
| `[in] get` | 返回动态命令数组的函数指针。 |

<a id="ga7664f5e184e9b41ac92e033f7b8d885d"></a>

### `SHELL_ERROR`

```c
#define SHELL_ERROR SHELL_VT100_COLOR_RED
```

```c
#include <zephyr/shell/shell.h>
```

用于shell_fprintf函数的红色文本（Red Text）。

<a id="ga408141c02209a9549cb9063f24ef3731"></a>

### `shell_error`

```c
#define shell_error ( _sh, _ft, ... )
```

```c
#include <zephyr/shell/shell.h>
```

展开值（Value）：

```c
shell_fprintf_error(_sh, _ft "\n", ##__VA_ARGS__)
```

向Shell打印错误消息（Error Message）。

消息以换行字符结束。参见shell_fprintf。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] _sh` | Shell实例指针。 |
| `[in] _ft` | 格式字符串（Format String）。 |
| `[in] ...` | 待打印参数列表。 |

<a id="ga59a835edbd7db3acdcb204248c0cf5fd"></a>

### `SHELL_EXPR_CMD`

```c
#define SHELL_EXPR_CMD ( _expr, _syntax, _subcmd, _help, _handler )
```

```c
#include <zephyr/shell/shell.h>
```

展开值（Value）：

```c
SHELL_EXPR_CMD_ARG(_expr, _syntax, _subcmd, _help, _handler, 0, 0, 0, 0)
```

编译期表达式结果非零时初始化Shell命令。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] _expr` | 编译期表达式（Compile-time Expression）。仅当表达式非零时，命令才存在。 |
| `[in] _syntax` | 命令语法名称（Command Syntax），例如history。 |
| `[in] _subcmd` | 子命令数组（Subcommands Array）的指针。 |
| `[in] _help` | 命令帮助字符串（Help String）的指针。 |
| `[in] _handler` | 处理函数（Handler）的指针。 |

另见（See Also）：SHELL_EXPR_CMD_ARG。

<a id="ga18657f55b8fc37a84660f040a89186bf"></a>

### `SHELL_EXPR_CMD_ARG`

```c
#define SHELL_EXPR_CMD_ARG ( _expr, _syntax, _subcmd, _help, _handler, _mand, _opt, _remote_cmd, _remote_id )
```

```c
#include <zephyr/shell/shell.h>
```

展开值（Value）：

```c
{ \
        .syntax = (_expr) ? (const char *)STRINGIFY(_syntax) : "", \
        .help  = (_expr) ? (const char *)_help : NULL, \
        .subcmd = (const union shell_cmd_entry *)((_expr) ? \
                        _subcmd : NULL), \
        .handler = (shell_cmd_handler)((_expr) ? _handler : NULL), \
        .args = { .mandatory = _mand, .optional = _opt, \
                .remote_cmd = _remote_cmd, .remote_id = _remote_id } \
}
```

编译期表达式结果非零时，初始化带参数的条件Shell命令。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] _expr` | 表达式（Expression）。 |
| `[in] _syntax` | 命令语法名称（Command Syntax），例如history。 |
| `[in] _subcmd` | 子命令数组（Subcommands Array）的指针。 |
| `[in] _help` | 命令帮助字符串（Help String）的指针。 |
| `[in] _handler` | 处理函数（Handler）的指针。 |
| `[in] _mand` | 必需参数（Mandatory Arguments）的数量，包含命令名称。 |
| `[in] _opt` | 可选参数（Optional Arguments）的数量。 |
| `[in] _remote_cmd` | 远端Shell命令类型（Remote Command Type）；远端Shell对应非零值。 |
| `[in] _remote_id` | 远端连接编号（Remote Connection ID）；仅在remote_cmd非零时有效。 |

另见（See Also）：SHELL_CMD_ARG。根据表达式创建有效条目或Shell会忽略的空命令。当条件并非单个配置标志时，应使用此宏而不是SHELL_COND_CMD_ARG，例如SHELL_EXPR_CMD_ARG(IS_ENABLED(CONFIG_FOO) && IS_ENABLED(CONFIG_FOO_SETTING_1), ...)。

<a id="ga1fd1671311b112f0c87ab2dafd801105"></a>

### `shell_fprintf`

```c
#define shell_fprintf ( sh, color, fmt, ... )
```

```c
#include <zephyr/shell/shell.h>
```

展开值（Value）：

```c
COND_CODE_1(IS_ENABLED(CONFIG_SHELL_REMOTE_CLI), \
        (SHELL_REMOTE_CLI_FPRINTF(sh, color, fmt, ##__VA_ARGS__)), \
        (shell_fprintf_impl(sh, color, fmt, ##__VA_ARGS__)))
```

类似printf的函数，向Shell发送格式化数据流（Formatted Data Stream）。

可从命令处理函数或线程调用此函数，但不能从中断上下文（Interrupt Context）调用。启用CONFIG_SHELL_REMOTE_CLI时，输出会透明地路由到远端Shell。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] sh` | Shell实例指针。 |
| `[in] color` | 打印文本的颜色（Printed Text Color）。 |
| `[in] fmt` | 格式字符串（Format String）。 |
| `[in] ...` | 待打印参数列表。 |

<a id="gac32c42fb696c2198c73c2c73087cdfc3"></a>

### `shell_fprintf_error`

```c
#define shell_fprintf_error ( _sh, _ft, ... )
```

```c
#include <zephyr/shell/shell.h>
```

展开值（Value）：

```c
shell_fprintf(_sh, SHELL_ERROR, _ft, ##__VA_ARGS__)
```

向Shell打印错误消息（Error Message）。

参见shell_fprintf。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] _sh` | Shell实例指针。 |
| `[in] _ft` | 格式字符串（Format String）。 |
| `[in] ...` | 待打印参数列表。 |

<a id="ga2285d8085d3696bf1c568213d31dabc7"></a>

### `shell_fprintf_info`

```c
#define shell_fprintf_info ( _sh, _ft, ... )
```

```c
#include <zephyr/shell/shell.h>
```

展开值（Value）：

```c
shell_fprintf(_sh, SHELL_INFO, _ft, ##__VA_ARGS__)
```

向Shell打印信息消息（Info Message）。

参见shell_fprintf。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] _sh` | Shell实例指针。 |
| `[in] _ft` | 格式字符串（Format String）。 |
| `[in] ...` | 待打印参数列表。 |

<a id="gafe3749d6ed0867052d74365c40a702fc"></a>

### `shell_fprintf_normal`

```c
#define shell_fprintf_normal ( _sh, _ft, ... )
```

```c
#include <zephyr/shell/shell.h>
```

展开值（Value）：

```c
shell_fprintf(_sh, SHELL_NORMAL, _ft, ##__VA_ARGS__)
```

向Shell打印普通消息（Normal Message）。

参见shell_fprintf。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] _sh` | Shell实例指针。 |
| `[in] _ft` | 格式字符串（Format String）。 |
| `[in] ...` | 待打印参数列表。 |

<a id="ga214fff4fc56f5a90c4063dad9c233f1b"></a>

### `shell_fprintf_warn`

```c
#define shell_fprintf_warn ( _sh, _ft, ... )
```

```c
#include <zephyr/shell/shell.h>
```

展开值（Value）：

```c
shell_fprintf(_sh, SHELL_WARNING, _ft, ##__VA_ARGS__)
```

向Shell打印警告消息（Warning Message）。

参见shell_fprintf。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] _sh` | Shell实例指针。 |
| `[in] _ft` | 格式字符串（Format String）。 |
| `[in] ...` | 待打印参数列表。 |

<a id="gacf66d1ef4c3ae7d18a5f0668c667ed77"></a>

### `SHELL_HELP`

```c
#define SHELL_HELP ( _description, _usage )
```

```c
#include <zephyr/shell/shell.h>
```

展开值（Value）：

```c
((const char *)&(const struct shell_cmd_help){                                             \
        .magic = SHELL_STRUCTURED_HELP_MAGIC,                                              \
        .description = (_description),                                                     \
        .usage = (_usage),                                                                 \
})
```

内联创建结构化帮助（Structured Help）的辅助宏。

此宏允许将结构化帮助（Structured Help）直接传给现有Shell宏。

示例（Example）：

原始示例（Example）：

```c
#define MY_CMD_HELP SHELL_HELP("Do stuff", "<device> <arg1> [<arg2>]")
SHELL_CMD_REGISTER(my_cmd, NULL, MY_CMD_HELP, &my_cmd_handler, 1, 1);
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] _description` | 命令描述（Command Description），可以是多行字符串。第一行应以一句话描述命令，其余行可提供补充细节。 |
| `[in] _usage` | 命令用法字符串（Command Usage String），可以有多行。第一行应说明不含命令名称的命令语法。其余行可提供补充细节，例如各参数的含义、允许值等。 |

<a id="gaac0ea96fbb5885432dca93174c9ad4e6"></a>

### `SHELL_INFO`

```c
#define SHELL_INFO SHELL_VT100_COLOR_GREEN
```

```c
#include <zephyr/shell/shell.h>
```

用于shell_fprintf函数的绿色文本（Green Text）。

<a id="ga9382959c41fe6850c2daa51306b3c5fd"></a>

### `shell_info`

```c
#define shell_info ( _sh, _ft, ... )
```

```c
#include <zephyr/shell/shell.h>
```

展开值（Value）：

```c
shell_fprintf(_sh, SHELL_INFO, _ft "\n", ##__VA_ARGS__)
```

向Shell打印信息消息（Info Message）。

消息以换行字符结束。参见shell_fprintf。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] _sh` | Shell实例指针。 |
| `[in] _ft` | 格式字符串（Format String）。 |
| `[in] ...` | 待打印参数列表。 |

<a id="ga4c3a7db0c2bdbf36bbf72302a04bb44d"></a>

### `SHELL_NORMAL`

```c
#define SHELL_NORMAL SHELL_VT100_COLOR_DEFAULT
```

```c
#include <zephyr/shell/shell.h>
```

用于shell_fprintf函数的终端默认文本颜色（Default Text Color）。

<a id="ga0e2b3ac54184ae15f13e2024df1ac69b"></a>

### `SHELL_OPT_ARG_CHECK_SKIP`

```c
#define SHELL_OPT_ARG_CHECK_SKIP (0xFF)
```

```c
#include <zephyr/shell/shell.h>
```

表示可选参数数量不受限制的标志。

<a id="gaba166d98da7258a2a50abc94c1b744c8"></a>

### `SHELL_OPT_ARG_MAX`

```c
#define SHELL_OPT_ARG_MAX (0xFD)
```

```c
#include <zephyr/shell/shell.h>
```

表示可校验的最大可选参数数量的标志。

<a id="ga2b64d0c6e086ea227e85fe50312896f7"></a>

### `SHELL_OPT_ARG_RAW`

```c
#define SHELL_OPT_ARG_RAW (0xFE)
```

```c
#include <zephyr/shell/shell.h>
```

表示将所有可选参数作为一个未经格式处理的参数（Unformatted Argument）的标志。

默认情况下，Shell解析所有参数，将空格视为参数分隔符；引号内的空格除外，且这时引号会移除。如果命令依赖未经格式处理的参数，应在命令定义中用此标志替代可选参数数量，表示只解析必需参数，并将剩余命令文本作为原始字符串（Raw String）传入。

<a id="gacc7c6e7b1fc65cc350353cc166da528b"></a>

### `SHELL_OPTION`

```c
#define SHELL_OPTION SHELL_VT100_COLOR_CYAN
```

```c
#include <zephyr/shell/shell.h>
```

用于shell_fprintf函数的青色文本（Cyan Text）。

<a id="ga3126019b2100d1ccb2d4dc5efb7d8228"></a>

### `shell_print`

```c
#define shell_print ( _sh, _ft, ... )
```

```c
#include <zephyr/shell/shell.h>
```

展开值（Value）：

```c
shell_fprintf_normal(_sh, _ft "\n", ##__VA_ARGS__)
```

向Shell打印普通消息（Normal Message）。

消息以换行字符结束。参见shell_fprintf。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] _sh` | Shell实例指针。 |
| `[in] _ft` | 格式字符串（Format String）。 |
| `[in] ...` | 待打印参数列表。 |

<a id="gacb2d1a969368efdbeec704ee6e962dee"></a>

### `SHELL_STATIC_SUBCMD_SET_CREATE`

```c
#define SHELL_STATIC_SUBCMD_SET_CREATE ( name, ... )
```

```c
#include <zephyr/shell/shell.h>
```

展开值（Value）：

```c
static const struct shell_static_entry shell_##name[] = {       \
        __VA_ARGS__                                             \
};                                                              \
static const union shell_cmd_entry name = {                     \
        .entry = shell_##name                                   \
}
```

创建子命令集合（Subcommand Set）的宏。

必须在所有函数体之外使用。

用法示例（Example Usage）：

原始示例（Example）：

```c
SHELL_STATIC_SUBCMD_SET_CREATE(
   foo,
   SHELL_CMD(abc, ...),
   SHELL_CMD(def, ...),
   SHELL_SUBCMD_SET_END
)
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] name` | 子命令集合名称（Subcommand Set Name）。 |
| `[in] ...` | 使用SHELL_CMD_ARG或SHELL_CMD创建的命令列表。 |

<a id="ga85b0afcacd3831bf5c724590765e035f"></a>

### `SHELL_SUBCMD_ADD`

```c
#define SHELL_SUBCMD_ADD ( _parent, _syntax, _subcmd, _help, _handler, _mand, _opt )
```

```c
#include <zephyr/shell/shell.h>
```

展开值（Value）：

```c
SHELL_SUBCMD_COND_ADD(1, _parent, _syntax, _subcmd, _help, _handler, _mand, _opt)
```

向子命令集合添加命令。

向使用SHELL_SUBCMD_SET_CREATE创建的集合添加命令。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] _parent` | 父命令序列（Parent Command Sequence），放在括号内并用逗号分隔。 |
| `[in] _syntax` | 命令语法名称（Command Syntax），例如history。 |
| `[in] _subcmd` | 子命令数组（Subcommands Array）的指针。 |
| `[in] _help` | 命令帮助字符串（Help String）的指针。 |
| `[in] _handler` | 处理函数（Handler）的指针。 |
| `[in] _mand` | 必需参数（Mandatory Arguments）的数量，包含命令名称。 |
| `[in] _opt` | 可选参数（Optional Arguments）的数量。 |

<a id="gab1b643efbaee748be0256e904642e310"></a>

### `SHELL_SUBCMD_COND_ADD`

```c
#define SHELL_SUBCMD_COND_ADD ( _flag, _parent, _syntax, _subcmd, _help, _handler, _mand, _opt )
```

```c
#include <zephyr/shell/shell.h>
```

展开值（Value）：

```c
COND_CODE_1(_flag, \
        (static const TYPE_SECTION_ITERABLE(struct shell_static_entry, \
                                Z_SHELL_SUBCMD_NAME(__DEBRACKET _parent, _syntax), \
                                shell_subcmds, \
                                Z_SHELL_SUBCMD_ADD_SECTION_TAG(_parent, _syntax)) = \
                SHELL_EXPR_CMD_ARG(1, _syntax, _subcmd, _help, \
                                   _handler, _mand, _opt, 0, 0)\
        ), \
        (static shell_cmd_handler dummy_handler_##_syntax __unused = _handler;\
         static const union shell_cmd_entry dummy_subcmd_##_syntax __unused = { \
                .entry = (const struct shell_static_entry *)_subcmd\
         } \
        ) \
)
```

按条件向子命令集合添加命令。

向使用SHELL_SUBCMD_SET_CREATE创建的集合添加命令。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] _flag` | 编译期标志（Compile-time Flag）。仅当标志存在且等于1时，命令才存在。 |
| `[in] _parent` | 父命令序列（Parent Command Sequence），放在括号内并用逗号分隔。 |
| `[in] _syntax` | 命令语法名称（Command Syntax），例如history。 |
| `[in] _subcmd` | 子命令数组（Subcommands Array）的指针。 |
| `[in] _help` | 命令帮助字符串（Help String）的指针。 |
| `[in] _handler` | 处理函数（Handler）的指针。 |
| `[in] _mand` | 必需参数（Mandatory Arguments）的数量，包含命令名称。 |
| `[in] _opt` | 可选参数（Optional Arguments）的数量。 |

说明（Note）：段名称（Section Name）由父命令数量、所有父命令的名称和自身语法名称拼接形成。加入父命令数量是为了保证段前缀唯一；否则(foo)和(foo, cmd1)的子命令会混在一起。

<a id="ga401e19cf8ec8601b8a96fe8e95a2b4d2"></a>

### `SHELL_SUBCMD_DICT_SET_CREATE`

```c
#define SHELL_SUBCMD_DICT_SET_CREATE ( _name, _handler, ... )
```

```c
#include <zephyr/shell/shell.h>
```

展开值（Value）：

```c
FOR_EACH_FIXED_ARG(Z_SHELL_CMD_DICT_HANDLER_CREATE, (),         \
                   _handler, __VA_ARGS__)                       \
SHELL_STATIC_SUBCMD_SET_CREATE(_name,                           \
        FOR_EACH_FIXED_ARG(SHELL_CMD_DICT_CREATE, (,), _handler, __VA_ARGS__),  \
        SHELL_SUBCMD_SET_END                                    \
)
```

初始化Shell字典命令（Dictionary Commands）。

这是特殊的静态命令（Static Commands）。当命令处理函数需要使用“字符串与对应数据”的配对时，可以使用字典命令（Dictionary Commands）。字符串通常是对数据的文字描述；将其作为命令语法名称后，Shell可提示该字符串，并用对应数据处理命令。

用法示例（Example Usage）：

原始示例（Example）：

```c
static int my_handler(const struct shell *sh,
                 size_t argc, char **argv, void *data)
{
   int val = (int)data;

   shell_print(sh, "(syntax, value) : (%s, %d)", argv[0], val);
   return 0;
}

SHELL_SUBCMD_DICT_SET_CREATE(sub_dict_cmds, my_handler,
   (value_0, 0, "value 0"), (value_1, 1, "value 1"),
   (value_2, 2, "value 2"), (value_3, 3, "value 3")
);
SHELL_CMD_REGISTER(dictionary, &sub_dict_cmds, NULL, NULL);
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] _name` | 字典子命令集合（Dictionary Subcommand Set）的名称。 |
| `[in] _handler` | 所有字典命令共用的处理函数。 |

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] ...` | 字典三元组（Dictionary Triplets）：(command_syntax, value, helper)。value会作为用户数据传给_handler。 |

另见（See Also）：shell_dict_cmd_handler。

<a id="ga1e314886b70ee2e7e0763cd945a1a988"></a>

### `SHELL_SUBCMD_SET_CREATE`

```c
#define SHELL_SUBCMD_SET_CREATE ( _name, _parent )
```

```c
#include <zephyr/shell/shell.h>
```

展开值（Value）：

```c
static const TYPE_SECTION_ITERABLE(struct shell_static_entry, _name, shell_subcmds, \
                                  Z_SHELL_SUBCMD_SET_SECTION_TAG(_parent))
```

创建子命令集合（Subcommand Set）。

使用SHELL_SUBCMD_ADD和SHELL_SUBCMD_COND_ADD向此集合添加命令。命令可以来自多个文件。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] _name` | 集合名称。在父命令中通过_name引用此集合。 |
| `[in] _parent` | 用括号包围、逗号分隔的父命令集合；例如根命令foo_cmd的子命令使用(foo_cmd)。 |

<a id="ga4f7a3432f76541eb226a426507e10174"></a>

### `SHELL_SUBCMD_SET_END`

```c
#define SHELL_SUBCMD_SET_END {0}
```

```c
#include <zephyr/shell/shell.h>
```

定义子命令集合结束标记（Ending Subcommands Set）。

<a id="ga3d886cfd7b4340b2e71a92bd7c4534d9"></a>

### `shell_warn`

```c
#define shell_warn ( _sh, _ft, ... )
```

```c
#include <zephyr/shell/shell.h>
```

展开值（Value）：

```c
shell_fprintf_warn(_sh, _ft "\n", ##__VA_ARGS__)
```

向Shell打印警告消息（Warning Message）。

消息以换行字符结束。参见shell_fprintf。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] _sh` | Shell实例指针。 |
| `[in] _ft` | 格式字符串（Format String）。 |
| `[in] ...` | 待打印参数列表。 |

<a id="ga118dd6829e092423a85e2b6de07f8dd3"></a>

### `SHELL_WARNING`

```c
#define SHELL_WARNING SHELL_VT100_COLOR_YELLOW
```

```c
#include <zephyr/shell/shell.h>
```

用于shell_fprintf函数的黄色文本（Yellow Text）。

<a id="gacaddbcd6e84f377f39a5d69398996557"></a>

### `shell_bypass_cb_t`

```c
typedef void(* shell_bypass_cb_t) (const struct shell *sh, uint8_t *data, size_t len, void *user_data)
```

```c
#include <zephyr/shell/shell.h>
```

旁路回调（Bypass Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `sh` | Shell实例（Shell Instance）。 |
| `data` | 来自传输层的原始数据（Raw Data）。 |
| `len` | 数据长度（Data Length）。 |
| `user_data` | 传给回调的用户数据（User Data）。 |

<a id="ga331e7d19b9b0755486596f5ffc598338"></a>

### `shell_cmd_handler`

```c
typedef int(* shell_cmd_handler) (const struct shell *sh, size_t argc, char **argv)
```

```c
#include <zephyr/shell/shell.h>
```

Shell命令处理函数原型（Command Handler Prototype）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `sh` | Shell实例（Shell Instance）。 |
| `argc` | 参数数量（Argument Count）。 |
| `argv` | 参数（Arguments）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 命令执行成功。 |
| `1` | 已打印帮助，命令未执行。 |
| `-EINVAL` | 参数校验失败（Argument Validation Failed）。 |
| `-ENOEXEC` | 命令未执行。 |

<a id="gaa2b8cf8ac78b8355408ef94958ebdc70"></a>

### `shell_device_filter_t`

```c
typedef bool(* shell_device_filter_t) (const struct device *dev)
```

```c
#include <zephyr/shell/shell.h>
```

用于shell_device_filter的过滤回调类型（Filter Callback Type）。

作为shell_device_filter的参数使用，只返回符合过滤器（Filter）所实现特定条件的设备。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向struct device的指针。 |

返回（Returns）：布尔值；过滤器匹配设备类型时为true。

<a id="ga182f247052041f1236d13726589885e2"></a>

### `shell_dict_cmd_handler`

```c
typedef int(* shell_dict_cmd_handler) (const struct shell *sh, size_t argc, char **argv, void *data)
```

```c
#include <zephyr/shell/shell.h>
```

Shell字典命令处理函数原型（Dictionary Command Handler Prototype）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `sh` | Shell实例（Shell Instance）。 |
| `argc` | 参数数量（Argument Count）。 |
| `argv` | 参数（Arguments）。 |
| `data` | 用户数据指针（User Data Pointer）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 命令执行成功。 |
| `1` | 已打印帮助，命令未执行。 |
| `-EINVAL` | 参数校验失败（Argument Validation Failed）。 |
| `-ENOEXEC` | 命令未执行。 |

<a id="gafc042f32bac2fdd4cbde9f943e29b008"></a>

### `shell_dynamic_get`

```c
typedef void(* shell_dynamic_get) (size_t idx, struct shell_static_entry *entry)
```

```c
#include <zephyr/shell/shell.h>
```

Shell动态命令描述符（Dynamic Command Descriptor）。

函数应将请求索引idx对应的动态子命令数据填入收到的shell_static_entry结构。有多个动态子命令时，必须保证返回的entry->syntax按字母顺序排序。idx超出可用子命令范围时，必须将entry->syntax设为NULL，以通知Shell模块没有更多动态命令可读取。

<a id="ga265807c2d8eba7b9ea633968627e085d"></a>

### `shell_transport_handler_t`

```c
typedef void(* shell_transport_handler_t) (enum shell_transport_evt evt, void *context)
```

```c
#include <zephyr/shell/shell.h>
```

Shell传输事件处理回调（Transport Event Handler Callback）。

由传输后端调用，通知Shell核心发生了传输事件（Transport Event），例如接收数据已就绪或传输完成。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `evt` | 发生的传输事件。 |
| `context` | 初始化时传给传输层的不透明上下文指针（Opaque Context Pointer），参见shell_transport_api.init。 |

<a id="ga0844a0ce151551d3ccf45d507e5bab25"></a>

### `shell_uninit_cb_t`

```c
typedef void(* shell_uninit_cb_t) (const struct shell *sh, int res)
```

```c
#include <zephyr/shell/shell.h>
```

Shell反初始化完成回调（Uninitialization Completion Callback）。

shell_uninit()完成后、Shell线程终止前，从Shell线程上下文调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `sh` | 已完成反初始化的Shell实例。 |
| `res` | 操作结果：成功为0，失败为负的errno错误码。 |

<a id="ga56bf30741f9ec7a6d94e5c18c2858948"></a>

### `shell_flag`

```c
enum shell_flag
```

```c
#include <zephyr/shell/shell.h>
```

设置Shell输出换行序列（Output Newline Sequence）的标志。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SHELL_FLAG_CRLF_DEFAULT` | 不转换回车（CR）或换行（LF）。 |
| `SHELL_FLAG_OLF_CRLF` | 输出时将LF转换为CRLF。 |

<a id="ga6dcf569be711db32286fb1ef2dcf36d2"></a>

### `shell_vt100_color`

```c
enum shell_vt100_color
```

```c
#include <zephyr/shell/shell_types.h>
```

Shell输出可用的文本颜色（Text Colors）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SHELL_VT100_COLOR_BLACK` | 黑色（Black）。 |
| `SHELL_VT100_COLOR_RED` | 红色（Red）。 |
| `SHELL_VT100_COLOR_GREEN` | 绿色（Green）。 |
| `SHELL_VT100_COLOR_YELLOW` | 黄色（Yellow）。 |
| `SHELL_VT100_COLOR_BLUE` | 蓝色（Blue）。 |
| `SHELL_VT100_COLOR_MAGENTA` | 品红色（Magenta）。 |
| `SHELL_VT100_COLOR_CYAN` | 青色（Cyan）。 |
| `SHELL_VT100_COLOR_WHITE` | 白色（White）。 |
| `SHELL_VT100_COLOR_DEFAULT` | 终端默认前景色（Default Foreground Color）。 |

<a id="ga706aebd24cbdb7f14b9a324515414ecf"></a>

### `shell_cbpprintf()`

```c
void shell_cbpprintf ( const struct shell * sh, enum shell_vt100_color color, void * package )
```

```c
#include <zephyr/shell/shell.h>
```

将cbprintf包格式化后以数据流形式发送到Shell的函数。

类似shell_fprintf，但接收cbprintf包，而非格式字符串和可变参数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] sh` | Shell实例指针。 |
| `[in] color` | 打印文本的颜色（Printed Text Color）。 |
| `[in] package` | 包指针（Package Pointer）。 |

<a id="gae2a8e3d44a9bf5eb55be80833ac6eb5d"></a>

### `shell_device_filter()`

```c
const struct device * shell_device_filter ( size_t idx, shell_device_filter_t filter )
```

```c
#include <zephyr/shell/shell.h>
```

根据索引与过滤器（Filter）取得设备。

可用于返回匹配特定类型的设备。

过滤器返回false、初始化失败或没有非空名称的设备，不会进入匹配候选集合。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `idx` | 从零开始的设备序号。 |
| `filter` | shell_device_filter_t函数指针；设备匹配过滤器时，该函数返回true。 |

<a id="ga7fb40045dc0a27c175e37a6c9cd84b53"></a>

### `shell_device_get_binding()`

```c
const struct device * shell_device_get_binding ( const char * name)
```

```c
#include <zephyr/shell/shell.h>
```

通过device::name字段或标签（Label）取得设备引用。

此函数遍历系统中的设备。若找到name字段与给定名称匹配、且启动时初始化成功的设备，则返回其指针。

没有设备使用该名称时，返回NULL。

找到设备但它未能在启动时成功初始化时，也返回NULL。排查这种情况可在设备驱动初始化函数上设置断点。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `name` | 要查找的设备名称。传入空指针或指向空字符串的指针时，返回NULL。 |

返回（Returns）：具有给定名称的设备结构指针；设备未找到或其初始化函数失败时返回NULL。

<a id="ga919147e222fe10ce14ab3c3a5c5a94e3"></a>

### `shell_device_get_binding_all()`

```c
const struct device * shell_device_get_binding_all ( const char * name)
```

```c
#include <zephyr/shell/shell.h>
```

通过device::name字段或标签（Label）取得设备引用。

此函数遍历系统中的设备。找到name字段与给定名称匹配的设备时，返回其指针。

没有设备使用该名称时，返回NULL。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `name` | 要查找的设备名称。传入空指针或指向空字符串的指针时，返回NULL。 |

返回（Returns）：具有给定名称的设备结构指针；未找到设备时返回NULL。

<a id="ga571db3aa3e024a09e82b117a74d6f248"></a>

### `shell_device_lookup()`

```c
const struct device * shell_device_lookup ( size_t idx, const char * prefix )
```

```c
#include <zephyr/shell/shell.h>
```

按索引取得匹配的设备。（原文在matches后未给出匹配对象，参数说明见下文。）

例如，可用于将I2C_1识别为第二个I2C设备。

初始化失败或没有非空名称的设备，不会进入匹配候选集合。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `idx` | 从零开始的设备序号。 |
| `prefix` | 可选的名称前缀（Name Prefix），用于限制候选设备。索引相对于名称以该文本开头的设备计算。无需前缀匹配时传入空指针。 |

<a id="ga8e83709f5e75d4cea51f42f41bb4e20f"></a>

### `shell_device_lookup_all()`

```c
const struct device * shell_device_lookup_all ( size_t idx, const char * prefix )
```

```c
#include <zephyr/shell/shell.h>
```

按索引取得匹配的设备。（原文在matches后未给出匹配对象，参数说明见下文。）

例如，可用于将I2C_1识别为第二个I2C设备。

初始化失败或被延迟初始化（Deferred Initialization）的设备会进入匹配候选集合，但没有非空名称的设备除外。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `idx` | 从零开始的设备序号。 |
| `prefix` | 可选的名称前缀（Name Prefix），用于限制候选设备。索引相对于名称以该文本开头的设备计算。无需前缀匹配时传入空指针。 |

<a id="ga9f2994f2d6a55521a3e162a81299e4c3"></a>

### `shell_device_lookup_non_ready()`

```c
const struct device * shell_device_lookup_non_ready ( size_t idx, const char * prefix )
```

```c
#include <zephyr/shell/shell.h>
```

按索引取得匹配的、未初始化设备。（原文在matches后未给出匹配对象，参数说明见下文。）

例如，可用于将I2C_1识别为第二个I2C设备。

初始化成功或没有非空名称的设备会被排除。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `idx` | 从零开始的设备序号。 |
| `prefix` | 可选的名称前缀（Name Prefix），用于限制候选设备。索引相对于名称以该文本开头的设备计算。无需前缀匹配时传入空指针。 |

<a id="gad53881371bbaedfd3ef3ecf219706fd1"></a>

### `shell_echo_set()`

```c
int shell_echo_set ( const struct shell * sh, bool val )
```

```c
#include <zephyr/shell/shell.h>
```

允许应用控制是否回显用户输入（Echo）。

以原子方式（Atomically）修改值，并返回先前的值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] sh` | Shell实例指针。 |
| `[in] val` | 回显模式（Echo Mode）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EINVAL` | shell为NULL时。 |

返回（Returns）：0或1，表示先前的值。

<a id="gabfb6a1f1f53f90365de349348015311e"></a>

### `shell_execute_cmd()`

```c
int shell_execute_cmd ( const struct shell * sh, const char * cmd )
```

```c
#include <zephyr/shell/shell.h>
```

执行命令（Execute Command）。

将命令行传给Shell执行。

说明：此操作并不使任何命令成为稳定接口（Stable Interface），因此此函数只应用于调试或诊断。

不得从Shell命令上下文调用此函数！

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] sh` | Shell实例指针。启用CONFIG_SHELL_BACKEND_DUMMY时可以为NULL。 |
| `[in] cmd` | 待执行的命令。 |

返回（Returns）：执行结果。

<a id="ga54dc053c92641bc9b9736bc2d61140f7"></a>

### `shell_get_return_value()`

```c
int shell_get_return_value ( const struct shell * sh)
```

```c
#include <zephyr/shell/shell.h>
```

取得最近一次执行的Shell命令的返回值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] sh` | Shell实例指针。 |

返回（Returns）：上一条命令的返回值。

<a id="ga9e4911ff2c3a07fa70711ddac83701d6"></a>

### `shell_help()`

```c
void shell_help ( const struct shell * sh)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/shell/shell.h>
```

打印当前命令的帮助。

此函数打印帮助字符串，包含当前输入的命令及其子命令（如果存在）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] sh` | Shell实例指针。 |

<a id="ga061bf2530269ebf20d8e006dace5e33b"></a>

### `shell_help_is_structured()`

```c
bool shell_help_is_structured ( const char * help)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/shell/shell.h>
```

检查帮助字符串是否为结构化帮助（Structured Help）。

检查help所指内容是否以结构化帮助魔数（Magic Word）开头，但不假定help按32位对齐，也不假定其作为字符串时至少有4字节长。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `help` | 帮助字符串或结构化帮助的指针。 |

返回（Returns）：结构化帮助为true，否则为false。

<a id="gaeeba0b483974205c54e364d509badd42"></a>

### `shell_hexdump()`

```c
void shell_hexdump ( const struct shell * sh, const uint8_t * data, size_t len )
```

```c
#include <zephyr/shell/shell.h>
```

以十六进制格式打印数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] sh` | Shell实例指针。 |
| `[in] data` | 数据指针。 |
| `[in] len` | 数据长度。 |

<a id="ga0b6e69b499c153ae8f7ba256d445f09d"></a>

### `shell_hexdump_line()`

```c
void shell_hexdump_line ( const struct shell * sh, unsigned int offset, const uint8_t * data, size_t len )
```

```c
#include <zephyr/shell/shell.h>
```

以十六进制格式（Hexadecimal Format）打印一行数据。

每一行依次显示偏移量（Offset）、字节及ASCII表示。

例如：

00008010: 20 25 00 20 2f 48 00 08 80 05 00 20 af 46 00 | %. /H.. ... .F. |

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] sh` | Shell实例指针。 |
| `[in] offset` | 此行要显示的偏移量。 |
| `[in] data` | 数据指针。 |
| `[in] len` | 数据长度。 |

<a id="ga8764ff11603855a10419c48e46e8221c"></a>

### `shell_init()`

```c
int shell_init ( const struct shell * sh, const void * transport_config, struct shell_backend_config_flags cfg_flags, bool log_backend, uint32_t init_log_level )
```

```c
#include <zephyr/shell/shell.h>
```

初始化传输层（Transport Layer）和Shell内部状态的函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] sh` | Shell实例指针。 |
| `[in] transport_config` | 初始化时使用的传输配置（Transport Configuration）。 |
| `[in] cfg_flags` | 后端初始配置标志（Backend Configuration Flags）。Shell会复制这些数据。 |
| `[in] log_backend` | 为true时，将控制台用作日志后端（Logger Backend）。 |
| `[in] init_log_level` | 日志记录器的默认严重性级别（Severity Level）。 |

返回（Returns）：标准错误码（Standard Error Code）。

<a id="gaf1f41d8b6cd430357d593ab0fc5adfeb"></a>

### `shell_insert_mode_set()`

```c
int shell_insert_mode_set ( const struct shell * sh, bool val )
```

```c
#include <zephyr/shell/shell.h>
```

允许应用控制文本插入模式（Insert Mode）。

以原子方式（Atomically）修改值，并返回先前的值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] sh` | Shell实例指针。 |
| `[in] val` | 插入模式（Insert Mode）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EINVAL` | shell为NULL时。 |

返回（Returns）：0或1，表示先前的值。

<a id="ga2df2997c4b04f3246c22f43b274a353b"></a>

### `shell_mode_delete_set()`

```c
int shell_mode_delete_set ( const struct shell * sh, bool val )
```

```c
#include <zephyr/shell/shell.h>
```

允许应用控制Delete键执行退格（Backspace）还是删除（Delete）。

以原子方式（Atomically）修改值，并返回先前的值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] sh` | Shell实例指针。 |
| `[in] val` | 删除模式（Delete Mode）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EINVAL` | shell为NULL时。 |

返回（Returns）：0或1，表示先前的值。

<a id="ga86fade2757d04c9220d5912a4ee540a0"></a>

### `shell_obscure_set()`

```c
int shell_obscure_set ( const struct shell * sh, bool obscure )
```

```c
#include <zephyr/shell/shell.h>
```

允许应用控制是否用星号遮蔽用户输入（Obscure），可用于实现口令输入。

以原子方式（Atomically）修改值，并返回先前的值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] sh` | Shell实例指针。 |
| `[in] obscure` | 遮蔽模式（Obscure Mode）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EINVAL` | shell为NULL时。 |

返回（Returns）：0或1，表示先前的值。

<a id="ga7e66389d0faf15a2a7c31c68cdd9c36c"></a>

### `shell_process()`

```c
void shell_process ( const struct shell * sh)
```

```c
#include <zephyr/shell/shell.h>
```

传输接口中有数据就绪时应执行的处理函数（Process Function）。

用于Shell线程被禁用的情形。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] sh` | Shell实例指针。 |

<a id="ga2113b7227b155755a7ab8a928f7ae499"></a>

### `shell_prompt_change()`

```c
int shell_prompt_change ( const struct shell * sh, const char * prompt )
```

```c
#include <zephyr/shell/shell.h>
```

更改显示的Shell提示符（Prompt）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] sh` | Shell实例指针。 |
| `[in] prompt` | 新的Shell提示符（Prompt）。 |

返回（Returns）：0表示成功；-EINVAL表示新的提示符指针不正确。

<a id="ga05b2eb80f3484216ef2e1d4bf9492453"></a>

### `shell_readline()`

```c
int shell_readline ( const struct shell * sh, uint8_t * buf, size_t len, k_timeout_t timeout )
```

```c
#include <zephyr/shell/shell.h>
```

从Shell读取一行输入。

此函数从Shell传输接口读取数据，直到收到换行字符，并将数据保存到提供的缓冲区。换行字符不存入缓冲区；成功时缓冲区以空字符（NUL）终止。

若通过shell_readline_prompt_set设置了提示符，则在等待输入前打印它；输入行被日志输出打断后，也会恢复该提示符。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] sh` | Shell实例（Shell Instance）。 |
| `[out] buf` | 用于保存输入行的缓冲区。 |
| `[in] len` | 最大缓冲区大小，包含NUL终止字符。 |
| `[in] timeout` | 等待完整一行输入的最长时间。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ETIMEDOUT` | 收到换行字符前发生超时时。 |
| `-ENOBUFS` | buf为NULL或输入超出缓冲区大小时。 |
| `-ECANCELED` | 按下CTRL+C时。 |
| `-EACCES` | 不在正在执行的Shell命令中调用，或已设置旁路回调时。 |

说明（Note）：应在Shell线程的命令处理函数中调用此函数；线程会阻塞，直到返回结果。

返回（Returns）：成功时返回读取的字节数，不含NUL终止字符。

<a id="ga313068db9c3b9972ca4129085d8605d5"></a>

### `shell_readline_prompt_set()`

```c
void shell_readline_prompt_set ( const struct shell * sh, const char * prompt )
```

```c
#include <zephyr/shell/shell.h>
```

为下一次shell_readline调用设置提示字符串（Prompt String）。

提示符在shell_readline开始时打印，并在日志消息之后恢复，以保持用户输入行完整。Shell不会复制该字符串；调用方必须保证它在shell_readline返回前持续有效，返回时会自动清除此提示符。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] sh` | Shell实例（Shell Instance）。 |
| `[in] prompt` | 待显示的提示字符串；NULL表示清除。 |

<a id="ga79369ddfea2dc2cb5813c5eb5c67634a"></a>

### `shell_ready()`

```c
bool shell_ready ( const struct shell * sh)
```

```c
#include <zephyr/shell/shell.h>
```

取得Shell是否已就绪、能够执行命令的状态。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] sh` | Shell实例指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `true` | Shell后端已就绪，可执行命令。 |
| `false` | Shell后端尚未初始化或未启动。 |

<a id="ga4d51d4dbb22bed5d040deabc7ab6dc9d"></a>

### `shell_set_bypass()`

```c
void shell_set_bypass ( const struct shell * sh, shell_bypass_cb_t bypass, void * user_data )
```

```c
#include <zephyr/shell/shell.h>
```

设置旁路回调（Bypass Callback）。

每当接收到数据时调用旁路回调（Bypass Callback）。此时绕过Shell，将数据直接传给回调；使用空指针可禁用旁路功能。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] sh` | Shell实例指针。 |
| `[in] bypass` | 旁路回调；空指针表示禁用。 |
| `[in] user_data` | 旁路回调的用户数据。 |

<a id="ga768c606f2d50f24e9b607ba0a341686d"></a>

### `shell_set_root_cmd()`

```c
int shell_set_root_cmd ( const char * cmd)
```

```c
#include <zephyr/shell/shell.h>
```

为所有Shell实例设置根命令（Root Command）。

允许通过代码设置根命令。它相当于以某个根命令为参数调用select命令，例如select log，但会为所有Shell实例设置该命令。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cmd` | 包含某个根命令名称的字符串；空指针表示重置。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 根命令设置成功时。 |
| `-EINVAL` | 提供的根命令无效时。 |

<a id="gad386d4e8077103e7976f25996fcc3132"></a>

### `shell_start()`

```c
int shell_start ( const struct shell * sh)
```

```c
#include <zephyr/shell/shell.h>
```

启动Shell处理的函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `sh` | Shell实例指针。 |

返回（Returns）：标准错误码（Standard Error Code）。

<a id="gad27754d0beb31bc501f28f9ef26a362c"></a>

### `shell_stop()`

```c
int shell_stop ( const struct shell * sh)
```

```c
#include <zephyr/shell/shell.h>
```

停止Shell处理的函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `sh` | Shell实例指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-ENOTSUP` | Shell已停止或尚未启动时。 |
| `-EBUSY` | Shell线程当前正在处理接收数据，例如执行命令时。请在处理完成后重试。 |

<a id="gaabc3fbdfdc2c3cbd4cd41dc97309aea4"></a>

### `shell_strtobool()`

```c
bool shell_strtobool ( const char * str, int base, int * err )
```

```c
#include <zephyr/shell/shell_string_conv.h>
```

将字符串转换为布尔值（Boolean），并检查错误。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `str` | 输入字符串（Input String）。 |
| `base` | 转换基数（Conversion Base）。 |
| `err` | 错误码指针：字符串输入无效时设为-EINVAL；数值字符串过大、无法转换时设为-ERANGE；成功时保持不变。 |

**警告（Warning）**：警告（Warning）：为避免增加错误检查代码，成功时不会修改传入的err引用。调用方应将err预先初始化为0。

返回（Returns）：转换得到的布尔值（Boolean）。

<a id="ga2a3fc802d8a4d13e49024ee5546d62a6"></a>

### `shell_strtol()`

```c
long shell_strtol ( const char * str, int base, int * err )
```

```c
#include <zephyr/shell/shell_string_conv.h>
```

将字符串转换为long，并检查错误。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `str` | 输入字符串（Input String）。 |
| `base` | 转换基数（Conversion Base）。 |
| `err` | 错误码指针：字符串输入无效为-EINVAL；数值字符串过大、无法转换为-ERANGE；成功时保持不变。 |

**警告（Warning）**：警告（Warning）：为避免增加错误检查代码，成功时不会修改传入的err引用。调用方应将err预先初始化为0。

返回（Returns）：转换得到的long值。

<a id="gac7928525a22e053d1dea44995c8198b9"></a>

### `shell_strtoul()`

```c
unsigned long shell_strtoul ( const char * str, int base, int * err )
```

```c
#include <zephyr/shell/shell_string_conv.h>
```

将字符串转换为unsigned long，并检查错误。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `str` | 输入字符串（Input String）。 |
| `base` | 转换基数（Conversion Base）。 |
| `err` | 错误码指针：字符串输入无效时设为-EINVAL；数值字符串过大、无法转换时设为-ERANGE；成功时保持不变。 |

**警告（Warning）**：警告（Warning）：为避免增加错误检查代码，成功时不会修改传入的err引用。调用方应将err预先初始化为0。

返回（Returns）：转换得到的unsigned long值。

<a id="ga635c05cc9a2e84b6438402334587d537"></a>

### `shell_strtoull()`

```c
unsigned long long shell_strtoull ( const char * str, int base, int * err )
```

```c
#include <zephyr/shell/shell_string_conv.h>
```

将字符串转换为unsigned long long，并检查错误。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `str` | 输入字符串（Input String）。 |
| `base` | 转换基数（Conversion Base）。 |
| `err` | 错误码指针：字符串输入无效时设为-EINVAL；数值字符串过大、无法转换时设为-ERANGE；成功时保持不变。 |

**警告（Warning）**：警告（Warning）：为避免增加错误检查代码，成功时不会修改传入的err引用。调用方应将err预先初始化为0。

返回（Returns）：转换得到的unsigned long long值。

<a id="ga07e76646c5065218464aa8ce78b75af3"></a>

### `shell_uninit()`

```c
void shell_uninit ( const struct shell * sh, shell_uninit_cb_t cb )
```

```c
#include <zephyr/shell/shell.h>
```

反初始化传输层和Shell内部状态。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `sh` | Shell实例指针。 |
| `cb` | 反初始化完成时调用的回调。 |

<a id="ga7d5873456ba43ebd3cc86d25e3f4a72c"></a>

### `shell_use_colors_set()`

```c
int shell_use_colors_set ( const struct shell * sh, bool val )
```

```c
#include <zephyr/shell/shell.h>
```

允许应用控制终端输出是否使用彩色语法（Colored Syntax）。

以原子方式（Atomically）修改值，并返回先前的值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] sh` | Shell实例指针。 |
| `[in] val` | 颜色模式（Color Mode）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EINVAL` | shell为NULL时。 |

返回（Returns）：0或1，表示先前的值。

<a id="ga80ff4b3b4cc62e543fd510c14f55b42a"></a>

### `shell_use_vt100_set()`

```c
int shell_use_vt100_set ( const struct shell * sh, bool val )
```

```c
#include <zephyr/shell/shell.h>
```

允许应用控制终端是否使用VT100命令。

以原子方式（Atomically）修改值，并返回先前的值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] sh` | Shell实例指针。 |
| `[in] val` | VT100模式。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EINVAL` | shell为NULL时。 |

返回（Returns）：0或1，表示先前的值。

<a id="ga74a1c4edd803cad14c893fc9816e534f"></a>

### `shell_vfprintf()`

```c
void shell_vfprintf ( const struct shell * sh, enum shell_vt100_color color, const char * fmt, va_list args )
```

```c
#include <zephyr/shell/shell.h>
```

类似vprintf的函数，向Shell发送格式化数据流。

可从命令处理函数或线程调用此函数，但不能从中断上下文调用。它类似shell_fprintf()，但使用va_list而非可变参数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] sh` | Shell实例指针。 |
| `[in] color` | 打印文本的颜色（Printed Text Color）。 |
| `[in] fmt` | 格式字符串（Format String）。 |
| `[in] args` | 待打印参数列表。 |

## 1.9\_源码定位与版本边界

源码定位：[include/zephyr/shell/shell.h](../../../include/zephyr/shell/shell.h)、[subsys/shell/shell.c](../../../subsys/shell/shell.c)、[subsys/shell/shell_utils.c](../../../subsys/shell/shell_utils.c)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：以下源码跟踪译注独立于官方正文。源码与公开接口按本次官方快照核对，未将隐藏的内部条目补造为公开说明。

> 译注——源码核对：命令注册中的mandatory包含命令名称本身；optional可使用原文规定的特殊标志。条件宏与表达式宏控制命令是否存在，原宏展开保留，用来核对处理函数和子命令在不同配置下的去留。

> 译注——源码核对：动态命令回调应按索引填入条目、保证语法名称按字母顺序排序，并在没有更多条目时将syntax设为NULL。返回指针或空条目的含义应遵守该回调协议，不能用未初始化字段代替结束标记。

> 译注——源码核对：shell_execute_cmd禁止在Shell命令上下文内调用，而shell_readline要求从Shell线程的命令处理函数调用。二者调用条件不同；异步旁路（Bypass）与同步读行也有明确的互斥使用条件。

> 译注——源码核对：readline提示字符串不会被复制，必须有效到读行返回；返回后提示设置会自动清除。缓冲区容量包含NUL终止字符，成功返回的长度不含该字符。

> 译注——源码核对：字符串转换成功时保留err原值，应预先初始化错误变量。返回0或false既可能是有效结果，也可能是失败时的返回值，需要同时检查err。

> 译注——源码核对：shell和shell_ctx原页只给出结构用途，内部字段由Doxygen隐藏；本册对应页如实保留这个公开范围，完整可见布局另见头文件源码。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 1.10\_原页交叉引用（Cross References）

- [Shell后端（Shell Backends）](../shell_backend_reference/P001_Shell后端目录.md)
- [Shell remote](../shell_remote_reference/P001_远端Shell接口.md)
- [shell.h](P002_Shell核心头文件参考.md)
- [shell_string_conv.h](../shell_util_reference/P005_Shell字符串转换头文件参考.md)
- [shell_types.h](../shell_util_reference/P007_Shell类型头文件参考.md)
- [shell_cmd_entry](P011_Shell命令条目联合体.md)
- [shell_static_args](P007_Shell命令参数约束.md)
- [shell_static_entry](P008_Shell静态命令条目.md)
- [shell_cmd_help](P006_Shell命令帮助结构.md)
- [shell_transport_api](P010_Shell传输接口结构.md)
- [shell_transport](P009_Shell传输实例.md)
- [shell_ctx](P005_Shell运行上下文.md)
- [shell](P004_Shell实例结构.md)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [device](../device_reference/P002_设备对象结构.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [device::name](../device_reference/P002_设备对象结构.md#a1e74e8d3b0b1a981c67e1d0284ccac3d)
- [log_backend](../log_backend_reference/P004_日志后端结构.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)
- [cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [UTIL_CAT](../util_reference/P006_内部宏工具头文件参考.md#a7e7766e792d1638bfbbc9d0f328d3d0d)
- [TYPE_SECTION_ITERABLE](../iterable_reference/P001_可遍历段公共接口.md#gac5177fefd615bdd3025fac742d414808)
- [IS_ENABLED](../util_reference/P001_通用工具公共接口.md#ga111fe4e9d63758262fc6810a782cb32a)
- [COND_CODE_1](../util_reference/P001_通用工具公共接口.md#ga358bc3e7669c860a98839a51cd526b20)
- [SHELL_REMOTE_CLI_FPRINTF](../shell_remote_reference/P004_远端Shell命令行头文件参考.md#a6b59d1cfc325f0ef68d1ffc725199755)
- [CONFIG_SHELL_REMOTE_CLI](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL_REMOTE_CLI)
- [FOR_EACH_FIXED_ARG](../util_reference/P001_通用工具公共接口.md#ga1a2b2aa21d7cc37f33e6a62abd2ae340)
- [shell_transport_api.init](P010_Shell传输接口结构.md#a59afba962312a077343b440448d67135)
- [CONFIG_SHELL_BACKEND_DUMMY](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL_BACKEND_DUMMY)
- [true](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#a41f9c5fb8b08eb5dc3edce4dcb37fee7)
- [false](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#a65e9886d74aaee76545e83dd09011727)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__shell__api_html_gad762c496a2ced65069b6d1d02a4d925c"></a>
<a id="agroup__shell__api_html_ga18657f55b8fc37a84660f040a89186bf"></a>
<a id="agroup__iterable__section__apis_html_gac5177fefd615bdd3025fac742d414808"></a>
<a id="astructshell__static__entry_html"></a>
<a id="aunionshell__cmd__entry_html"></a>
<a id="autil__internal_8h_html_a7e7766e792d1638bfbbc9d0f328d3d0d"></a>
<a id="agroup__shell__api_html_gae8a8bbcbb842027c02a319b3fb976a3d"></a>
<a id="agroup__shell__api_html_ga68229f89484c3459d77cebb450ee1f24"></a>
<a id="agroup__sys-util_html_ga111fe4e9d63758262fc6810a782cb32a"></a>
<a id="agroup__shell__api_html_ga331e7d19b9b0755486596f5ffc598338"></a>
<a id="agroup__sys-util_html_ga358bc3e7669c860a98839a51cd526b20"></a>
<a id="agroup__shell__api_html_ga6a3ed4ea9051ac138d22cc39134fb2e5"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="agroup__shell__api_html_gac32c42fb696c2198c73c2c73087cdfc3"></a>
<a id="ashell__remote__cli_8h_html_a6b59d1cfc325f0ef68d1ffc725199755"></a>
<a id="agroup__shell__api_html_ga1fd1671311b112f0c87ab2dafd801105"></a>
<a id="agroup__shell__api_html_ga7664f5e184e9b41ac92e033f7b8d885d"></a>
<a id="agroup__shell__api_html_gaac0ea96fbb5885432dca93174c9ad4e6"></a>
<a id="agroup__shell__api_html_ga4c3a7db0c2bdbf36bbf72302a04bb44d"></a>
<a id="agroup__shell__api_html_ga118dd6829e092423a85e2b6de07f8dd3"></a>
<a id="astructshell__cmd__help_html"></a>
<a id="agroup__shell__api_html_ga06060b98eb505300a3dcc8f922a8e7ab"></a>
<a id="agroup__shell__api_html_gafe3749d6ed0867052d74365c40a702fc"></a>
<a id="agroup__shell__api_html_ga24ade9db85af9a8776a45ba0084f4cca"></a>
<a id="agroup__shell__api_html_ga4f7a3432f76541eb226a426507e10174"></a>
<a id="agroup__shell__api_html_gacb2d1a969368efdbeec704ee6e962dee"></a>
<a id="agroup__shell__api_html_gab1b643efbaee748be0256e904642e310"></a>
<a id="agroup__sys-util_html_ga1a2b2aa21d7cc37f33e6a62abd2ae340"></a>
<a id="agroup__shell__api_html_ga3126019b2100d1ccb2d4dc5efb7d8228"></a>
<a id="agroup__shell__api_html_ga401e19cf8ec8601b8a96fe8e95a2b4d2"></a>
<a id="astructshell_html"></a>
<a id="agroup__shell__api_html_ga214fff4fc56f5a90c4063dad9c233f1b"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga56bf30741f9ec7a6d94e5c18c2858948a343ee559d6259111dbab529a283b23ab"></a>
<a id="gga56bf30741f9ec7a6d94e5c18c2858948ab6fec7b615b6de79e1d00d4117615446"></a>
<a id="gga6dcf569be711db32286fb1ef2dcf36d2a52be3094dd0400eba48c686b0b4e57c6"></a>
<a id="gga6dcf569be711db32286fb1ef2dcf36d2a6f6be6e431dc8e905c5734b4e9c32af4"></a>
<a id="gga6dcf569be711db32286fb1ef2dcf36d2ac6fce9bc89ceb0043697b26cca380c8a"></a>
<a id="gga6dcf569be711db32286fb1ef2dcf36d2adb8fbc39eddceb95f523eed8d5c5bf7d"></a>
<a id="gga6dcf569be711db32286fb1ef2dcf36d2ace5b01755eec4567f0dc65e48143e33d"></a>
<a id="gga6dcf569be711db32286fb1ef2dcf36d2a85c738dbb19eccc90adba2e4a131140a"></a>
<a id="gga6dcf569be711db32286fb1ef2dcf36d2a618a6789463b1980f1086ee128c65972"></a>
<a id="gga6dcf569be711db32286fb1ef2dcf36d2a20523afc967f7f3bc0af645255b0b28c"></a>
<a id="gga6dcf569be711db32286fb1ef2dcf36d2a32de6063c44948beeb8501fed9b7d18e"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[返回大纲](大纲.md) · [下一章](P002_Shell核心头文件参考.md)

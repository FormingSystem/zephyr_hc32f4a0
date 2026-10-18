---
id: learning.zephyr-docs.api-file-display-chat-reference.page-4
title: zephyr__modem__chat.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/chat_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_zephyr\_\_modem\_\_chat.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/chat_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/kernel.h>
#include <zephyr/types.h>
#include <zephyr/device.h>
#include <zephyr/sys/ring_buffer.h>
#include <zephyr/modem/pipe.h>
#include <zephyr/modem/stats.h>
```

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 4.1\_数据结构（Data Structures）

<a id="r_modem_5Fchat_5Fmatch"></a>

```c
struct modem_chat_match
```

相关声明：[modem_chat_match](../modem_wireless_model_reference/P054_modem_chat_match_结构体.md)。

调制解调器交互匹配项（Modem Chat Match）。

<a id="r_modem_5Fchat_5Fscript_5Fchat"></a>

```c
struct modem_chat_script_chat
```

相关声明：[modem_chat_script_chat](../modem_wireless_model_reference/P056_modem_chat_script_chat_结构体.md)。

调制解调器交互脚本中的交互项（Modem Chat Script Chat）。

<a id="r_modem_5Fchat_5Fscript_5Fcompletion_5Finfo"></a>

```c
struct modem_chat_script_completion_info
```

相关声明：[modem_chat_script_completion_info](../modem_wireless_model_reference/P057_modem_chat_script_completion_info_结构体.md)。

已完成脚本（Script）的附加信息。

<a id="r_modem_5Fchat_5Fscript"></a>

```c
struct modem_chat_script
```

相关声明：[modem_chat_script](../modem_wireless_model_reference/P055_modem_chat_script_结构体.md)。

调制解调器交互脚本（Modem Chat Script）。

<a id="r_modem_5Fchat"></a>

```c
struct modem_chat
```

相关声明：[modem_chat](../modem_wireless_model_reference/P052_modem_chat_结构体.md)。

交互实例（Chat Instance）的内部上下文。

<a id="r_modem_5Fchat_5Fconfig"></a>

```c
struct modem_chat_config
```

相关声明：[modem_chat_config](../modem_wireless_model_reference/P053_modem_chat_config_结构体.md)。

交互配置（Chat Configuration）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 4.2\_宏定义（Macros）

<a id="r_ga078fd13acc9abcc0e0aa0304e6a8537a"></a>

```c
#define MODEM_CHAT_MATCH(_match, _separators, _callback)
```

相关声明：[MODEM_CHAT_MATCH](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga078fd13acc9abcc0e0aa0304e6a8537a)。

<a id="r_ga02b06e0d97df03b32eb6c40e91f91fd8"></a>

```c
#define MODEM_CHAT_MATCH_WILDCARD(_match, _separators, _callback)
```

相关声明：[MODEM_CHAT_MATCH_WILDCARD](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga02b06e0d97df03b32eb6c40e91f91fd8)。

<a id="r_gaa62ca91615d0b93b0d2adbcf6c78e251"></a>

```c
#define MODEM_CHAT_MATCH_INITIALIZER(_match, _separators, _callback, _wildcards, _partial)
```

相关声明：[MODEM_CHAT_MATCH_INITIALIZER](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#gaa62ca91615d0b93b0d2adbcf6c78e251)。

<a id="r_ga926b0d2993eb8158137e2caa7687abb8"></a>

```c
#define MODEM_CHAT_MATCH_DEFINE(_sym, _match, _separators, _callback)
```

相关声明：[MODEM_CHAT_MATCH_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga926b0d2993eb8158137e2caa7687abb8)。

<a id="r_ga692a16d6a450ffa4f8b90fd27f1dca61"></a>

```c
#define MODEM_CHAT_MATCH_WILDCARD_DEFINE(_sym, _match, _separators, _callback)
```

相关声明：[MODEM_CHAT_MATCH_WILDCARD_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga692a16d6a450ffa4f8b90fd27f1dca61)。

<a id="r_ga216094ddd94351fadf0e84bacbadc84e"></a>

```c
#define MODEM_CHAT_MATCHES_DEFINE(_sym, ...)
```

相关声明：[MODEM_CHAT_MATCHES_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga216094ddd94351fadf0e84bacbadc84e)。

<a id="r_ga01c94aa4a5881f2f4bdc004d08abaf0d"></a>

```c
#define MODEM_CHAT_SCRIPT_CMD_RESP(_request, _response_match)
```

相关声明：[MODEM_CHAT_SCRIPT_CMD_RESP](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga01c94aa4a5881f2f4bdc004d08abaf0d)。

预期收到单个响应（Single Response）的命令。

<a id="r_gadd48fe039151f5596e5208cccd170746"></a>

```c
#define MODEM_CHAT_SCRIPT_CMD_RESP_MULT(_request, _response_matches)
```

相关声明：[MODEM_CHAT_SCRIPT_CMD_RESP_MULT](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#gadd48fe039151f5596e5208cccd170746)。

能够处理多个响应（Multiple Responses）的命令。

<a id="r_ga0a62af922c1ca5aed812ac634e490453"></a>

```c
#define MODEM_CHAT_SCRIPT_CMD_RESP_NONE(_request, _timeout_ms)
```

相关声明：[MODEM_CHAT_SCRIPT_CMD_RESP_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga0a62af922c1ca5aed812ac634e490453)。

不预期收到任何响应（Response）的命令。

<a id="r_gae89904f4a1a414872ff71a8633c0a1ca"></a>

```c
#define MODEM_CHAT_SCRIPT_CMD_RESP_COND(_request, _response_match, _run_check)
```

相关声明：[MODEM_CHAT_SCRIPT_CMD_RESP_COND](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#gae89904f4a1a414872ff71a8633c0a1ca)。

按条件执行、预期收到单个响应（Single Response）的命令。

<a id="r_ga280eec4caf2a33c24a5e2be25949e4f7"></a>

```c
#define MODEM_CHAT_SCRIPT_CMD_RESP_MULT_COND(_request, _response_matches, _run_check)
```

相关声明：[MODEM_CHAT_SCRIPT_CMD_RESP_MULT_COND](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga280eec4caf2a33c24a5e2be25949e4f7)。

按条件执行、能够处理多个响应（Multiple Responses）的命令。

<a id="r_ga0e3a36d28c818dc251c107f2119ef45a"></a>

```c
#define MODEM_CHAT_SCRIPT_CMD_RESP_NONE_COND(_request, _timeout_ms, _run_check)
```

相关声明：[MODEM_CHAT_SCRIPT_CMD_RESP_NONE_COND](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga0e3a36d28c818dc251c107f2119ef45a)。

按条件执行、不预期收到任何响应（Response）的命令。

<a id="r_gab807fffae2007bc03a8e87ba73921888"></a>

```c
#define MODEM_CHAT_SCRIPT_CMDS_DEFINE(_sym, ...)
```

相关声明：[MODEM_CHAT_SCRIPT_CMDS_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#gab807fffae2007bc03a8e87ba73921888)。

定义 static const modem_chat_script_chat 数组。

<a id="r_gad15f82648a073883c5956d6b14f4e41a"></a>

```c
#define MODEM_CHAT_SCRIPT_DEFINE(_sym, _script_chats, _abort_matches, _callback, _timeout_s)
```

相关声明：[MODEM_CHAT_SCRIPT_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#gad15f82648a073883c5956d6b14f4e41a)。

<a id="r_ga7be78a33341512359a1857baaa4ac915"></a>

```c
#define MODEM_CHAT_SCRIPT_NO_ABORT_DEFINE(_sym, _script_chats, _callback, _timeout_s)
```

相关声明：[MODEM_CHAT_SCRIPT_NO_ABORT_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga7be78a33341512359a1857baaa4ac915)。

<a id="r_ga16441c0c385874a41b9ac071a67cea1c"></a>

```c
#define MODEM_CHAT_SCRIPT_EMPTY_DEFINE(_sym)
```

相关声明：[MODEM_CHAT_SCRIPT_EMPTY_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga16441c0c385874a41b9ac071a67cea1c)。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 4.3\_类型定义（Typedefs）

<a id="r_ga372f3ffe3960a1bd3aa59a377656c262"></a>

```c
typedef bool(* modem_chat_run_check) (void *user_data)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[modem_chat_run_check](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga372f3ffe3960a1bd3aa59a377656c262)。

用于确定是否应执行交互命令（Chat Command）的回调。

<a id="r_gae689e92c91d414f968267e290e5246bd"></a>

```c
typedef void(* modem_chat_match_callback) (struct modem_chat *chat, char **argv, uint16_t argc, void *user_data)
```

相关声明：[modem_chat_match_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#gae689e92c91d414f968267e290e5246bd)、[modem_chat](../modem_wireless_model_reference/P052_modem_chat_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

收到匹配的交互内容（Matching Chat）时调用的回调。

<a id="r_ga1a0680c65972b58ea065b98a78095540"></a>

```c
typedef void(* modem_chat_script_callback) (struct modem_chat *chat, enum modem_chat_script_result result, const struct modem_chat_script_completion_info *info, void *user_data)
```

相关声明：[modem_chat_script_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga1a0680c65972b58ea065b98a78095540)、[modem_chat](../modem_wireless_model_reference/P052_modem_chat_结构体.md)、[modem_chat_script_result](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga4035be227ddec8424311575305647d3e)、[modem_chat_script_completion_info](../modem_wireless_model_reference/P057_modem_chat_script_completion_info_结构体.md)。

脚本执行（Script Execution）完成时调用的回调。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 4.4\_枚举（Enumerations）

<a id="r_ga4035be227ddec8424311575305647d3e"></a>

```c
enum modem_chat_script_result { MODEM_CHAT_SCRIPT_RESULT_SUCCESS , MODEM_CHAT_SCRIPT_RESULT_ABORT , MODEM_CHAT_SCRIPT_RESULT_TIMEOUT }
```

相关声明：[modem_chat_script_result](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga4035be227ddec8424311575305647d3e)、[MODEM_CHAT_SCRIPT_RESULT_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#gga4035be227ddec8424311575305647d3ea977c97fa42b7fb38d337062984b0deee)、[MODEM_CHAT_SCRIPT_RESULT_ABORT](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#gga4035be227ddec8424311575305647d3eacddc6a743055b7c49fac484442dda31b)、[MODEM_CHAT_SCRIPT_RESULT_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#gga4035be227ddec8424311575305647d3ea4991b2748978d1219923d275a42c575e)。

<a id="r_ga734cb1bcbbbf5c87551b20038e0608ae"></a>

```c
enum modem_chat_script_send_state { MODEM_CHAT_SCRIPT_SEND_STATE_IDLE , MODEM_CHAT_SCRIPT_SEND_STATE_REQUEST }
```

相关声明：[modem_chat_script_send_state](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga734cb1bcbbbf5c87551b20038e0608ae)、[MODEM_CHAT_SCRIPT_SEND_STATE_IDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#gga734cb1bcbbbf5c87551b20038e0608aea8971f4f05275f31d255f4a5c7dd47974)、[MODEM_CHAT_SCRIPT_SEND_STATE_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#gga734cb1bcbbbf5c87551b20038e0608aea14824a0ffb464bf00a8aadcf4c8bdbbd)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 4.5\_函数（Functions）

<a id="r_gaf79f3b0e67b5777876137b9e3e16d985"></a>

```c
int modem_chat_init (struct modem_chat *chat, const struct modem_chat_config *config)
```

相关声明：[modem_chat_init](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#gaf79f3b0e67b5777876137b9e3e16d985)、[modem_chat](../modem_wireless_model_reference/P052_modem_chat_结构体.md)、[modem_chat_config](../modem_wireless_model_reference/P053_modem_chat_config_结构体.md)。

初始化调制解调器管道交互实例（Modem Pipe Chat Instance）。

<a id="r_gaf91ae4e64113188e7049a7568a086556"></a>

```c
int modem_chat_attach (struct modem_chat *chat, struct modem_pipe *pipe)
```

相关声明：[modem_chat_attach](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#gaf91ae4e64113188e7049a7568a086556)、[modem_chat](../modem_wireless_model_reference/P052_modem_chat_结构体.md)。

将调制解调器交互实例（Modem Chat Instance）附接到管道（Pipe）。

<a id="r_ga959b05c06c113cd8107dbc71d06b0f81"></a>

```c
bool modem_chat_is_running (struct modem_chat *chat)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[modem_chat_is_running](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga959b05c06c113cd8107dbc71d06b0f81)、[modem_chat](../modem_wireless_model_reference/P052_modem_chat_结构体.md)。

检查脚本（Script）是否正在运行。

<a id="r_ga397d399703449498171ac898776fe791"></a>

```c
int modem_chat_run_script_async (struct modem_chat *chat, const struct modem_chat_script *script)
```

相关声明：[modem_chat_run_script_async](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga397d399703449498171ac898776fe791)、[modem_chat](../modem_wireless_model_reference/P052_modem_chat_结构体.md)、[modem_chat_script](../modem_wireless_model_reference/P055_modem_chat_script_结构体.md)。

异步运行脚本（Run Script Asynchronously）。

<a id="r_gae64d151a5f65bde1dd1973393acf3ff1"></a>

```c
int modem_chat_run_script (struct modem_chat *chat, const struct modem_chat_script *script)
```

相关声明：[modem_chat_run_script](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#gae64d151a5f65bde1dd1973393acf3ff1)、[modem_chat](../modem_wireless_model_reference/P052_modem_chat_结构体.md)、[modem_chat_script](../modem_wireless_model_reference/P055_modem_chat_script_结构体.md)。

运行脚本（Script）。

<a id="r_gaa92ffb91bab15c882cff7b13fca7eeb5"></a>

```c
static int modem_chat_script_run (struct modem_chat *chat, const struct modem_chat_script *script)
```

相关声明：[modem_chat_script_run](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#gaa92ffb91bab15c882cff7b13fca7eeb5)、[modem_chat](../modem_wireless_model_reference/P052_modem_chat_结构体.md)、[modem_chat_script](../modem_wireless_model_reference/P055_modem_chat_script_结构体.md)。

异步运行脚本（Run Script Asynchronously）。

<a id="r_ga5ec3918a4beb6b30deecedbd6f6382ee"></a>

```c
void modem_chat_script_abort (struct modem_chat *chat)
```

相关声明：[modem_chat_script_abort](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga5ec3918a4beb6b30deecedbd6f6382ee)、[modem_chat](../modem_wireless_model_reference/P052_modem_chat_结构体.md)。

中止脚本（Abort Script）。

<a id="r_ga62fa275cb9ce387b0bf5b384c9448c41"></a>

```c
void modem_chat_release (struct modem_chat *chat)
```

相关声明：[modem_chat_release](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga62fa275cb9ce387b0bf5b384c9448c41)、[modem_chat](../modem_wireless_model_reference/P052_modem_chat_结构体.md)。

从交互实例（Chat Instance）释放管道（Pipe）。

<a id="r_ga1f41fc90f5026dc688a90567278ac175"></a>

```c
void modem_chat_match_init (struct modem_chat_match *chat_match)
```

相关声明：[modem_chat_match_init](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga1f41fc90f5026dc688a90567278ac175)、[modem_chat_match](../modem_wireless_model_reference/P054_modem_chat_match_结构体.md)。

初始化调制解调器交互匹配项（Modem Chat Match）。

<a id="r_gac9ed985688aeaee96adcb2b6c4285099"></a>

```c
int modem_chat_match_set_match (struct modem_chat_match *chat_match, const char *match)
```

相关声明：[modem_chat_match_set_match](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#gac9ed985688aeaee96adcb2b6c4285099)、[modem_chat_match](../modem_wireless_model_reference/P054_modem_chat_match_结构体.md)。

设置调制解调器交互匹配实例（Modem Chat Match Instance）的匹配内容（Match）。

<a id="r_ga35c1a4f9ed2677fb747025f859eeae56"></a>

```c
int modem_chat_match_set_separators (struct modem_chat_match *chat_match, const char *separators)
```

相关声明：[modem_chat_match_set_separators](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga35c1a4f9ed2677fb747025f859eeae56)、[modem_chat_match](../modem_wireless_model_reference/P054_modem_chat_match_结构体.md)。

设置调制解调器交互匹配实例（Modem Chat Match Instance）的分隔符（Separators）。

<a id="r_gafea28e13817e1daa6bb5c42514542e4e"></a>

```c
void modem_chat_match_set_callback (struct modem_chat_match *chat_match, modem_chat_match_callback callback)
```

相关声明：[modem_chat_match_set_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#gafea28e13817e1daa6bb5c42514542e4e)、[modem_chat_match](../modem_wireless_model_reference/P054_modem_chat_match_结构体.md)、[modem_chat_match_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#gae689e92c91d414f968267e290e5246bd)。

设置调制解调器交互匹配回调（Modem Chat Match Callback）。

<a id="r_ga53cb148e665095d036edc266e778a8ce"></a>

```c
void modem_chat_match_set_partial (struct modem_chat_match *chat_match, bool partial)
```

相关声明：[modem_chat_match_set_partial](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga53cb148e665095d036edc266e778a8ce)、[modem_chat_match](../modem_wireless_model_reference/P054_modem_chat_match_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

设置调制解调器交互匹配项的部分匹配标志（Partial Flag）。

<a id="r_ga3274b7ffcce059c4d0a5d2ccb3e0bcc6"></a>

```c
void modem_chat_match_enable_wildcards (struct modem_chat_match *chat_match, bool enable)
```

相关声明：[modem_chat_match_enable_wildcards](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga3274b7ffcce059c4d0a5d2ccb3e0bcc6)、[modem_chat_match](../modem_wireless_model_reference/P054_modem_chat_match_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

设置调制解调器交互匹配项的通配符标志（Wildcards Flag）。

<a id="r_gaf12d45cf404e85c94fc13252294c76ca"></a>

```c
void modem_chat_script_chat_init (struct modem_chat_script_chat *script_chat)
```

相关声明：[modem_chat_script_chat_init](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#gaf12d45cf404e85c94fc13252294c76ca)、[modem_chat_script_chat](../modem_wireless_model_reference/P056_modem_chat_script_chat_结构体.md)。

初始化调制解调器交互脚本中的交互项（Modem Chat Script Chat）。

<a id="r_gadaed8cb3a0933fd15a46344ca0df9930"></a>

```c
int modem_chat_script_chat_set_request (struct modem_chat_script_chat *script_chat, const char *request)
```

相关声明：[modem_chat_script_chat_set_request](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#gadaed8cb3a0933fd15a46344ca0df9930)、[modem_chat_script_chat](../modem_wireless_model_reference/P056_modem_chat_script_chat_结构体.md)。

设置调制解调器交互脚本交互项实例的请求（Request）。

<a id="r_ga2aec485e298ebde8af0372deb9c4784f"></a>

```c
int modem_chat_script_chat_set_response_matches (struct modem_chat_script_chat *script_chat, const struct modem_chat_match *response_matches, uint16_t response_matches_size)
```

相关声明：[modem_chat_script_chat_set_response_matches](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga2aec485e298ebde8af0372deb9c4784f)、[modem_chat_script_chat](../modem_wireless_model_reference/P056_modem_chat_script_chat_结构体.md)、[modem_chat_match](../modem_wireless_model_reference/P054_modem_chat_match_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

设置调制解调器交互脚本交互项的匹配项（Matches）。

<a id="r_gae52a949df85cbcb7729c88917f46ef8d"></a>

```c
void modem_chat_script_chat_set_timeout (struct modem_chat_script_chat *script_chat, uint16_t timeout_ms)
```

相关声明：[modem_chat_script_chat_set_timeout](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#gae52a949df85cbcb7729c88917f46ef8d)、[modem_chat_script_chat](../modem_wireless_model_reference/P056_modem_chat_script_chat_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

设置调制解调器交互脚本交互项的超时（Timeout）。

<a id="r_gafdca5529d3ae3c982f3577560216e309"></a>

```c
void modem_chat_script_init (struct modem_chat_script *script)
```

相关声明：[modem_chat_script_init](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#gafdca5529d3ae3c982f3577560216e309)、[modem_chat_script](../modem_wireless_model_reference/P055_modem_chat_script_结构体.md)。

初始化调制解调器交互脚本（Modem Chat Script）。

<a id="r_ga9ab3fa018ee0b2ebaacb3d74ee7ce29a"></a>

```c
void modem_chat_script_set_name (struct modem_chat_script *script, const char *name)
```

相关声明：[modem_chat_script_set_name](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga9ab3fa018ee0b2ebaacb3d74ee7ce29a)、[modem_chat_script](../modem_wireless_model_reference/P055_modem_chat_script_结构体.md)。

设置调制解调器交互脚本名称（Script Name）。

<a id="r_gad6b669708d24a3d3d91d1c40c2c504c8"></a>

```c
int modem_chat_script_set_script_chats (struct modem_chat_script *script, const struct modem_chat_script_chat *script_chats, uint16_t script_chats_size)
```

相关声明：[modem_chat_script_set_script_chats](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#gad6b669708d24a3d3d91d1c40c2c504c8)、[modem_chat_script](../modem_wireless_model_reference/P055_modem_chat_script_结构体.md)、[modem_chat_script_chat](../modem_wireless_model_reference/P056_modem_chat_script_chat_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

设置调制解调器交互脚本的交互项（Chats）。

<a id="r_ga9bff858315a05324ff9690bdbce7398f"></a>

```c
int modem_chat_script_set_abort_matches (struct modem_chat_script *script, const struct modem_chat_match *abort_matches, uint16_t abort_matches_size)
```

相关声明：[modem_chat_script_set_abort_matches](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga9bff858315a05324ff9690bdbce7398f)、[modem_chat_script](../modem_wireless_model_reference/P055_modem_chat_script_结构体.md)、[modem_chat_match](../modem_wireless_model_reference/P054_modem_chat_match_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

设置调制解调器交互脚本的中止匹配项（Abort Matches）。

<a id="r_ga4389d813db136c199c872f20a125eba2"></a>

```c
void modem_chat_script_set_callback (struct modem_chat_script *script, modem_chat_script_callback callback)
```

相关声明：[modem_chat_script_set_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga4389d813db136c199c872f20a125eba2)、[modem_chat_script](../modem_wireless_model_reference/P055_modem_chat_script_结构体.md)、[modem_chat_script_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga1a0680c65972b58ea065b98a78095540)。

设置调制解调器交互脚本回调（Script Callback）。

<a id="r_ga9180fa670c3b6e88fa6011fdce5fd909"></a>

```c
void modem_chat_script_set_timeout (struct modem_chat_script *script, uint32_t timeout_s)
```

相关声明：[modem_chat_script_set_timeout](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga9180fa670c3b6e88fa6011fdce5fd909)、[modem_chat_script](../modem_wireless_model_reference/P055_modem_chat_script_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

设置调制解调器交互脚本超时（Script Timeout）。

<a id="header-var-members"></a>
<a id="var-members"></a>

## 4.6\_变量（Variables）

<a id="r_gada2cd7e12d9a37af6f13ecfb6c182176"></a>

```c
const struct modem_chat_match modem_chat_any_match
```

相关声明：[modem_chat_match](../modem_wireless_model_reference/P054_modem_chat_match_结构体.md)、[modem_chat_any_match](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#gada2cd7e12d9a37af6f13ecfb6c182176)。

<a id="r_gac94a45b118b155ca7de1a45d12297ae4"></a>

```c
const struct modem_chat_match modem_chat_empty_matches [0]
```

相关声明：[modem_chat_match](../modem_wireless_model_reference/P054_modem_chat_match_结构体.md)、[modem_chat_empty_matches](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#gac94a45b118b155ca7de1a45d12297ae4)。

<a id="r_ga19cd30454fb4eb9293e87b24a8cf0655"></a>

```c
const struct modem_chat_script_chat modem_chat_empty_script_chats [0]
```

相关声明：[modem_chat_script_chat](../modem_wireless_model_reference/P056_modem_chat_script_chat_结构体.md)、[modem_chat_empty_script_chats](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga19cd30454fb4eb9293e87b24a8cf0655)。


## 4.7\_原页交叉引用（Cross References）

- [zephyr/kernel.h](../api_source_workqueue_pin_control_reference/P002_kernel.h_源码浏览.md)
- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/sys/ring_buffer.h](../ringbuffer_reference/P004_环形缓冲区头文件源码.md)
- [zephyr/modem/pipe.h](../api_source_supplement_reference/P145_pipe.h_源码浏览.md)
- [zephyr/modem/stats.h](../api_source_reference/P539_stats.h_源码浏览.md)
- [查看此文件的源码。](../api_source_interrupt_modem_reference/P002_chat.h_源码浏览.md)
- [modem_chat_match](../modem_wireless_model_reference/P054_modem_chat_match_结构体.md)
- [modem_chat_script_chat](../modem_wireless_model_reference/P056_modem_chat_script_chat_结构体.md)
- [modem_chat_script_completion_info](../modem_wireless_model_reference/P057_modem_chat_script_completion_info_结构体.md)
- [modem_chat_script](../modem_wireless_model_reference/P055_modem_chat_script_结构体.md)
- [modem_chat](../modem_wireless_model_reference/P052_modem_chat_结构体.md)
- [modem_chat_config](../modem_wireless_model_reference/P053_modem_chat_config_结构体.md)
- [MODEM_CHAT_MATCH](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga078fd13acc9abcc0e0aa0304e6a8537a)
- [MODEM_CHAT_MATCH_WILDCARD](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga02b06e0d97df03b32eb6c40e91f91fd8)
- [MODEM_CHAT_MATCH_INITIALIZER](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#gaa62ca91615d0b93b0d2adbcf6c78e251)
- [MODEM_CHAT_MATCH_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga926b0d2993eb8158137e2caa7687abb8)
- [MODEM_CHAT_MATCH_WILDCARD_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga692a16d6a450ffa4f8b90fd27f1dca61)
- [MODEM_CHAT_MATCHES_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga216094ddd94351fadf0e84bacbadc84e)
- [MODEM_CHAT_SCRIPT_CMD_RESP](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga01c94aa4a5881f2f4bdc004d08abaf0d)
- [MODEM_CHAT_SCRIPT_CMD_RESP_MULT](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#gadd48fe039151f5596e5208cccd170746)
- [MODEM_CHAT_SCRIPT_CMD_RESP_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga0a62af922c1ca5aed812ac634e490453)
- [MODEM_CHAT_SCRIPT_CMD_RESP_COND](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#gae89904f4a1a414872ff71a8633c0a1ca)
- [MODEM_CHAT_SCRIPT_CMD_RESP_MULT_COND](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga280eec4caf2a33c24a5e2be25949e4f7)
- [MODEM_CHAT_SCRIPT_CMD_RESP_NONE_COND](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga0e3a36d28c818dc251c107f2119ef45a)
- [MODEM_CHAT_SCRIPT_CMDS_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#gab807fffae2007bc03a8e87ba73921888)
- [MODEM_CHAT_SCRIPT_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#gad15f82648a073883c5956d6b14f4e41a)
- [MODEM_CHAT_SCRIPT_NO_ABORT_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga7be78a33341512359a1857baaa4ac915)
- [MODEM_CHAT_SCRIPT_EMPTY_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga16441c0c385874a41b9ac071a67cea1c)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [modem_chat_run_check](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga372f3ffe3960a1bd3aa59a377656c262)
- [modem_chat_match_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#gae689e92c91d414f968267e290e5246bd)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [modem_chat_script_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga1a0680c65972b58ea065b98a78095540)
- [modem_chat_script_result](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga4035be227ddec8424311575305647d3e)
- [MODEM_CHAT_SCRIPT_RESULT_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#gga4035be227ddec8424311575305647d3ea977c97fa42b7fb38d337062984b0deee)
- [MODEM_CHAT_SCRIPT_RESULT_ABORT](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#gga4035be227ddec8424311575305647d3eacddc6a743055b7c49fac484442dda31b)
- [MODEM_CHAT_SCRIPT_RESULT_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#gga4035be227ddec8424311575305647d3ea4991b2748978d1219923d275a42c575e)
- [modem_chat_script_send_state](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga734cb1bcbbbf5c87551b20038e0608ae)
- [MODEM_CHAT_SCRIPT_SEND_STATE_IDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#gga734cb1bcbbbf5c87551b20038e0608aea8971f4f05275f31d255f4a5c7dd47974)
- [MODEM_CHAT_SCRIPT_SEND_STATE_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#gga734cb1bcbbbf5c87551b20038e0608aea14824a0ffb464bf00a8aadcf4c8bdbbd)
- [modem_chat_init](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#gaf79f3b0e67b5777876137b9e3e16d985)
- [modem_chat_attach](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#gaf91ae4e64113188e7049a7568a086556)
- [modem_chat_is_running](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga959b05c06c113cd8107dbc71d06b0f81)
- [modem_chat_run_script_async](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga397d399703449498171ac898776fe791)
- [modem_chat_run_script](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#gae64d151a5f65bde1dd1973393acf3ff1)
- [modem_chat_script_run](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#gaa92ffb91bab15c882cff7b13fca7eeb5)
- [modem_chat_script_abort](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga5ec3918a4beb6b30deecedbd6f6382ee)
- [modem_chat_release](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga62fa275cb9ce387b0bf5b384c9448c41)
- [modem_chat_match_init](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga1f41fc90f5026dc688a90567278ac175)
- [modem_chat_match_set_match](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#gac9ed985688aeaee96adcb2b6c4285099)
- [modem_chat_match_set_separators](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga35c1a4f9ed2677fb747025f859eeae56)
- [modem_chat_match_set_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#gafea28e13817e1daa6bb5c42514542e4e)
- [modem_chat_match_set_partial](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga53cb148e665095d036edc266e778a8ce)
- [modem_chat_match_enable_wildcards](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga3274b7ffcce059c4d0a5d2ccb3e0bcc6)
- [modem_chat_script_chat_init](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#gaf12d45cf404e85c94fc13252294c76ca)
- [modem_chat_script_chat_set_request](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#gadaed8cb3a0933fd15a46344ca0df9930)
- [modem_chat_script_chat_set_response_matches](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga2aec485e298ebde8af0372deb9c4784f)
- [modem_chat_script_chat_set_timeout](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#gae52a949df85cbcb7729c88917f46ef8d)
- [modem_chat_script_init](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#gafdca5529d3ae3c982f3577560216e309)
- [modem_chat_script_set_name](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga9ab3fa018ee0b2ebaacb3d74ee7ce29a)
- [modem_chat_script_set_script_chats](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#gad6b669708d24a3d3d91d1c40c2c504c8)
- [modem_chat_script_set_abort_matches](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga9bff858315a05324ff9690bdbce7398f)
- [modem_chat_script_set_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga4389d813db136c199c872f20a125eba2)
- [modem_chat_script_set_timeout](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga9180fa670c3b6e88fa6011fdce5fd909)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [modem_chat_any_match](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#gada2cd7e12d9a37af6f13ecfb6c182176)
- [modem_chat_empty_matches](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#gac94a45b118b155ca7de1a45d12297ae4)
- [modem_chat_empty_script_chats](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga19cd30454fb4eb9293e87b24a8cf0655)

---

[上一章](P003_zephyr__bluetooth__mesh__cfg.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P005_zephyr__bluetooth__audio__csip.h_文件参考.md)

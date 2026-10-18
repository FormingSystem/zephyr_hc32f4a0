---
id: learning.zephyr-docs.api-flash-connection-topic-reference.page-7
title: 调制解调器命令会话（Modem Chat）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_调制解调器命令会话（Modem Chat）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

调制解调器命令会话（Modem Chat）

<a id="details"></a>

调制解调器命令交互（Modem Chat）。起始版本（Since）：3.5。接口版本（Version）：1.0.0。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 7.1\_数据结构（Data Structures）

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

## 7.2\_宏定义（Macros）

<a id="r_ga078fd13acc9abcc0e0aa0304e6a8537a"></a>

```c
#define MODEM_CHAT_MATCH(_match, _separators, _callback)
```

相关声明：[MODEM_CHAT_MATCH](#ga078fd13acc9abcc0e0aa0304e6a8537a)。

<a id="r_ga02b06e0d97df03b32eb6c40e91f91fd8"></a>

```c
#define MODEM_CHAT_MATCH_WILDCARD(_match, _separators, _callback)
```

相关声明：[MODEM_CHAT_MATCH_WILDCARD](#ga02b06e0d97df03b32eb6c40e91f91fd8)。

<a id="r_gaa62ca91615d0b93b0d2adbcf6c78e251"></a>

```c
#define MODEM_CHAT_MATCH_INITIALIZER(_match, _separators, _callback, _wildcards, _partial)
```

相关声明：[MODEM_CHAT_MATCH_INITIALIZER](#gaa62ca91615d0b93b0d2adbcf6c78e251)。

<a id="r_ga926b0d2993eb8158137e2caa7687abb8"></a>

```c
#define MODEM_CHAT_MATCH_DEFINE(_sym, _match, _separators, _callback)
```

相关声明：[MODEM_CHAT_MATCH_DEFINE](#ga926b0d2993eb8158137e2caa7687abb8)。

<a id="r_ga692a16d6a450ffa4f8b90fd27f1dca61"></a>

```c
#define MODEM_CHAT_MATCH_WILDCARD_DEFINE(_sym, _match, _separators, _callback)
```

相关声明：[MODEM_CHAT_MATCH_WILDCARD_DEFINE](#ga692a16d6a450ffa4f8b90fd27f1dca61)。

<a id="r_ga216094ddd94351fadf0e84bacbadc84e"></a>

```c
#define MODEM_CHAT_MATCHES_DEFINE(_sym, ...)
```

相关声明：[MODEM_CHAT_MATCHES_DEFINE](#ga216094ddd94351fadf0e84bacbadc84e)。

<a id="r_ga01c94aa4a5881f2f4bdc004d08abaf0d"></a>

```c
#define MODEM_CHAT_SCRIPT_CMD_RESP(_request, _response_match)
```

相关声明：[MODEM_CHAT_SCRIPT_CMD_RESP](#ga01c94aa4a5881f2f4bdc004d08abaf0d)。

预期收到单个响应（Single Response）的命令。

<a id="r_gadd48fe039151f5596e5208cccd170746"></a>

```c
#define MODEM_CHAT_SCRIPT_CMD_RESP_MULT(_request, _response_matches)
```

相关声明：[MODEM_CHAT_SCRIPT_CMD_RESP_MULT](#gadd48fe039151f5596e5208cccd170746)。

能够处理多个响应（Multiple Responses）的命令。

<a id="r_ga0a62af922c1ca5aed812ac634e490453"></a>

```c
#define MODEM_CHAT_SCRIPT_CMD_RESP_NONE(_request, _timeout_ms)
```

相关声明：[MODEM_CHAT_SCRIPT_CMD_RESP_NONE](#ga0a62af922c1ca5aed812ac634e490453)。

不预期收到任何响应（Response）的命令。

<a id="r_gae89904f4a1a414872ff71a8633c0a1ca"></a>

```c
#define MODEM_CHAT_SCRIPT_CMD_RESP_COND(_request, _response_match, _run_check)
```

相关声明：[MODEM_CHAT_SCRIPT_CMD_RESP_COND](#gae89904f4a1a414872ff71a8633c0a1ca)。

按条件执行、预期收到单个响应（Single Response）的命令。

<a id="r_ga280eec4caf2a33c24a5e2be25949e4f7"></a>

```c
#define MODEM_CHAT_SCRIPT_CMD_RESP_MULT_COND(_request, _response_matches, _run_check)
```

相关声明：[MODEM_CHAT_SCRIPT_CMD_RESP_MULT_COND](#ga280eec4caf2a33c24a5e2be25949e4f7)。

按条件执行、能够处理多个响应（Multiple Responses）的命令。

<a id="r_ga0e3a36d28c818dc251c107f2119ef45a"></a>

```c
#define MODEM_CHAT_SCRIPT_CMD_RESP_NONE_COND(_request, _timeout_ms, _run_check)
```

相关声明：[MODEM_CHAT_SCRIPT_CMD_RESP_NONE_COND](#ga0e3a36d28c818dc251c107f2119ef45a)。

按条件执行、不预期收到任何响应（Response）的命令。

<a id="r_gab807fffae2007bc03a8e87ba73921888"></a>

```c
#define MODEM_CHAT_SCRIPT_CMDS_DEFINE(_sym, ...)
```

相关声明：[MODEM_CHAT_SCRIPT_CMDS_DEFINE](#gab807fffae2007bc03a8e87ba73921888)。

定义 static const modem_chat_script_chat 数组。

<a id="r_gad15f82648a073883c5956d6b14f4e41a"></a>

```c
#define MODEM_CHAT_SCRIPT_DEFINE(_sym, _script_chats, _abort_matches, _callback, _timeout_s)
```

相关声明：[MODEM_CHAT_SCRIPT_DEFINE](#gad15f82648a073883c5956d6b14f4e41a)。

<a id="r_ga7be78a33341512359a1857baaa4ac915"></a>

```c
#define MODEM_CHAT_SCRIPT_NO_ABORT_DEFINE(_sym, _script_chats, _callback, _timeout_s)
```

相关声明：[MODEM_CHAT_SCRIPT_NO_ABORT_DEFINE](#ga7be78a33341512359a1857baaa4ac915)。

<a id="r_ga16441c0c385874a41b9ac071a67cea1c"></a>

```c
#define MODEM_CHAT_SCRIPT_EMPTY_DEFINE(_sym)
```

相关声明：[MODEM_CHAT_SCRIPT_EMPTY_DEFINE](#ga16441c0c385874a41b9ac071a67cea1c)。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 7.3\_类型定义（Typedefs）

<a id="r_ga372f3ffe3960a1bd3aa59a377656c262"></a>

```c
typedef bool(* modem_chat_run_check) (void *user_data)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[modem_chat_run_check](#ga372f3ffe3960a1bd3aa59a377656c262)。

用于确定是否应执行交互命令（Chat Command）的回调。

<a id="r_gae689e92c91d414f968267e290e5246bd"></a>

```c
typedef void(* modem_chat_match_callback) (struct modem_chat *chat, char **argv, uint16_t argc, void *user_data)
```

相关声明：[modem_chat_match_callback](#gae689e92c91d414f968267e290e5246bd)、[modem_chat](../modem_wireless_model_reference/P052_modem_chat_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

收到匹配的交互内容（Matching Chat）时调用的回调。

<a id="r_ga1a0680c65972b58ea065b98a78095540"></a>

```c
typedef void(* modem_chat_script_callback) (struct modem_chat *chat, enum modem_chat_script_result result, const struct modem_chat_script_completion_info *info, void *user_data)
```

相关声明：[modem_chat_script_callback](#ga1a0680c65972b58ea065b98a78095540)、[modem_chat](../modem_wireless_model_reference/P052_modem_chat_结构体.md)、[modem_chat_script_result](#ga4035be227ddec8424311575305647d3e)、[modem_chat_script_completion_info](../modem_wireless_model_reference/P057_modem_chat_script_completion_info_结构体.md)。

脚本执行（Script Execution）完成时调用的回调。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 7.4\_枚举（Enumerations）

<a id="r_ga4035be227ddec8424311575305647d3e"></a>

```c
enum modem_chat_script_result { MODEM_CHAT_SCRIPT_RESULT_SUCCESS , MODEM_CHAT_SCRIPT_RESULT_ABORT , MODEM_CHAT_SCRIPT_RESULT_TIMEOUT }
```

相关声明：[modem_chat_script_result](#ga4035be227ddec8424311575305647d3e)、[MODEM_CHAT_SCRIPT_RESULT_SUCCESS](#gga4035be227ddec8424311575305647d3ea977c97fa42b7fb38d337062984b0deee)、[MODEM_CHAT_SCRIPT_RESULT_ABORT](#gga4035be227ddec8424311575305647d3eacddc6a743055b7c49fac484442dda31b)、[MODEM_CHAT_SCRIPT_RESULT_TIMEOUT](#gga4035be227ddec8424311575305647d3ea4991b2748978d1219923d275a42c575e)。

<a id="r_ga734cb1bcbbbf5c87551b20038e0608ae"></a>

```c
enum modem_chat_script_send_state { MODEM_CHAT_SCRIPT_SEND_STATE_IDLE , MODEM_CHAT_SCRIPT_SEND_STATE_REQUEST }
```

相关声明：[modem_chat_script_send_state](#ga734cb1bcbbbf5c87551b20038e0608ae)、[MODEM_CHAT_SCRIPT_SEND_STATE_IDLE](#gga734cb1bcbbbf5c87551b20038e0608aea8971f4f05275f31d255f4a5c7dd47974)、[MODEM_CHAT_SCRIPT_SEND_STATE_REQUEST](#gga734cb1bcbbbf5c87551b20038e0608aea14824a0ffb464bf00a8aadcf4c8bdbbd)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 7.5\_函数（Functions）

<a id="r_gaf79f3b0e67b5777876137b9e3e16d985"></a>

```c
int modem_chat_init (struct modem_chat *chat, const struct modem_chat_config *config)
```

相关声明：[modem_chat_init](#gaf79f3b0e67b5777876137b9e3e16d985)、[modem_chat](../modem_wireless_model_reference/P052_modem_chat_结构体.md)、[modem_chat_config](../modem_wireless_model_reference/P053_modem_chat_config_结构体.md)。

初始化调制解调器管道交互实例（Modem Pipe Chat Instance）。

<a id="r_gaf91ae4e64113188e7049a7568a086556"></a>

```c
int modem_chat_attach (struct modem_chat *chat, struct modem_pipe *pipe)
```

相关声明：[modem_chat_attach](#gaf91ae4e64113188e7049a7568a086556)、[modem_chat](../modem_wireless_model_reference/P052_modem_chat_结构体.md)。

将调制解调器交互实例（Modem Chat Instance）附接到管道（Pipe）。

<a id="r_ga959b05c06c113cd8107dbc71d06b0f81"></a>

```c
bool modem_chat_is_running (struct modem_chat *chat)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[modem_chat_is_running](#ga959b05c06c113cd8107dbc71d06b0f81)、[modem_chat](../modem_wireless_model_reference/P052_modem_chat_结构体.md)。

检查脚本（Script）是否正在运行。

<a id="r_ga397d399703449498171ac898776fe791"></a>

```c
int modem_chat_run_script_async (struct modem_chat *chat, const struct modem_chat_script *script)
```

相关声明：[modem_chat_run_script_async](#ga397d399703449498171ac898776fe791)、[modem_chat](../modem_wireless_model_reference/P052_modem_chat_结构体.md)、[modem_chat_script](../modem_wireless_model_reference/P055_modem_chat_script_结构体.md)。

异步运行脚本（Run Script Asynchronously）。

<a id="r_gae64d151a5f65bde1dd1973393acf3ff1"></a>

```c
int modem_chat_run_script (struct modem_chat *chat, const struct modem_chat_script *script)
```

相关声明：[modem_chat_run_script](#gae64d151a5f65bde1dd1973393acf3ff1)、[modem_chat](../modem_wireless_model_reference/P052_modem_chat_结构体.md)、[modem_chat_script](../modem_wireless_model_reference/P055_modem_chat_script_结构体.md)。

运行脚本（Script）。

<a id="r_gaa92ffb91bab15c882cff7b13fca7eeb5"></a>

```c
static int modem_chat_script_run (struct modem_chat *chat, const struct modem_chat_script *script)
```

相关声明：[modem_chat_script_run](#gaa92ffb91bab15c882cff7b13fca7eeb5)、[modem_chat](../modem_wireless_model_reference/P052_modem_chat_结构体.md)、[modem_chat_script](../modem_wireless_model_reference/P055_modem_chat_script_结构体.md)。

异步运行脚本（Run Script Asynchronously）。

<a id="r_ga5ec3918a4beb6b30deecedbd6f6382ee"></a>

```c
void modem_chat_script_abort (struct modem_chat *chat)
```

相关声明：[modem_chat_script_abort](#ga5ec3918a4beb6b30deecedbd6f6382ee)、[modem_chat](../modem_wireless_model_reference/P052_modem_chat_结构体.md)。

中止脚本（Abort Script）。

<a id="r_ga62fa275cb9ce387b0bf5b384c9448c41"></a>

```c
void modem_chat_release (struct modem_chat *chat)
```

相关声明：[modem_chat_release](#ga62fa275cb9ce387b0bf5b384c9448c41)、[modem_chat](../modem_wireless_model_reference/P052_modem_chat_结构体.md)。

从交互实例（Chat Instance）释放管道（Pipe）。

<a id="r_ga1f41fc90f5026dc688a90567278ac175"></a>

```c
void modem_chat_match_init (struct modem_chat_match *chat_match)
```

相关声明：[modem_chat_match_init](#ga1f41fc90f5026dc688a90567278ac175)、[modem_chat_match](../modem_wireless_model_reference/P054_modem_chat_match_结构体.md)。

初始化调制解调器交互匹配项（Modem Chat Match）。

<a id="r_gac9ed985688aeaee96adcb2b6c4285099"></a>

```c
int modem_chat_match_set_match (struct modem_chat_match *chat_match, const char *match)
```

相关声明：[modem_chat_match_set_match](#gac9ed985688aeaee96adcb2b6c4285099)、[modem_chat_match](../modem_wireless_model_reference/P054_modem_chat_match_结构体.md)。

设置调制解调器交互匹配实例（Modem Chat Match Instance）的匹配内容（Match）。

<a id="r_ga35c1a4f9ed2677fb747025f859eeae56"></a>

```c
int modem_chat_match_set_separators (struct modem_chat_match *chat_match, const char *separators)
```

相关声明：[modem_chat_match_set_separators](#ga35c1a4f9ed2677fb747025f859eeae56)、[modem_chat_match](../modem_wireless_model_reference/P054_modem_chat_match_结构体.md)。

设置调制解调器交互匹配实例（Modem Chat Match Instance）的分隔符（Separators）。

<a id="r_gafea28e13817e1daa6bb5c42514542e4e"></a>

```c
void modem_chat_match_set_callback (struct modem_chat_match *chat_match, modem_chat_match_callback callback)
```

相关声明：[modem_chat_match_set_callback](#gafea28e13817e1daa6bb5c42514542e4e)、[modem_chat_match](../modem_wireless_model_reference/P054_modem_chat_match_结构体.md)、[modem_chat_match_callback](#gae689e92c91d414f968267e290e5246bd)。

设置调制解调器交互匹配回调（Modem Chat Match Callback）。

<a id="r_ga53cb148e665095d036edc266e778a8ce"></a>

```c
void modem_chat_match_set_partial (struct modem_chat_match *chat_match, bool partial)
```

相关声明：[modem_chat_match_set_partial](#ga53cb148e665095d036edc266e778a8ce)、[modem_chat_match](../modem_wireless_model_reference/P054_modem_chat_match_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

设置调制解调器交互匹配项的部分匹配标志（Partial Flag）。

<a id="r_ga3274b7ffcce059c4d0a5d2ccb3e0bcc6"></a>

```c
void modem_chat_match_enable_wildcards (struct modem_chat_match *chat_match, bool enable)
```

相关声明：[modem_chat_match_enable_wildcards](#ga3274b7ffcce059c4d0a5d2ccb3e0bcc6)、[modem_chat_match](../modem_wireless_model_reference/P054_modem_chat_match_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

设置调制解调器交互匹配项的通配符标志（Wildcards Flag）。

<a id="r_gaf12d45cf404e85c94fc13252294c76ca"></a>

```c
void modem_chat_script_chat_init (struct modem_chat_script_chat *script_chat)
```

相关声明：[modem_chat_script_chat_init](#gaf12d45cf404e85c94fc13252294c76ca)、[modem_chat_script_chat](../modem_wireless_model_reference/P056_modem_chat_script_chat_结构体.md)。

初始化调制解调器交互脚本中的交互项（Modem Chat Script Chat）。

<a id="r_gadaed8cb3a0933fd15a46344ca0df9930"></a>

```c
int modem_chat_script_chat_set_request (struct modem_chat_script_chat *script_chat, const char *request)
```

相关声明：[modem_chat_script_chat_set_request](#gadaed8cb3a0933fd15a46344ca0df9930)、[modem_chat_script_chat](../modem_wireless_model_reference/P056_modem_chat_script_chat_结构体.md)。

设置调制解调器交互脚本交互项实例的请求（Request）。

<a id="r_ga2aec485e298ebde8af0372deb9c4784f"></a>

```c
int modem_chat_script_chat_set_response_matches (struct modem_chat_script_chat *script_chat, const struct modem_chat_match *response_matches, uint16_t response_matches_size)
```

相关声明：[modem_chat_script_chat_set_response_matches](#ga2aec485e298ebde8af0372deb9c4784f)、[modem_chat_script_chat](../modem_wireless_model_reference/P056_modem_chat_script_chat_结构体.md)、[modem_chat_match](../modem_wireless_model_reference/P054_modem_chat_match_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

设置调制解调器交互脚本交互项的匹配项（Matches）。

<a id="r_gae52a949df85cbcb7729c88917f46ef8d"></a>

```c
void modem_chat_script_chat_set_timeout (struct modem_chat_script_chat *script_chat, uint16_t timeout_ms)
```

相关声明：[modem_chat_script_chat_set_timeout](#gae52a949df85cbcb7729c88917f46ef8d)、[modem_chat_script_chat](../modem_wireless_model_reference/P056_modem_chat_script_chat_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

设置调制解调器交互脚本交互项的超时（Timeout）。

<a id="r_gafdca5529d3ae3c982f3577560216e309"></a>

```c
void modem_chat_script_init (struct modem_chat_script *script)
```

相关声明：[modem_chat_script_init](#gafdca5529d3ae3c982f3577560216e309)、[modem_chat_script](../modem_wireless_model_reference/P055_modem_chat_script_结构体.md)。

初始化调制解调器交互脚本（Modem Chat Script）。

<a id="r_ga9ab3fa018ee0b2ebaacb3d74ee7ce29a"></a>

```c
void modem_chat_script_set_name (struct modem_chat_script *script, const char *name)
```

相关声明：[modem_chat_script_set_name](#ga9ab3fa018ee0b2ebaacb3d74ee7ce29a)、[modem_chat_script](../modem_wireless_model_reference/P055_modem_chat_script_结构体.md)。

设置调制解调器交互脚本名称（Script Name）。

<a id="r_gad6b669708d24a3d3d91d1c40c2c504c8"></a>

```c
int modem_chat_script_set_script_chats (struct modem_chat_script *script, const struct modem_chat_script_chat *script_chats, uint16_t script_chats_size)
```

相关声明：[modem_chat_script_set_script_chats](#gad6b669708d24a3d3d91d1c40c2c504c8)、[modem_chat_script](../modem_wireless_model_reference/P055_modem_chat_script_结构体.md)、[modem_chat_script_chat](../modem_wireless_model_reference/P056_modem_chat_script_chat_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

设置调制解调器交互脚本的交互项（Chats）。

<a id="r_ga9bff858315a05324ff9690bdbce7398f"></a>

```c
int modem_chat_script_set_abort_matches (struct modem_chat_script *script, const struct modem_chat_match *abort_matches, uint16_t abort_matches_size)
```

相关声明：[modem_chat_script_set_abort_matches](#ga9bff858315a05324ff9690bdbce7398f)、[modem_chat_script](../modem_wireless_model_reference/P055_modem_chat_script_结构体.md)、[modem_chat_match](../modem_wireless_model_reference/P054_modem_chat_match_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

设置调制解调器交互脚本的中止匹配项（Abort Matches）。

<a id="r_ga4389d813db136c199c872f20a125eba2"></a>

```c
void modem_chat_script_set_callback (struct modem_chat_script *script, modem_chat_script_callback callback)
```

相关声明：[modem_chat_script_set_callback](#ga4389d813db136c199c872f20a125eba2)、[modem_chat_script](../modem_wireless_model_reference/P055_modem_chat_script_结构体.md)、[modem_chat_script_callback](#ga1a0680c65972b58ea065b98a78095540)。

设置调制解调器交互脚本回调（Script Callback）。

<a id="r_ga9180fa670c3b6e88fa6011fdce5fd909"></a>

```c
void modem_chat_script_set_timeout (struct modem_chat_script *script, uint32_t timeout_s)
```

相关声明：[modem_chat_script_set_timeout](#ga9180fa670c3b6e88fa6011fdce5fd909)、[modem_chat_script](../modem_wireless_model_reference/P055_modem_chat_script_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

设置调制解调器交互脚本超时（Script Timeout）。

<a id="header-var-members"></a>
<a id="var-members"></a>

## 7.6\_变量（Variables）

<a id="r_gada2cd7e12d9a37af6f13ecfb6c182176"></a>

```c
const struct modem_chat_match modem_chat_any_match
```

相关声明：[modem_chat_match](../modem_wireless_model_reference/P054_modem_chat_match_结构体.md)、[modem_chat_any_match](#gada2cd7e12d9a37af6f13ecfb6c182176)。

<a id="r_gac94a45b118b155ca7de1a45d12297ae4"></a>

```c
const struct modem_chat_match modem_chat_empty_matches [0]
```

相关声明：[modem_chat_match](../modem_wireless_model_reference/P054_modem_chat_match_结构体.md)、[modem_chat_empty_matches](#gac94a45b118b155ca7de1a45d12297ae4)。

<a id="r_ga19cd30454fb4eb9293e87b24a8cf0655"></a>

```c
const struct modem_chat_script_chat modem_chat_empty_script_chats [0]
```

相关声明：[modem_chat_script_chat](../modem_wireless_model_reference/P056_modem_chat_script_chat_结构体.md)、[modem_chat_empty_script_chats](#ga19cd30454fb4eb9293e87b24a8cf0655)。

## 7.7\_详细说明（Detailed Documentation）

<a id="ga078fd13acc9abcc0e0aa0304e6a8537a"></a>

### `MODEM_CHAT_MATCH`

```c
#define MODEM_CHAT_MATCH ( _match, _separators, _callback )
```

```c
#include <zephyr/modem/chat.h>
```

展开值（Value）：

```c
{                                                                                          \
        .match = (uint8_t *)(_match),                                                      \
        .separators = (uint8_t *)(_separators),                                            \
        .match_size = (uint8_t)(sizeof(_match) - 1),                                       \
        .separators_size = (uint8_t)(sizeof(_separators) - 1),                             \
        .wildcards = false,                                                                \
        .callback = _callback,                                                             \
}
```

<a id="ga926b0d2993eb8158137e2caa7687abb8"></a>

### `MODEM_CHAT_MATCH_DEFINE`

```c
#define MODEM_CHAT_MATCH_DEFINE ( _sym, _match, _separators, _callback )
```

```c
#include <zephyr/modem/chat.h>
```

展开值（Value）：

```c
const static struct modem_chat_match _sym = MODEM_CHAT_MATCH(_match, _separators, _callback)
```

<a id="gaa62ca91615d0b93b0d2adbcf6c78e251"></a>

### `MODEM_CHAT_MATCH_INITIALIZER`

```c
#define MODEM_CHAT_MATCH_INITIALIZER ( _match, _separators, _callback, _wildcards, _partial )
```

```c
#include <zephyr/modem/chat.h>
```

展开值（Value）：

```c
{                                                                                          \
        .match = (uint8_t *)(_match),                                                      \
        .separators = (uint8_t *)(_separators),                                            \
        .match_size = (uint8_t)(sizeof(_match) - 1),                                       \
        .separators_size = (uint8_t)(sizeof(_separators) - 1),                             \
        .wildcards = _wildcards,                                                           \
        .partial = _partial,                                                               \
        .callback = _callback,                                                             \
}
```

<a id="ga02b06e0d97df03b32eb6c40e91f91fd8"></a>

### `MODEM_CHAT_MATCH_WILDCARD`

```c
#define MODEM_CHAT_MATCH_WILDCARD ( _match, _separators, _callback )
```

```c
#include <zephyr/modem/chat.h>
```

展开值（Value）：

```c
{                                                                                          \
        .match = (uint8_t *)(_match),                                                      \
        .separators = (uint8_t *)(_separators),                                            \
        .match_size = (uint8_t)(sizeof(_match) - 1),                                       \
        .separators_size = (uint8_t)(sizeof(_separators) - 1),                             \
        .wildcards = true,                                                                 \
        .callback = _callback,                                                             \
}
```

<a id="ga692a16d6a450ffa4f8b90fd27f1dca61"></a>

### `MODEM_CHAT_MATCH_WILDCARD_DEFINE`

```c
#define MODEM_CHAT_MATCH_WILDCARD_DEFINE ( _sym, _match, _separators, _callback )
```

```c
#include <zephyr/modem/chat.h>
```

展开值（Value）：

```c
const static struct modem_chat_match _sym =                                                \
        MODEM_CHAT_MATCH_WILDCARD(_match, _separators, _callback)
```

<a id="ga216094ddd94351fadf0e84bacbadc84e"></a>

### `MODEM_CHAT_MATCHES_DEFINE`

```c
#define MODEM_CHAT_MATCHES_DEFINE ( _sym, ... )
```

```c
#include <zephyr/modem/chat.h>
```

展开值（Value）：

```c
const static struct modem_chat_match _sym[] = {__VA_ARGS__}
```

<a id="ga01c94aa4a5881f2f4bdc004d08abaf0d"></a>

### `MODEM_CHAT_SCRIPT_CMD_RESP`

```c
#define MODEM_CHAT_SCRIPT_CMD_RESP ( _request, _response_match )
```

```c
#include <zephyr/modem/chat.h>
```

展开值（Value）：

```c
{                                                                                          \
        .request = (uint8_t *)(_request),                                                  \
        .request_size = (uint16_t)(sizeof(_request) - 1),                                  \
        .response_matches = &_response_match,                                              \
        .response_matches_size = 1,                                                        \
        .timeout = 0,                                                                      \
}
```

预期收到单个响应（Single Response）的命令。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_request` | 要发送的命令字符串（Command String）。 |
| `_response_match` | 预期响应（Expected Response），由 `MODEM_CHAT_MATCH` 或其变体创建。 |

<a id="gae89904f4a1a414872ff71a8633c0a1ca"></a>

### `MODEM_CHAT_SCRIPT_CMD_RESP_COND`

```c
#define MODEM_CHAT_SCRIPT_CMD_RESP_COND ( _request, _response_match, _run_check )
```

```c
#include <zephyr/modem/chat.h>
```

展开值（Value）：

```c
{                                                                                          \
        .request = (uint8_t *)(_request),                                                  \
        .request_size = (uint16_t)(sizeof(_request) - 1),                                  \
        .response_matches = &_response_match,                                              \
        .response_matches_size = 1,                                                        \
        .timeout = 0,                                                                      \
        .run_check = _run_check                                                            \
}
```

按条件执行、预期收到单个响应（Single Response）的命令。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_request` | 要发送的命令字符串（Command String）。 |
| `_response_match` | 预期响应（Expected Response），由 `MODEM_CHAT_MATCH` 或其变体创建。 |
| `_run_check` | 控制是否执行命令的回调（Callback）。 |

<a id="gadd48fe039151f5596e5208cccd170746"></a>

### `MODEM_CHAT_SCRIPT_CMD_RESP_MULT`

```c
#define MODEM_CHAT_SCRIPT_CMD_RESP_MULT ( _request, _response_matches )
```

```c
#include <zephyr/modem/chat.h>
```

展开值（Value）：

```c
{                                                                                          \
        .request = (uint8_t *)(_request),                                                  \
        .request_size = (uint16_t)(sizeof(_request) - 1),                                  \
        .response_matches = _response_matches,                                             \
        .response_matches_size = ARRAY_SIZE(_response_matches),                            \
        .timeout = 0,                                                                      \
}
```

能够处理多个响应（Multiple Responses）的命令。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_request` | 要发送的命令字符串（Command String）。 |
| `_response_matches` | 可接受响应（Accepted Responses），由 `MODEM_CHAT_MATCHES_DEFINE` 创建。 |

<a id="ga280eec4caf2a33c24a5e2be25949e4f7"></a>

### `MODEM_CHAT_SCRIPT_CMD_RESP_MULT_COND`

```c
#define MODEM_CHAT_SCRIPT_CMD_RESP_MULT_COND ( _request, _response_matches, _run_check )
```

```c
#include <zephyr/modem/chat.h>
```

展开值（Value）：

```c
{                                                                                          \
        .request = (uint8_t *)(_request),                                                  \
        .request_size = (uint16_t)(sizeof(_request) - 1),                                  \
        .response_matches = _response_matches,                                             \
        .response_matches_size = ARRAY_SIZE(_response_matches),                            \
        .timeout = 0,                                                                      \
        .run_check = _run_check                                                            \
}
```

按条件执行、能够处理多个响应（Multiple Responses）的命令。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_request` | 要发送的命令字符串（Command String）。 |
| `_response_matches` | 可接受响应（Accepted Responses），由 `MODEM_CHAT_MATCHES_DEFINE` 创建。 |
| `_run_check` | 控制是否执行命令的回调（Callback）。 |

<a id="ga0a62af922c1ca5aed812ac634e490453"></a>

### `MODEM_CHAT_SCRIPT_CMD_RESP_NONE`

```c
#define MODEM_CHAT_SCRIPT_CMD_RESP_NONE ( _request, _timeout_ms )
```

```c
#include <zephyr/modem/chat.h>
```

展开值（Value）：

```c
{                                                                                          \
        .request = (uint8_t *)(_request),                                                  \
        .request_size = (uint16_t)(sizeof(_request) - 1),                                  \
        .response_matches = NULL,                                                          \
        .response_matches_size = 0,                                                        \
        .timeout = _timeout_ms,                                                            \
}
```

不预期收到任何响应（Response）的命令。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_request` | 要发送的命令字符串（Command String）。 |
| `_timeout_ms` | 继续执行脚本前等待的时长（Duration），以毫秒为单位。 |

<a id="ga0e3a36d28c818dc251c107f2119ef45a"></a>

### `MODEM_CHAT_SCRIPT_CMD_RESP_NONE_COND`

```c
#define MODEM_CHAT_SCRIPT_CMD_RESP_NONE_COND ( _request, _timeout_ms, _run_check )
```

```c
#include <zephyr/modem/chat.h>
```

展开值（Value）：

```c
{                                                                                          \
        .request = (uint8_t *)(_request),                                                  \
        .request_size = (uint16_t)(sizeof(_request) - 1),                                  \
        .response_matches = NULL,                                                          \
        .response_matches_size = 0,                                                        \
        .timeout = _timeout_ms,                                                            \
        .run_check = _run_check                                                            \
}
```

按条件执行、不预期收到任何响应（Response）的命令。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_request` | 要发送的命令字符串（Command String）。 |
| `_timeout_ms` | 继续执行脚本前等待的时长（Duration），以毫秒为单位。 |
| `_run_check` | 控制是否执行命令的回调（Callback）。 |

<a id="gab807fffae2007bc03a8e87ba73921888"></a>

### `MODEM_CHAT_SCRIPT_CMDS_DEFINE`

```c
#define MODEM_CHAT_SCRIPT_CMDS_DEFINE ( _sym, ... )
```

```c
#include <zephyr/modem/chat.h>
```

展开值（Value）：

```c
const static struct modem_chat_script_chat _sym[] = {__VA_ARGS__}
```

定义 static const modem_chat_script_chat 数组。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_sym` | 所创建数组的名称（Array Name）。 |
| `...` | 任意数量的 `MODEM_CHAT_SCRIPT_CMD_RESP` 及其变体宏。 |

<a id="gad15f82648a073883c5956d6b14f4e41a"></a>

### `MODEM_CHAT_SCRIPT_DEFINE`

```c
#define MODEM_CHAT_SCRIPT_DEFINE ( _sym, _script_chats, _abort_matches, _callback, _timeout_s )
```

```c
#include <zephyr/modem/chat.h>
```

展开值（Value）：

```c
const static struct modem_chat_script _sym = {                                             \
        .name = #_sym,                                                                     \
        .script_chats = _script_chats,                                                     \
        .script_chats_size = ARRAY_SIZE(_script_chats),                                    \
        .abort_matches = _abort_matches,                                                   \
        .abort_matches_size = ARRAY_SIZE(_abort_matches),                                  \
        .callback = _callback,                                                             \
        .timeout = _timeout_s,                                                             \
}
```

<a id="ga16441c0c385874a41b9ac071a67cea1c"></a>

### `MODEM_CHAT_SCRIPT_EMPTY_DEFINE`

```c
#define MODEM_CHAT_SCRIPT_EMPTY_DEFINE ( _sym)
```

```c
#include <zephyr/modem/chat.h>
```

展开值（Value）：

```c
MODEM_CHAT_SCRIPT_NO_ABORT_DEFINE(_sym, modem_chat_empty_script_chats, NULL, 0)
```

<a id="ga7be78a33341512359a1857baaa4ac915"></a>

### `MODEM_CHAT_SCRIPT_NO_ABORT_DEFINE`

```c
#define MODEM_CHAT_SCRIPT_NO_ABORT_DEFINE ( _sym, _script_chats, _callback, _timeout_s )
```

```c
#include <zephyr/modem/chat.h>
```

展开值（Value）：

```c
MODEM_CHAT_SCRIPT_DEFINE(_sym, _script_chats, modem_chat_empty_matches,                    \
                         _callback, _timeout_s)
```

<a id="gae689e92c91d414f968267e290e5246bd"></a>

### `modem_chat_match_callback`

```c
typedef void(* modem_chat_match_callback) (struct modem_chat *chat, char **argv, uint16_t argc, void *user_data)
```

```c
#include <zephyr/modem/chat.h>
```

收到匹配的交互内容（Matching Chat）时调用的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `chat` | 指向命令交互实例（Chat Instance）的指针。 |
| `argv` | 指向已解析参数数组（Parsed Arguments Array）的指针。 |
| `argc` | 已解析参数的数量；参数 0 保存精确匹配内容（Exact Match）。 |
| `user_data` | 在 `modem_chat_init()` 期间设置的用户数据（User Data），可自由使用。 |

<a id="ga372f3ffe3960a1bd3aa59a377656c262"></a>

### `modem_chat_run_check`

```c
typedef bool(* modem_chat_run_check) (void *user_data)
```

```c
#include <zephyr/modem/chat.h>
```

用于确定是否应执行交互命令（Chat Command）的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `user_data` | 在 `modem_chat_init()` 期间设置的用户数据（User Data），可自由使用。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `true` | 应执行命令交互命令（Chat Command）。 |
| `false` | 应跳过命令交互命令（Chat Command）。 |

<a id="ga1a0680c65972b58ea065b98a78095540"></a>

### `modem_chat_script_callback`

```c
typedef void(* modem_chat_script_callback) (struct modem_chat *chat, enum modem_chat_script_result result, const struct modem_chat_script_completion_info *info, void *user_data)
```

```c
#include <zephyr/modem/chat.h>
```

脚本执行（Script Execution）完成时调用的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `chat` | 指向命令交互实例（Chat Instance）的指针。 |
| `result` | 脚本执行结果（Script Execution Result）。 |
| `info` | 有关此前正在执行的脚本的附加信息（Extra Information）。 |
| `user_data` | 在 `modem_chat_init()` 期间设置的用户数据（User Data），可自由使用。 |

**说明（Note）**：注意（Note）：进入回调时，内部命令交互上下文（Chat Context）已经重置。可直接在回调中将其他异步脚本（Asynchronous Script）入队，但此时检查内部对象状态已无实际意义。应通过 `info` 获取所有信息。

<a id="ga4035be227ddec8424311575305647d3e"></a>

### `modem_chat_script_result`

```c
enum modem_chat_script_result
```

```c
#include <zephyr/modem/chat.h>
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MODEM_CHAT_SCRIPT_RESULT_SUCCESS` |  |
| `MODEM_CHAT_SCRIPT_RESULT_ABORT` |  |
| `MODEM_CHAT_SCRIPT_RESULT_TIMEOUT` |  |

<a id="ga734cb1bcbbbf5c87551b20038e0608ae"></a>

### `modem_chat_script_send_state`

```c
enum modem_chat_script_send_state
```

```c
#include <zephyr/modem/chat.h>
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MODEM_CHAT_SCRIPT_SEND_STATE_IDLE` |  |
| `MODEM_CHAT_SCRIPT_SEND_STATE_REQUEST` |  |

<a id="gaf91ae4e64113188e7049a7568a086556"></a>

### `modem_chat_attach()`

```c
int modem_chat_attach ( struct modem_chat * chat, struct modem_pipe * pipe )
```

```c
#include <zephyr/modem/chat.h>
```

将调制解调器交互实例（Modem Chat Instance）附接到管道（Pipe）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `chat` | 命令交互实例（Chat Instance）。 |
| `pipe` | 命令交互实例（Chat Instance）要附接到的管道实例（Pipe Instance）。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负 `errno` 错误码。

**说明（Note）**：注意（Note）：成功后会启用命令交互实例（Chat Instance）。

<a id="gaf79f3b0e67b5777876137b9e3e16d985"></a>

### `modem_chat_init()`

```c
int modem_chat_init ( struct modem_chat * chat, const struct modem_chat_config * config )
```

```c
#include <zephyr/modem/chat.h>
```

初始化调制解调器管道交互实例（Modem Pipe Chat Instance）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `chat` | 命令交互实例（Chat Instance）。 |
| `config` | 要应用于命令交互实例（Chat Instance）的配置（Configuration）。 |

**说明（Note）**：注意（Note）：命令交互实例（Chat Instance）必须已附接到管道（Pipe）。

<a id="ga959b05c06c113cd8107dbc71d06b0f81"></a>

### `modem_chat_is_running()`

```c
bool modem_chat_is_running ( struct modem_chat * chat)
```

```c
#include <zephyr/modem/chat.h>
```

检查脚本（Script）是否正在运行。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `chat` | 命令交互实例（Chat Instance）。 |

**返回（Returns）**：返回值（Returns）：当前有脚本运行时为 `true`，没有脚本运行时为 `false`。

<a id="ga3274b7ffcce059c4d0a5d2ccb3e0bcc6"></a>

### `modem_chat_match_enable_wildcards()`

```c
void modem_chat_match_enable_wildcards ( struct modem_chat_match * chat_match, bool enable )
```

```c
#include <zephyr/modem/chat.h>
```

设置调制解调器交互匹配项的通配符标志（Wildcards Flag）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `chat_match` | 调制解调器命令交互匹配实例（Modem Chat Match Instance）。 |
| `enable` | 启用／禁用通配符（Wildcards）。 |

<a id="ga1f41fc90f5026dc688a90567278ac175"></a>

### `modem_chat_match_init()`

```c
void modem_chat_match_init ( struct modem_chat_match * chat_match)
```

```c
#include <zephyr/modem/chat.h>
```

初始化调制解调器交互匹配项（Modem Chat Match）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `chat_match` | 调制解调器命令交互匹配实例（Modem Chat Match Instance）。 |

<a id="gafea28e13817e1daa6bb5c42514542e4e"></a>

### `modem_chat_match_set_callback()`

```c
void modem_chat_match_set_callback ( struct modem_chat_match * chat_match, modem_chat_match_callback callback )
```

```c
#include <zephyr/modem/chat.h>
```

设置调制解调器交互匹配回调（Modem Chat Match Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `chat_match` | 调制解调器命令交互匹配实例（Modem Chat Match Instance）。 |
| `callback` | 要设置的回调（Callback）。 |

<a id="gac9ed985688aeaee96adcb2b6c4285099"></a>

### `modem_chat_match_set_match()`

```c
int modem_chat_match_set_match ( struct modem_chat_match * chat_match, const char * match )
```

```c
#include <zephyr/modem/chat.h>
```

设置调制解调器交互匹配实例（Modem Chat Match Instance）的匹配内容（Match）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `chat_match` | 调制解调器命令交互匹配实例（Modem Chat Match Instance）。 |
| `match` | 要设置的匹配内容（Match）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时；否则返回负 `errno` 错误码。 |

**说明（Note）**：注意（Note）：`match` 的生命周期（Lifetime）必须不短于 `chat_match` 的生命周期。

**警告（Warning）**：警告（Warning）：修改 `match` 后，必须始终调用本 API。

<a id="ga53cb148e665095d036edc266e778a8ce"></a>

### `modem_chat_match_set_partial()`

```c
void modem_chat_match_set_partial ( struct modem_chat_match * chat_match, bool partial )
```

```c
#include <zephyr/modem/chat.h>
```

设置调制解调器交互匹配项的部分匹配标志（Partial Flag）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `chat_match` | 调制解调器命令交互匹配实例（Modem Chat Match Instance）。 |
| `partial` | 要设置的部分匹配标志（Partial Flag）。 |

<a id="ga35c1a4f9ed2677fb747025f859eeae56"></a>

### `modem_chat_match_set_separators()`

```c
int modem_chat_match_set_separators ( struct modem_chat_match * chat_match, const char * separators )
```

```c
#include <zephyr/modem/chat.h>
```

设置调制解调器交互匹配实例（Modem Chat Match Instance）的分隔符（Separators）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `chat_match` | 调制解调器命令交互匹配实例（Modem Chat Match Instance）。 |
| `separators` | 要设置的分隔符（Separators）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时；否则返回负 `errno` 错误码。 |

**说明（Note）**：注意（Note）：`separators` 的生命周期（Lifetime）必须不短于 `chat_match` 的生命周期。

**警告（Warning）**：警告（Warning）：修改 `separators` 后，必须始终调用本 API。

<a id="ga62fa275cb9ce387b0bf5b384c9448c41"></a>

### `modem_chat_release()`

```c
void modem_chat_release ( struct modem_chat * chat)
```

```c
#include <zephyr/modem/chat.h>
```

从交互实例（Chat Instance）释放管道（Pipe）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `chat` | 命令交互实例（Chat Instance）。 |

<a id="gae64d151a5f65bde1dd1973393acf3ff1"></a>

### `modem_chat_run_script()`

```c
int modem_chat_run_script ( struct modem_chat * chat, const struct modem_chat_script * script )
```

```c
#include <zephyr/modem/chat.h>
```

运行脚本（Script）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `chat` | 命令交互实例（Chat Instance）。 |
| `script` | 要运行的脚本（Script）。 |

**返回（Returns）**：返回值（Returns）：成功时为 0；已有脚本运行时为 `-EBUSY`；未附接调制解调器管道（Modem Pipe）时为 `-EPERM`；参数或脚本无效时为 `-EINVAL`。

**说明（Note）**：注意（Note）：脚本（Script）运行至完成或中止。

<a id="ga397d399703449498171ac898776fe791"></a>

### `modem_chat_run_script_async()`

```c
int modem_chat_run_script_async ( struct modem_chat * chat, const struct modem_chat_script * script )
```

```c
#include <zephyr/modem/chat.h>
```

异步运行脚本（Run Script Asynchronously）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `chat` | 命令交互实例（Chat Instance）。 |
| `script` | 要运行的脚本（Script）。 |

**返回（Returns）**：返回值（Returns）：成功启动脚本时为 0；已有脚本运行时为 `-EBUSY`；未附接调制解调器管道（Modem Pipe）时为 `-EPERM`；参数或脚本无效时为 `-EINVAL`。

**说明（Note）**：注意（Note）：脚本（Script）异步运行至完成或中止。

<a id="ga5ec3918a4beb6b30deecedbd6f6382ee"></a>

### `modem_chat_script_abort()`

```c
void modem_chat_script_abort ( struct modem_chat * chat)
```

```c
#include <zephyr/modem/chat.h>
```

中止脚本（Abort Script）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `chat` | 命令交互实例（Chat Instance）。 |

<a id="gaf12d45cf404e85c94fc13252294c76ca"></a>

### `modem_chat_script_chat_init()`

```c
void modem_chat_script_chat_init ( struct modem_chat_script_chat * script_chat)
```

```c
#include <zephyr/modem/chat.h>
```

初始化调制解调器交互脚本中的交互项（Modem Chat Script Chat）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `script_chat` | 调制解调器命令交互脚本的交互实例（Modem Chat Script Chat Instance）。 |

<a id="gadaed8cb3a0933fd15a46344ca0df9930"></a>

### `modem_chat_script_chat_set_request()`

```c
int modem_chat_script_chat_set_request ( struct modem_chat_script_chat * script_chat, const char * request )
```

```c
#include <zephyr/modem/chat.h>
```

设置调制解调器交互脚本交互项实例的请求（Request）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `script_chat` | 调制解调器命令交互脚本的交互实例（Modem Chat Script Chat Instance）。 |
| `request` | 要设置的请求（Request）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时；否则返回负 `errno` 错误码。 |

**说明（Note）**：注意（Note）：`request` 的生命周期（Lifetime）必须不短于 `script_chat` 的生命周期。

**警告（Warning）**：警告（Warning）：修改 `request` 后，必须始终调用本 API。

<a id="ga2aec485e298ebde8af0372deb9c4784f"></a>

### `modem_chat_script_chat_set_response_matches()`

```c
int modem_chat_script_chat_set_response_matches ( struct modem_chat_script_chat * script_chat, const struct modem_chat_match * response_matches, uint16_t response_matches_size )
```

```c
#include <zephyr/modem/chat.h>
```

设置调制解调器交互脚本交互项的匹配项（Matches）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `script_chat` | 调制解调器命令交互脚本的交互实例（Modem Chat Script Chat Instance）。 |
| `response_matches` | 要设置的响应匹配数组（Response Match Array）。 |
| `response_matches_size` | 响应匹配数组大小（Response Match Array Size）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时；否则返回负 `errno` 错误码。 |

**说明（Note）**：注意（Note）：`response_matches` 的生命周期（Lifetime）必须不短于 `script_chat` 的生命周期。

<a id="gae52a949df85cbcb7729c88917f46ef8d"></a>

### `modem_chat_script_chat_set_timeout()`

```c
void modem_chat_script_chat_set_timeout ( struct modem_chat_script_chat * script_chat, uint16_t timeout_ms )
```

```c
#include <zephyr/modem/chat.h>
```

设置调制解调器交互脚本交互项的超时（Timeout）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `script_chat` | 调制解调器命令交互脚本的交互实例（Modem Chat Script Chat Instance）。 |
| `timeout_ms` | 超时时间（Timeout），以毫秒为单位。 |

<a id="gafdca5529d3ae3c982f3577560216e309"></a>

### `modem_chat_script_init()`

```c
void modem_chat_script_init ( struct modem_chat_script * script)
```

```c
#include <zephyr/modem/chat.h>
```

初始化调制解调器交互脚本（Modem Chat Script）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `script` | 调制解调器命令交互脚本实例（Modem Chat Script Instance）。 |

<a id="gaa92ffb91bab15c882cff7b13fca7eeb5"></a>

### `modem_chat_script_run()`

```c
int modem_chat_script_run ( struct modem_chat * chat, const struct modem_chat_script * script )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/modem/chat.h>
```

异步运行脚本（Run Script Asynchronously）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `chat` | 命令交互实例（Chat Instance）。 |
| `script` | 要运行的脚本（Script）。 |

**说明（Note）**：注意（Note）：本函数为向后兼容（Backwards Compatibility）而保留，应予弃用（Deprecated）。

**返回（Returns）**：返回值（Returns）：成功启动脚本时为 0；已有脚本运行时为 `-EBUSY`；未附接调制解调器管道（Modem Pipe）时为 `-EPERM`；参数或脚本无效时为 `-EINVAL`。

<a id="ga9bff858315a05324ff9690bdbce7398f"></a>

### `modem_chat_script_set_abort_matches()`

```c
int modem_chat_script_set_abort_matches ( struct modem_chat_script * script, const struct modem_chat_match * abort_matches, uint16_t abort_matches_size )
```

```c
#include <zephyr/modem/chat.h>
```

设置调制解调器交互脚本的中止匹配项（Abort Matches）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `script` | 调制解调器命令交互脚本实例（Modem Chat Script Instance）。 |
| `abort_matches` | 要设置的中止匹配数组（Abort Match Array）。 |
| `abort_matches_size` | 中止匹配数组大小（Abort Match Array Size）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时；否则返回负 `errno` 错误码。 |

**说明（Note）**：注意（Note）：`abort_matches` 的生命周期（Lifetime）必须不短于 `script` 的生命周期。

<a id="ga4389d813db136c199c872f20a125eba2"></a>

### `modem_chat_script_set_callback()`

```c
void modem_chat_script_set_callback ( struct modem_chat_script * script, modem_chat_script_callback callback )
```

```c
#include <zephyr/modem/chat.h>
```

设置调制解调器交互脚本回调（Script Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `script` | 调制解调器命令交互脚本实例（Modem Chat Script Instance）。 |
| `callback` | 要设置的回调（Callback）。 |

<a id="ga9ab3fa018ee0b2ebaacb3d74ee7ce29a"></a>

### `modem_chat_script_set_name()`

```c
void modem_chat_script_set_name ( struct modem_chat_script * script, const char * name )
```

```c
#include <zephyr/modem/chat.h>
```

设置调制解调器交互脚本名称（Script Name）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `script` | 调制解调器命令交互脚本实例（Modem Chat Script Instance）。 |
| `name` | 要设置的名称（Name）。 |

**说明（Note）**：注意（Note）：`name` 的生命周期（Lifetime）必须不短于 `script` 的生命周期。

<a id="gad6b669708d24a3d3d91d1c40c2c504c8"></a>

### `modem_chat_script_set_script_chats()`

```c
int modem_chat_script_set_script_chats ( struct modem_chat_script * script, const struct modem_chat_script_chat * script_chats, uint16_t script_chats_size )
```

```c
#include <zephyr/modem/chat.h>
```

设置调制解调器交互脚本的交互项（Chats）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `script` | 调制解调器命令交互脚本实例（Modem Chat Script Instance）。 |
| `script_chats` | 要设置的命令交互脚本数组（Chat Script Array）。 |
| `script_chats_size` | 命令交互脚本数组大小（Chat Script Array Size）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时；否则返回负 `errno` 错误码。 |

**说明（Note）**：注意（Note）：`script_chats` 的生命周期（Lifetime）必须不短于 `script` 的生命周期。

<a id="ga9180fa670c3b6e88fa6011fdce5fd909"></a>

### `modem_chat_script_set_timeout()`

```c
void modem_chat_script_set_timeout ( struct modem_chat_script * script, uint32_t timeout_s )
```

```c
#include <zephyr/modem/chat.h>
```

设置调制解调器交互脚本超时（Script Timeout）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `script` | 调制解调器命令交互脚本实例（Modem Chat Script Instance）。 |
| `timeout_s` | 超时时间（Timeout），以秒为单位。 |

<a id="gada2cd7e12d9a37af6f13ecfb6c182176"></a>

### `modem_chat_any_match`

```c
const struct modem_chat_match modem_chat_any_match
```

声明属性：`extern`。

```c
#include <zephyr/modem/chat.h>
```

<a id="gac94a45b118b155ca7de1a45d12297ae4"></a>

### `modem_chat_empty_matches`

```c
const struct modem_chat_match modem_chat_empty_matches[0]
```

声明属性：`extern`。

```c
#include <zephyr/modem/chat.h>
```

<a id="ga19cd30454fb4eb9293e87b24a8cf0655"></a>

### `modem_chat_empty_script_chats`

```c
const struct modem_chat_script_chat modem_chat_empty_script_chats[0]
```

声明属性：`extern`。

```c
#include <zephyr/modem/chat.h>
```


## 7.8\_原页交叉引用（Cross References）

- [modem_chat_match](../modem_wireless_model_reference/P054_modem_chat_match_结构体.md)
- [modem_chat_script_chat](../modem_wireless_model_reference/P056_modem_chat_script_chat_结构体.md)
- [modem_chat_script_completion_info](../modem_wireless_model_reference/P057_modem_chat_script_completion_info_结构体.md)
- [modem_chat_script](../modem_wireless_model_reference/P055_modem_chat_script_结构体.md)
- [modem_chat](../modem_wireless_model_reference/P052_modem_chat_结构体.md)
- [modem_chat_config](../modem_wireless_model_reference/P053_modem_chat_config_结构体.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [zephyr/modem/chat.h](../api_file_display_chat_reference/P004_zephyr__modem__chat.h_文件参考.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [ARRAY_SIZE](../util_reference/P001_通用工具公共接口.md#ga70c57aae3eb654e205459b4362c8089a)
- [script_chats](../modem_wireless_model_reference/P055_modem_chat_script_结构体.md#a5f329ecadd721d88e423074f00005114)
- [超时（Timeout）](../modem_wireless_model_reference/P056_modem_chat_script_chat_结构体.md#a21647c746e9b2da52b7093afccf08268)
- [true](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7)
- [false](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a65e9886d74aaee76545e83dd09011727)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="agroup__modem__chat_html_ga078fd13acc9abcc0e0aa0304e6a8537a"></a>
<a id="astructmodem__chat__match_html"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="agroup__sys-util_html_ga70c57aae3eb654e205459b4362c8089a"></a>
<a id="astructmodem__chat__script__chat_html"></a>
<a id="astructmodem__chat__script__chat_html_a21647c746e9b2da52b7093afccf08268"></a>
<a id="astructmodem__chat__script_html"></a>
<a id="astructmodem__chat__script_html_a5f329ecadd721d88e423074f00005114"></a>
<a id="agroup__modem__chat_html_ga19cd30454fb4eb9293e87b24a8cf0655"></a>
<a id="agroup__modem__chat_html_ga7be78a33341512359a1857baaa4ac915"></a>
<a id="agroup__modem__chat_html_gac94a45b118b155ca7de1a45d12297ae4"></a>
<a id="agroup__modem__chat_html_gad15f82648a073883c5956d6b14f4e41a"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga4035be227ddec8424311575305647d3ea977c97fa42b7fb38d337062984b0deee"></a>
<a id="gga4035be227ddec8424311575305647d3eacddc6a743055b7c49fac484442dda31b"></a>
<a id="gga4035be227ddec8424311575305647d3ea4991b2748978d1219923d275a42c575e"></a>
<a id="gga734cb1bcbbbf5c87551b20038e0608aea8971f4f05275f31d255f4a5c7dd47974"></a>
<a id="gga734cb1bcbbbf5c87551b20038e0608aea14824a0ffb464bf00a8aadcf4c8bdbbd"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>
<a id="doc-var-members"></a>
<a id="header-doc-var-members"></a>

---

[上一章](P006_SMP 传输（SMP transport）.md) · [返回大纲](大纲.md) · [下一章](P008_实时传输协议（Real-time Transport Protocol，RTP）.md)

---
id: learning.zephyr-docs.shell-ssh-reference.page-3
title: Shell_SSH头文件源码
kind: reference
status: maintained
domains: [zephyr, kernel, source, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/shell__ssh_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_Shell\_SSH头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/shell__ssh_8h_source.html)。读取日期：2026-10-15；摘要见[来源记录](../SOURCES.md)。

本页保留官方Doxygen源码浏览页的全部可见代码及注释，移除展示行号、还原不换行空格并清除行尾空白。代码、标识符与许可证不翻译替换，中文对照列在后面。原网页隐藏了部分API文档注释，所以原始行号会跳跃；相关页面见[头文件参考](P002_Shell_SSH头文件参考.md)和[公共接口](P001_Shell_SSH后端接口.md)；访问语义和生命周期见本页译注。

## 3.1\_原始可见代码（Source Code）

原始行号锚点保留在对应代码行，使用Markdown内嵌HTML预格式代码容器承载。

<a id="foldopen00043"></a>
<a id="foldopen00056"></a>
<a id="foldopen00090"></a>
<a id="foldopen00100"></a>
<a id="agroup__shell__api_html_ga265807c2d8eba7b9ea633968627e085d"></a>
<a id="agroup__shell__ssh_html_gae0437a2655471cad3608a9f82e6cb239"></a>
<a id="anet_2socket_8h_html"></a>
<a id="ashell_2shell_8h_html"></a>
<a id="assh_2server_8h_html"></a>
<a id="astructshell__ssh__context_html"></a>
<a id="astructshell__ssh__context_html_a28b05473d9d45f699b8ec310fb0433f6"></a>
<a id="astructshell__ssh__context_html_a6def2564fe322935e757a450564caab6"></a>
<a id="astructshell__ssh__context_html_a8ed84276247f827d8a577b3e4723490b"></a>
<a id="astructshell__ssh__context_html_a98b995de48367e233f8df075db07c01b"></a>
<a id="astructshell__ssh__context_html_aa631cab0b48ebf311472e23aded0c074"></a>
<a id="astructshell__ssh__context_html_ad1846f871029db1640789cf51c116903"></a>
<a id="astructshell__ssh__context_html_adc0068e62576bd921459a3a826a1db84"></a>
<a id="astructshell__ssh__passwd_html"></a>
<a id="astructshell__ssh__passwd_html_a2354d4ecb613b35744681f1d8aa30c5a"></a>
<a id="astructshell__ssh__passwd_html_a64c4777913be1fceb42a576b8c3643af"></a>
<a id="astructshell__ssh_html"></a>
<a id="astructshell__ssh_html_a40e55fed76688fef7eff90723d4ec9a6"></a>
<a id="astructshell__ssh_html_a49e85e3b63c7cb9b2ff980bd1ae22900"></a>
<a id="astructshell__ssh_html_a85a5190e0d9692c534d5cfa9c18ffad0"></a>
<a id="astructshell__ssh_html_aa2ce6774c72acb5d49fc76ef54e6da07"></a>
<a id="astructshell__transport__api_html"></a>
<a id="astructshell_html"></a>
<a id="astructssh__server__event_html"></a>
<a id="astructssh__transport__event_html"></a>

<pre><code class="language-c"><a id="l00001"></a>/*
<a id="l00002"></a> * Copyright (c) 2024 Grant Ramsay &lt;grant.ramsay@hotmail.com&gt;
<a id="l00003"></a> * Copyright (c) 2026 Nordic Semiconductor ASA
<a id="l00004"></a> *
<a id="l00005"></a> * SPDX-License-Identifier: Apache-2.0
<a id="l00006"></a> */
<a id="l00007"></a>
<a id="l00013"></a>
<a id="l00014"></a>#ifndef ZEPHYR_INCLUDE_SHELL_SHELL_SSH_H_
<a id="l00015"></a>#define ZEPHYR_INCLUDE_SHELL_SHELL_SSH_H_
<a id="l00016"></a>
<a id="l00017"></a>#include &lt;zephyr/net/socket.h&gt;
<a id="l00018"></a>#include &lt;zephyr/net/ssh/server.h&gt;
<a id="l00019"></a>#include &lt;zephyr/shell/shell.h&gt;
<a id="l00020"></a>
<a id="l00021"></a>#ifdef __cplusplus
<a id="l00022"></a>extern "C" {
<a id="l00023"></a>#endif
<a id="l00024"></a>
<a id="l00031"></a>
<a id="l00033"></a>#define SHELL_SSH_MAX_PASSWORD_LEN 32
<a id="l00034"></a>
<a id="l00036"></a>
<a id="l00037"></a>struct ssh_channel;
<a id="l00038"></a>struct shell_ssh;
<a id="l00039"></a>
<a id="l00041"></a>
<a id="l00043"></a>struct shell_ssh_passwd {
<a id="l00045"></a>        char buf[SHELL_SSH_MAX_PASSWORD_LEN + 1];
<a id="l00047"></a>        size_t len;
<a id="l00048"></a>};
<a id="l00049"></a>
<a id="l00056"></a>struct shell_ssh_context {
<a id="l00058"></a>        const struct shell *sh;
<a id="l00060"></a>        struct shell_ssh *ssh;
<a id="l00062"></a>        struct ssh_channel *channel;
<a id="l00064"></a>        struct ssh_transport *transport;
<a id="l00066"></a>        struct shell_ssh_passwd password;
<a id="l00068"></a>        int ssh_instance;
<a id="l00070"></a>        bool in_use;
<a id="l00071"></a>};
<a id="l00072"></a>
<a id="l00074"></a>extern const struct shell_transport_api shell_ssh_transport_api;
<a id="l00076"></a>
<a id="l00078"></a>#define SHELL_SSH_GET_NAME(_name) _name##_shell_ssh
<a id="l00079"></a>
<a id="l00090"></a>#define SHELL_SSH_DEFINE(_name)                                 \
<a id="l00091"></a>        static struct shell_ssh SHELL_SSH_GET_NAME(_name);      \
<a id="l00092"></a>        static struct shell_transport _name = {                 \
<a id="l00093"></a>                .api = &amp;shell_ssh_transport_api,                \
<a id="l00094"></a>                .ctx = &amp;_name##_shell_ssh,                      \
<a id="l00095"></a>        }
<a id="l00096"></a>
<a id="l00100"></a>struct shell_ssh {
<a id="l00102"></a>        shell_transport_handler_t handler;
<a id="l00104"></a>        struct ssh_channel *ssh_channel;
<a id="l00106"></a>        void *context;
<a id="l00108"></a>        bool in_use;
<a id="l00109"></a>};
<a id="l00110"></a>
<a id="l00112"></a>
<a id="l00113"></a>#if defined(CONFIG_SSH_SERVER)
<a id="l00114"></a>int shell_sshd_event_callback(struct ssh_server *ssh_server,
<a id="l00115"></a>                              const struct ssh_server_event *event,
<a id="l00116"></a>                              void *user_data);
<a id="l00117"></a>int shell_sshd_transport_event_callback(struct ssh_transport *transport,
<a id="l00118"></a>                                        const struct ssh_transport_event *event,
<a id="l00119"></a>                                        void *user_data);
<a id="l00120"></a>#endif /* CONFIG_SSH_SERVER */
<a id="l00121"></a>
<a id="l00123"></a>
<a id="l00125"></a>
<a id="l00126"></a>#ifdef __cplusplus
<a id="l00127"></a>}
<a id="l00128"></a>#endif
<a id="l00129"></a>
<a id="l00130"></a>#endif /* ZEPHYR_INCLUDE_SHELL_SHELL_SSH_H_ */
</code></pre>

## 3.2\_可见注释译文（Comments）

1. 版权与许可证：Copyright (c) 2024 Grant Ramsay <grant.ramsay@hotmail.com>；Copyright (c) 2026 Nordic Semiconductor ASA；SPDX-License-Identifier: Apache-2.0。原始法律声明保留。

2. CONFIG_SSH_SERVER条件编译结束标记。

3. ZEPHYR_INCLUDE_SHELL_SHELL_SSH_H_头文件包含保护结束。

## 3.3\_原页符号提示（Symbol Descriptions）

### `shell_transport_handler_t`

```c
void(* shell_transport_handler_t)(enum shell_transport_evt evt, void *context)
```

Shell传输事件处理回调（Transport Event Handler Callback）。

定义位置（Definition）：shell.h:831。

符号定位：[shell_transport_handler_t](../shell_core_reference/P001_Shell核心接口.md#ga265807c2d8eba7b9ea633968627e085d)。

### `SHELL_SSH_MAX_PASSWORD_LEN`

```c
#define SHELL_SSH_MAX_PASSWORD_LEN
```

Shell SSH传输支持的最大口令长度（Maximum Password Length）。

定义位置（Definition）：shell_ssh.h:33。

符号定位：[SHELL_SSH_MAX_PASSWORD_LEN](P001_Shell_SSH后端接口.md#gae0437a2655471cad3608a9f82e6cb239)。

### `socket.h`

兼容BSD套接字（BSD Sockets）的API定义。

符号定位：[socket.h](https://docs.zephyrproject.org/latest/doxygen/html/net_2socket_8h.html)。

### `shell.h`

Shell子系统（Shell Subsystem）的头文件。

符号定位：[shell.h](../shell_core_reference/P002_Shell核心头文件参考.md)。

### `server.h`

SSH服务器API（SSH Server API）。

符号定位：[server.h](https://docs.zephyrproject.org/latest/doxygen/html/ssh_2server_8h.html)。

### `shell_ssh_context`

SSH传输用户数据（Transport User Data）。

定义位置（Definition）：shell_ssh.h:56。

符号定位：[shell_ssh_context](P005_Shell_SSH上下文结构.md)。

### `shell_ssh_context::ssh_instance`

```c
int ssh_instance
```

SSH连接实例（Connection Instance），可以是客户端或服务器。

定义位置（Definition）：shell_ssh.h:68。

符号定位：[shell_ssh_context::ssh_instance](P005_Shell_SSH上下文结构.md#a28b05473d9d45f699b8ec310fb0433f6)。

### `shell_ssh_context::ssh`

```c
struct shell_ssh * ssh
```

Shell SSH传输API（Transport API）。

定义位置（Definition）：shell_ssh.h:60。

符号定位：[shell_ssh_context::ssh](P005_Shell_SSH上下文结构.md#a6def2564fe322935e757a450564caab6)。

### `shell_ssh_context::in_use`

```c
bool in_use
```

此上下文是否正在使用，用于服务器端池跟踪（Server-side Pool Tracking）。

定义位置（Definition）：shell_ssh.h:70。

符号定位：[shell_ssh_context::in_use](P005_Shell_SSH上下文结构.md#a8ed84276247f827d8a577b3e4723490b)。

### `shell_ssh_context::transport`

```c
struct ssh_transport * transport
```

与此用户数据关联的SSH传输（SSH Transport）。

定义位置（Definition）：shell_ssh.h:64。

符号定位：[shell_ssh_context::transport](P005_Shell_SSH上下文结构.md#a98b995de48367e233f8df075db07c01b)。

### `shell_ssh_context::channel`

```c
struct ssh_channel * channel
```

与此传输关联的SSH通道（SSH Channel）。

定义位置（Definition）：shell_ssh.h:62。

符号定位：[shell_ssh_context::channel](P005_Shell_SSH上下文结构.md#aa631cab0b48ebf311472e23aded0c074)。

### `shell_ssh_context::sh`

```c
const struct shell * sh
```

与此传输关联的Shell实例（Shell Instance）。

定义位置（Definition）：shell_ssh.h:58。

符号定位：[shell_ssh_context::sh](P005_Shell_SSH上下文结构.md#ad1846f871029db1640789cf51c116903)。

### `shell_ssh_context::password`

```c
struct shell_ssh_passwd password
```

SSH服务器口令存储（Server Password Storage）。

定义位置（Definition）：shell_ssh.h:66。

符号定位：[shell_ssh_context::password](P005_Shell_SSH上下文结构.md#adc0068e62576bd921459a3a826a1db84)。

### `shell_ssh_passwd`

SSH口令存储（Password Storage）。

定义位置（Definition）：shell_ssh.h:43。

符号定位：[shell_ssh_passwd](P006_Shell_SSH口令结构.md)。

### `shell_ssh_passwd::len`

```c
size_t len
```

缓冲区中存储的口令长度（Password Length）。

定义位置（Definition）：shell_ssh.h:47。

符号定位：[shell_ssh_passwd::len](P006_Shell_SSH口令结构.md#a2354d4ecb613b35744681f1d8aa30c5a)。

### `shell_ssh_passwd::buf`

```c
char buf[32+1]
```

保存口令的缓冲区（Password Buffer）。

定义位置（Definition）：shell_ssh.h:45。

符号定位：[shell_ssh_passwd::buf](P006_Shell_SSH口令结构.md#a64c4777913be1fceb42a576b8c3643af)。

### `shell_ssh`

SSH传输API（Transport API）。

定义位置（Definition）：shell_ssh.h:100。

符号定位：[shell_ssh](P004_Shell_SSH传输结构.md)。

### `shell_ssh::context`

```c
void * context
```

传输上下文（Transport Context）。

定义位置（Definition）：shell_ssh.h:106。

符号定位：[shell_ssh::context](P004_Shell_SSH传输结构.md#a40e55fed76688fef7eff90723d4ec9a6)。

### `shell_ssh::ssh_channel`

```c
struct ssh_channel * ssh_channel
```

SSH通道（SSH Channel）。

定义位置（Definition）：shell_ssh.h:104。

符号定位：[shell_ssh::ssh_channel](P004_Shell_SSH传输结构.md#a49e85e3b63c7cb9b2ff980bd1ae22900)。

### `shell_ssh::handler`

```c
shell_transport_handler_t handler
```

传输处理函数（Transport Handler）。

定义位置（Definition）：shell_ssh.h:102。

符号定位：[shell_ssh::handler](P004_Shell_SSH传输结构.md#a85a5190e0d9692c534d5cfa9c18ffad0)。

### `shell_ssh::in_use`

```c
bool in_use
```

此传输是否正在使用（In Use）。

定义位置（Definition）：shell_ssh.h:108。

符号定位：[shell_ssh::in_use](P004_Shell_SSH传输结构.md#aa2ce6774c72acb5d49fc76ef54e6da07)。

### `shell_transport_api`

统一的Shell传输接口（Transport Interface）。

定义位置（Definition）：shell.h:864。

符号定位：[shell_transport_api](../shell_core_reference/P010_Shell传输接口结构.md)。

### `shell`

Shell实例内部结构（Instance Internals）。

定义位置（Definition）：shell.h:1129。

符号定位：[shell](../shell_core_reference/P004_Shell实例结构.md)。

### `ssh_server_event`

SSH服务器事件（SSH Server Event）。

定义位置（Definition）：server.h:64。

符号定位：[ssh_server_event](https://docs.zephyrproject.org/latest/doxygen/html/structssh__server__event.html)。

### `ssh_transport_event`

SSH传输事件信息（Transport Event Information）。

定义位置（Definition）：common.h:164。

符号定位：[ssh_transport_event](https://docs.zephyrproject.org/latest/doxygen/html/structssh__transport__event.html)。

## 3.4\_源码跟踪译注

> 译注——SHELL_SSH_DEFINE创建SSH传输对象与静态上下文，需要与SHELL_DEFINE配合构造Shell实例。宏定义本身不建立网络连接，也不代表一个已认证的SSH会话。

> 译注——shell_ssh的in_use标志和shell_ssh_context的in_use标志分别用于Shell实例与服务器上下文池的占用跟踪。当前实现通过互斥锁（Mutex）保护分配和归还；不能把字段值当作对网络连通性的独立检测。

> 译注——SHELL_SSH_MAX_PASSWORD_LEN为32，buf数组容量为该值加1。结构另外保存size_t类型的len。字段仅描述存储布局，不能由此推断口令校验、编码或完整的认证策略。

> 译注——官方结构描述允许ssh_instance表示客户端或服务器连接；所核对实现中的服务器上下文池和事件回调受CONFIG_SSH_SERVER控制。字段的通用描述不表示所有配置都会构造服务器对象。

头文件定位：[include/zephyr/shell/shell_ssh.h](../../../include/zephyr/shell/shell_ssh.h)，关联实现／接口：[subsys/shell/backends/shell_ssh.c](../../../subsys/shell/backends/shell_ssh.c)；[官方原始头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/shell/shell_ssh.h)与[官方关联文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/shell_ssh.c)的摘要见来源记录。去掉注释和展示空白后，本页代码与本次读取的原始头文件一致，不能推广到以后滚动更新的main或任意本地版本。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 3.5\_原页交叉引用（Cross References）

- [查看此文件参考说明](P002_Shell_SSH头文件参考.md)
- [zephyr/net/socket.h](https://docs.zephyrproject.org/latest/doxygen/html/net_2socket_8h.html)
- [zephyr/net/ssh/server.h](https://docs.zephyrproject.org/latest/doxygen/html/ssh_2server_8h.html)
- [zephyr/shell/shell.h](../shell_core_reference/P002_Shell核心头文件参考.md)
- [shell_ssh](P004_Shell_SSH传输结构.md)
- [shell_ssh_passwd](P006_Shell_SSH口令结构.md)
- [buf](P006_Shell_SSH口令结构.md#a64c4777913be1fceb42a576b8c3643af)
- [SHELL_SSH_MAX_PASSWORD_LEN](P001_Shell_SSH后端接口.md#gae0437a2655471cad3608a9f82e6cb239)
- [len](P006_Shell_SSH口令结构.md#a2354d4ecb613b35744681f1d8aa30c5a)
- [shell_ssh_context](P005_Shell_SSH上下文结构.md)
- [shell](../shell_core_reference/P004_Shell实例结构.md)
- [sh](P005_Shell_SSH上下文结构.md#ad1846f871029db1640789cf51c116903)
- [ssh](P005_Shell_SSH上下文结构.md#a6def2564fe322935e757a450564caab6)
- [channel](P005_Shell_SSH上下文结构.md#aa631cab0b48ebf311472e23aded0c074)
- [transport](P005_Shell_SSH上下文结构.md#a98b995de48367e233f8df075db07c01b)
- [password](P005_Shell_SSH上下文结构.md#adc0068e62576bd921459a3a826a1db84)
- [ssh_instance](P005_Shell_SSH上下文结构.md#a28b05473d9d45f699b8ec310fb0433f6)
- [in_use](P005_Shell_SSH上下文结构.md#a8ed84276247f827d8a577b3e4723490b)
- [shell_transport_api](../shell_core_reference/P010_Shell传输接口结构.md)
- [shell_transport_handler_t](../shell_core_reference/P001_Shell核心接口.md#ga265807c2d8eba7b9ea633968627e085d)
- [handler](P004_Shell_SSH传输结构.md#a85a5190e0d9692c534d5cfa9c18ffad0)
- [ssh_channel](P004_Shell_SSH传输结构.md#a49e85e3b63c7cb9b2ff980bd1ae22900)
- [context](P004_Shell_SSH传输结构.md#a40e55fed76688fef7eff90723d4ec9a6)
- [in_use](P004_Shell_SSH传输结构.md#aa2ce6774c72acb5d49fc76ef54e6da07)
- [ssh_server_event](https://docs.zephyrproject.org/latest/doxygen/html/structssh__server__event.html)
- [ssh_transport_event](https://docs.zephyrproject.org/latest/doxygen/html/structssh__transport__event.html)

---

[上一章](P002_Shell_SSH头文件参考.md) · [返回大纲](大纲.md) · [下一章](P004_Shell_SSH传输结构.md)

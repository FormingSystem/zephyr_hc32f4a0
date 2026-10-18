---
id: learning.zephyr-docs.shell-remote-reference.page-3
title: 远端Shell头文件源码
kind: reference
status: maintained
domains: [zephyr, kernel, source, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/shell__remote_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_远端Shell头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/shell__remote_8h_source.html)。读取日期：2026-10-15；摘要见[来源记录](../SOURCES.md)。

本页保留官方Doxygen源码浏览页的全部可见代码及注释，移除展示行号、还原不换行空格并清除行尾空白。代码、标识符与许可证不翻译替换，中文对照列在后面。原网页隐藏了部分API文档注释，所以原始行号会跳跃；相关页面见[头文件参考](P002_远端Shell头文件参考.md)和[公共接口](P001_远端Shell接口.md)；访问语义和生命周期见本页译注。

## 3.1\_原始可见代码（Source Code）

原始行号锚点保留在对应代码行，使用Markdown内嵌HTML预格式代码容器承载。

<a id="foldopen00039"></a>
<a id="foldopen00051"></a>
<a id="foldopen00084"></a>
<a id="foldopen00100"></a>
<a id="agroup__ft8xx__reference__api_html_gacde1ca3945cbe6c828f65051c5c3a615"></a>
<a id="agroup__shell__remote_html_ga0644f6ba7da5eb5bd4952d3afa6ff536"></a>
<a id="agroup__shell__remote_html_ga63fce1cfe8b08c710fafa5cbc8e28a13"></a>
<a id="agroup__shell__remote_html_ga834254727aeba7c1e29cc1e6df22f23f"></a>
<a id="aipc__service_8h_html"></a>
<a id="ashell_2shell_8h_html"></a>
<a id="ashell__remote__common_8h_html"></a>
<a id="aslist_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructdevice_html"></a>
<a id="astructipc__ept__cfg_html"></a>
<a id="astructipc__ept_html"></a>
<a id="astructk__sem_html"></a>
<a id="astructk__work_html"></a>
<a id="astructshell__remote__cmd_html"></a>
<a id="astructshell__remote__cmd_html_a10d9f55e316984f5c5e1d89ce112b7ec"></a>
<a id="astructshell__remote__cmd_html_a6563d0ec7c942d974802759b4f5f506f"></a>
<a id="astructshell__remote__cmd_html_a7a7817a33d740d6b458338f551eb5328"></a>
<a id="astructshell__remote__data_html"></a>
<a id="astructshell__remote__data_html_a098d8b3da108972c75aae512527ee96d"></a>
<a id="astructshell__remote__data_html_a129256b9fd61a17027362874bae8c87d"></a>
<a id="astructshell__remote__data_html_a1b411b2f856385e08fc7e915f1ac88da"></a>
<a id="astructshell__remote__data_html_a76fa224ff7b9e121318c5ed2acccd2f8"></a>
<a id="astructshell__remote__data_html_a97b2cb413dc24aa511e9e7673d031103"></a>
<a id="astructshell__remote__data_html_ab1bade0da8e552b492c0f10448bdf6d6"></a>
<a id="astructshell__remote__data_html_ac5bfd07b113aa7a79eb0bfe9f361db48"></a>
<a id="astructshell__remote__data_html_ad007967f92725925d2b66b27bb5e548d"></a>
<a id="astructshell__remote__data_html_ad0cb7d3a07ad5590a86f559328fed338"></a>
<a id="astructshell__remote__data_html_af8872d013a80afeba1201dc82892437e"></a>
<a id="astructshell__remote_html"></a>
<a id="astructshell__remote_html_a599061c03ce6e626e57d91be5100783b"></a>
<a id="astructshell__remote_html_aa815345346bb54a610b8422232e78106"></a>
<a id="astructshell__remote_html_abc23c07899d59c1b942a6e50b814b8b1"></a>
<a id="astructshell__static__entry_html"></a>
<a id="astructshell_html"></a>

<pre><code class="language-c"><a id="l00001"></a>/*
<a id="l00002"></a> * Copyright (c) 2026 Nordic Semiconductor ASA
<a id="l00003"></a> *
<a id="l00004"></a> * SPDX-License-Identifier: Apache-2.0
<a id="l00005"></a> */
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00013"></a>
<a id="l00014"></a>#ifndef ZEPHYR_INCLUDE_SHELL_SHELL_REMOTE_H_
<a id="l00015"></a>#define ZEPHYR_INCLUDE_SHELL_SHELL_REMOTE_H_
<a id="l00016"></a>
<a id="l00023"></a>
<a id="l00024"></a>#include &lt;zephyr/shell/shell_remote_common.h&gt;
<a id="l00025"></a>#include &lt;zephyr/shell/shell.h&gt;
<a id="l00026"></a>#include &lt;zephyr/ipc/ipc_service.h&gt;
<a id="l00027"></a>#include &lt;zephyr/sys/slist.h&gt;
<a id="l00028"></a>
<a id="l00029"></a>#ifdef __cplusplus
<a id="l00030"></a>extern "C" {
<a id="l00031"></a>#endif
<a id="l00032"></a>
<a id="l00033"></a>#ifndef CONFIG_SHELL_REMOTE_TMP_BUF_SIZE
<a id="l00035"></a>#define CONFIG_SHELL_REMOTE_TMP_BUF_SIZE 128
<a id="l00036"></a>#endif
<a id="l00037"></a>
<a id="l00039"></a>struct shell_remote_cmd {
<a id="l00041"></a>        struct shell_static_entry cmd;
<a id="l00042"></a>
<a id="l00044"></a>        const struct shell_static_entry *rem_cmd;
<a id="l00045"></a>
<a id="l00047"></a>        char tmp_buf[CONFIG_SHELL_REMOTE_TMP_BUF_SIZE];
<a id="l00048"></a>};
<a id="l00049"></a>
<a id="l00051"></a>struct shell_remote_data {
<a id="l00053"></a>        struct ipc_ept ept;
<a id="l00054"></a>
<a id="l00056"></a>        struct k_sem sem;
<a id="l00057"></a>
<a id="l00059"></a>        struct k_work work;
<a id="l00060"></a>
<a id="l00062"></a>        const struct shell *sh;
<a id="l00063"></a>
<a id="l00065"></a>        struct shell_remote_cmd cmds[2];
<a id="l00066"></a>
<a id="l00068"></a>        struct shell_remote_cmd *current_cmd;
<a id="l00069"></a>
<a id="l00071"></a>        int result;
<a id="l00072"></a>
<a id="l00074"></a>        size_t msg_len;
<a id="l00075"></a>
<a id="l00077"></a>        void *msg;
<a id="l00078"></a>
<a id="l00080"></a>        bool ready;
<a id="l00081"></a>};
<a id="l00082"></a>
<a id="l00084"></a>struct shell_remote {
<a id="l00086"></a>        const char *name;
<a id="l00087"></a>
<a id="l00089"></a>        const struct device *ipc;
<a id="l00090"></a>
<a id="l00092"></a>        struct ipc_ept_cfg ep_cfg;
<a id="l00093"></a>};
<a id="l00094"></a>
<a id="l00100"></a>#define SHELL_REMOTE_CONN(_name, ipc_node)                                                         \
<a id="l00101"></a>        static struct shell_remote_data shell_remote_data_##_name;                                 \
<a id="l00102"></a>        static const STRUCT_SECTION_ITERABLE(shell_remote, _name) = {                              \
<a id="l00103"></a>                .name = STRINGIFY(_name), .ipc = DEVICE_DT_GET(ipc_node),                          \
<a id="l00104"></a>                                  .ep_cfg = {.name = CONFIG_SHELL_REMOTE_EP_NAME,                  \
<a id="l00105"></a>                                             .cb =                                                 \
<a id="l00106"></a>                                                     {                                             \
<a id="l00107"></a>                                                             .bound = shell_remote_ep_bound,       \
<a id="l00108"></a>                                                             .received = shell_remote_ep_recv,     \
<a id="l00109"></a>                                                     },                                            \
<a id="l00110"></a>                                             .priv = &amp;shell_remote_data_##_name}}
<a id="l00111"></a>
<a id="l00120"></a>const struct shell_static_entry *z_shell_remote_cmd_get(const struct shell_static_entry *parent,
<a id="l00121"></a>                                                        size_t idx,
<a id="l00122"></a>                                                        struct shell_static_entry *dloc);
<a id="l00123"></a>
<a id="l00134"></a>int z_shell_remote_cmd_exec(const struct shell *shell, const struct shell_static_entry *cmd,
<a id="l00135"></a>                            uint8_t argc, const char **argv, size_t cmd_lvl);
<a id="l00136"></a>
<a id="l00141"></a>void shell_remote_ep_bound(void *priv);
<a id="l00142"></a>
<a id="l00149"></a>void shell_remote_ep_recv(const void *data, size_t len, void *priv);
<a id="l00150"></a>
<a id="l00152"></a>
<a id="l00153"></a>#ifdef __cplusplus
<a id="l00154"></a>}
<a id="l00155"></a>#endif
<a id="l00156"></a>
<a id="l00157"></a>#endif /* ZEPHYR_INCLUDE_SHELL_SHELL_REMOTE_H_ */
</code></pre>

## 3.2\_可见注释译文（Comments）

1. 版权与许可证：Copyright (c) 2026 Nordic Semiconductor ASA；SPDX-License-Identifier: Apache-2.0。原始法律声明保留。

2. ZEPHYR_INCLUDE_SHELL_SHELL_REMOTE_H_头文件包含保护结束。

## 3.3\_原页符号提示（Symbol Descriptions）

### `cmd`

```c
static void cmd(uint32_t command)
```

通过协处理器引擎（Co-processor Engine）执行显示列表命令（Display List Command）。（保留原网页自动关联的符号提示；这不是远端Shell的功能说明。）

定义位置（Definition）：ft8xx_reference_api.h:153。

符号定位：[cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)。

### `CONFIG_SHELL_REMOTE_TMP_BUF_SIZE`

```c
#define CONFIG_SHELL_REMOTE_TMP_BUF_SIZE
```

远端Shell命令数据临时缓冲区（Temporary Buffer）的默认大小。

定义位置（Definition）：shell_remote.h:35。

符号定位：[CONFIG_SHELL_REMOTE_TMP_BUF_SIZE](P001_远端Shell接口.md#ga0644f6ba7da5eb5bd4952d3afa6ff536)。

### `shell_remote_ep_bound`

```c
void shell_remote_ep_bound(void *priv)
```

处理远端Shell实例绑定事件（Bound Event）的回调函数。

符号定位：[shell_remote_ep_bound](P001_远端Shell接口.md#ga63fce1cfe8b08c710fafa5cbc8e28a13)。

### `shell_remote_ep_recv`

```c
void shell_remote_ep_recv(const void *data, size_t len, void *priv)
```

处理远端Shell实例接收事件（Received Event）的回调函数。

符号定位：[shell_remote_ep_recv](P001_远端Shell接口.md#ga834254727aeba7c1e29cc1e6df22f23f)。

### `ipc_service.h`

符号定位：[ipc_service.h](../intercore_reference/P117_IPC服务头文件参考.md)。

### `shell.h`

Shell子系统（Shell Subsystem）的头文件。

符号定位：[shell.h](../shell_core_reference/P002_Shell核心头文件参考.md)。

### `shell_remote_common.h`

远端Shell的公共API（Common APIs）。

符号定位：[shell_remote_common.h](P006_远端Shell公共头文件参考.md)。

### `slist.h`

单向链表（Singly-linked List）API的头文件。

符号定位：[slist.h](../slist_reference/P002_单向链表头文件参考.md)。

### `uint8_t`

```c
__UINT8_TYPE__ uint8_t
```

定义位置（Definition）：stdint.h:88。

符号定位：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

### `device`

每个驱动实例的运行时设备结构（Runtime Device Structure），位于ROM中。

定义位置（Definition）：device.h:543。

符号定位：[device](../device_reference/P002_设备对象结构.md)。

### `ipc_ept_cfg`

端点配置结构（Endpoint Configuration Structure）。

定义位置（Definition）：ipc_service.h:208。

符号定位：[ipc_ept_cfg](../intercore_reference/P114_IPC服务端点配置.md)。

### `ipc_ept`

端点实例（Endpoint Instance）。

定义位置（Definition）：ipc_service.h:198。

符号定位：[ipc_ept](../intercore_reference/P113_IPC服务端点结构.md)。

### `k_sem`

信号量结构（Semaphore Structure）。

定义位置（Definition）：kernel.h:3738。

符号定位：[k_sem](../synchronization_reference/P009_内核信号量结构.md)。

### `k_work`

用于提交工作（Work）的结构。

定义位置（Definition）：kernel.h:4649。

符号定位：[k_work](https://docs.zephyrproject.org/latest/doxygen/html/structk__work.html)。

### `shell_remote_cmd`

用于存储远端Shell命令数据的结构（Command Data Structure）。

定义位置（Definition）：shell_remote.h:39。

符号定位：[shell_remote_cmd](P009_远端Shell命令.md)。

### `shell_remote_cmd::cmd`

```c
struct shell_static_entry cmd
```

命令条目（Command Entry）。

定义位置（Definition）：shell_remote.h:41。

符号定位：[shell_remote_cmd::cmd](P009_远端Shell命令.md#a10d9f55e316984f5c5e1d89ce112b7ec)。

### `shell_remote_cmd::tmp_buf`

```c
char tmp_buf[128]
```

用于命令语法和帮助文本的临时缓冲区（Temporary Buffer）。

定义位置（Definition）：shell_remote.h:47。

符号定位：[shell_remote_cmd::tmp_buf](P009_远端Shell命令.md#a6563d0ec7c942d974802759b4f5f506f)。

### `shell_remote_cmd::rem_cmd`

```c
const struct shell_static_entry * rem_cmd
```

父级远端命令（Parent Remote Command）的指针。

定义位置（Definition）：shell_remote.h:44。

符号定位：[shell_remote_cmd::rem_cmd](P009_远端Shell命令.md#a7a7817a33d740d6b458338f551eb5328)。

### `shell_remote_data`

用于存储远端Shell实例数据的结构（Instance Data Structure）。

定义位置（Definition）：shell_remote.h:51。

符号定位：[shell_remote_data](P010_远端Shell运行数据.md)。

### `shell_remote_data::current_cmd`

```c
struct shell_remote_cmd * current_cmd
```

当前命令（Current Command）的指针。

定义位置（Definition）：shell_remote.h:68。

符号定位：[shell_remote_data::current_cmd](P010_远端Shell运行数据.md#a098d8b3da108972c75aae512527ee96d)。

### `shell_remote_data::msg_len`

```c
size_t msg_len
```

打印消息长度（Print Message Length）。

定义位置（Definition）：shell_remote.h:74。

符号定位：[shell_remote_data::msg_len](P010_远端Shell运行数据.md#a129256b9fd61a17027362874bae8c87d)。

### `shell_remote_data::ept`

```c
struct ipc_ept ept
```

IPC端点（Endpoint）。

定义位置（Definition）：shell_remote.h:53。

符号定位：[shell_remote_data::ept](P010_远端Shell运行数据.md#a1b411b2f856385e08fc7e915f1ac88da)。

### `shell_remote_data::ready`

```c
bool ready
```

表示远端Shell实例已就绪、已绑定（Bound）的标志；原文括号中写作bounded。

定义位置（Definition）：shell_remote.h:80。

符号定位：[shell_remote_data::ready](P010_远端Shell运行数据.md#a76fa224ff7b9e121318c5ed2acccd2f8)。

### `shell_remote_data::sh`

```c
const struct shell * sh
```

Shell实例指针。

定义位置（Definition）：shell_remote.h:62。

符号定位：[shell_remote_data::sh](P010_远端Shell运行数据.md#a97b2cb413dc24aa511e9e7673d031103)。

### `shell_remote_data::work`

```c
struct k_work work
```

处理打印消息的工作队列（Work Queue）。

定义位置（Definition）：shell_remote.h:59。

符号定位：[shell_remote_data::work](P010_远端Shell运行数据.md#ab1bade0da8e552b492c0f10448bdf6d6)。

### `shell_remote_data::result`

```c
int result
```

上次命令的结果（Command Result）。

定义位置（Definition）：shell_remote.h:71。

符号定位：[shell_remote_data::result](P010_远端Shell运行数据.md#ac5bfd07b113aa7a79eb0bfe9f361db48)。

### `shell_remote_data::cmds`

```c
struct shell_remote_cmd cmds[2]
```

存储最近两个命令的空间，即当前命令（Current）和父命令（Parent）。

定义位置（Definition）：shell_remote.h:65。

符号定位：[shell_remote_data::cmds](P010_远端Shell运行数据.md#ad007967f92725925d2b66b27bb5e548d)。

### `shell_remote_data::msg`

```c
void * msg
```

打印消息指针；消息在堆（Heap）上分配。

定义位置（Definition）：shell_remote.h:77。

符号定位：[shell_remote_data::msg](P010_远端Shell运行数据.md#ad0cb7d3a07ad5590a86f559328fed338)。

### `shell_remote_data::sem`

```c
struct k_sem sem
```

用于同步访问远端Shell实例的信号量（Semaphore）。

定义位置（Definition）：shell_remote.h:56。

符号定位：[shell_remote_data::sem](P010_远端Shell运行数据.md#af8872d013a80afeba1201dc82892437e)。

### `shell_remote`

用于存储远端Shell实例配置的结构（Instance Configuration Structure）。

定义位置（Definition）：shell_remote.h:84。

符号定位：[shell_remote](P008_远端Shell实例.md)。

### `shell_remote::ep_cfg`

```c
struct ipc_ept_cfg ep_cfg
```

IPC端点配置（Endpoint Configuration）。

定义位置（Definition）：shell_remote.h:92。

符号定位：[shell_remote::ep_cfg](P008_远端Shell实例.md#a599061c03ce6e626e57d91be5100783b)。

### `shell_remote::name`

```c
const char * name
```

远端Shell实例的名称，即命令语法名称（Command Syntax）。

定义位置（Definition）：shell_remote.h:86。

符号定位：[shell_remote::name](P008_远端Shell实例.md#aa815345346bb54a610b8422232e78106)。

### `shell_remote::ipc`

```c
const struct device * ipc
```

进程间通信设备（IPC Device）。

定义位置（Definition）：shell_remote.h:89。

符号定位：[shell_remote::ipc](P008_远端Shell实例.md#abc23c07899d59c1b942a6e50b814b8b1)。

### `shell_static_entry`

Shell静态命令描述符（Static Command Descriptor）。

定义位置（Definition）：shell.h:299。

符号定位：[shell_static_entry](../shell_core_reference/P008_Shell静态命令条目.md)。

### `shell`

Shell实例内部结构（Instance Internals）。

定义位置（Definition）：shell.h:1129。

符号定位：[shell](../shell_core_reference/P004_Shell实例结构.md)。

## 3.4\_源码跟踪译注

> 译注——远端Shell通过IPC端点传递命令和结果。CONN宏声明静态运行数据及可遍历段中的配置，设备通过DEVICE_DT_GET取得；宏展开本身不证明端点已绑定。ready字段原文写作bounded，这里按绑定事件（Bound Event）解释。

> 译注——远端命令运行数据只保留两个命令槽，即当前命令和父命令。语法及帮助文本复制到固定大小临时缓冲区；现有实现对过长帮助文本作截断，并对语法长度使用断言。它不是可无限缓存整棵远端命令树的容器。

> 译注——打印消息接收后按8字节对齐在堆上复制，再提交工作项处理；打印结束后释放副本并发送结果确认。字段注释称work为工作队列，而声明实际是struct k_work工作项，由系统工作队列执行。

头文件定位：[include/zephyr/shell/shell_remote.h](../../../include/zephyr/shell/shell_remote.h)，关联实现／接口：[subsys/shell/shell_remote.c](../../../subsys/shell/shell_remote.c)；[官方原始头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/shell/shell_remote.h)与[官方关联文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/shell_remote.c)的摘要见来源记录。去掉注释和展示空白后，本页代码与本次读取的原始头文件一致，不能推广到以后滚动更新的main或任意本地版本。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 3.5\_原页交叉引用（Cross References）

- [查看此文件参考说明](P002_远端Shell头文件参考.md)
- [zephyr/shell/shell_remote_common.h](P006_远端Shell公共头文件参考.md)
- [zephyr/shell/shell.h](../shell_core_reference/P002_Shell核心头文件参考.md)
- [zephyr/ipc/ipc_service.h](../intercore_reference/P117_IPC服务头文件参考.md)
- [zephyr/sys/slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [shell_remote_cmd](P009_远端Shell命令.md)
- [shell_static_entry](../shell_core_reference/P008_Shell静态命令条目.md)
- [cmd](P009_远端Shell命令.md#a10d9f55e316984f5c5e1d89ce112b7ec)
- [rem_cmd](P009_远端Shell命令.md#a7a7817a33d740d6b458338f551eb5328)
- [tmp_buf](P009_远端Shell命令.md#a6563d0ec7c942d974802759b4f5f506f)
- [CONFIG_SHELL_REMOTE_TMP_BUF_SIZE](P001_远端Shell接口.md#ga0644f6ba7da5eb5bd4952d3afa6ff536)
- [shell_remote_data](P010_远端Shell运行数据.md)
- [ipc_ept](../intercore_reference/P113_IPC服务端点结构.md)
- [ept](P010_远端Shell运行数据.md#a1b411b2f856385e08fc7e915f1ac88da)
- [k_sem](../synchronization_reference/P009_内核信号量结构.md)
- [sem](P010_远端Shell运行数据.md#af8872d013a80afeba1201dc82892437e)
- [k_work](https://docs.zephyrproject.org/latest/doxygen/html/structk__work.html)
- [work](P010_远端Shell运行数据.md#ab1bade0da8e552b492c0f10448bdf6d6)
- [shell](../shell_core_reference/P004_Shell实例结构.md)
- [sh](P010_远端Shell运行数据.md#a97b2cb413dc24aa511e9e7673d031103)
- [cmds](P010_远端Shell运行数据.md#ad007967f92725925d2b66b27bb5e548d)
- [current_cmd](P010_远端Shell运行数据.md#a098d8b3da108972c75aae512527ee96d)
- [result](P010_远端Shell运行数据.md#ac5bfd07b113aa7a79eb0bfe9f361db48)
- [msg_len](P010_远端Shell运行数据.md#a129256b9fd61a17027362874bae8c87d)
- [msg](P010_远端Shell运行数据.md#ad0cb7d3a07ad5590a86f559328fed338)
- [ready](P010_远端Shell运行数据.md#a76fa224ff7b9e121318c5ed2acccd2f8)
- [shell_remote](P008_远端Shell实例.md)
- [name](P008_远端Shell实例.md#aa815345346bb54a610b8422232e78106)
- [device](../device_reference/P002_设备对象结构.md)
- [ipc](P008_远端Shell实例.md#abc23c07899d59c1b942a6e50b814b8b1)
- [ipc_ept_cfg](../intercore_reference/P114_IPC服务端点配置.md)
- [ep_cfg](P008_远端Shell实例.md#a599061c03ce6e626e57d91be5100783b)
- [cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [shell_remote_ep_bound](P001_远端Shell接口.md#ga63fce1cfe8b08c710fafa5cbc8e28a13)
- [shell_remote_ep_recv](P001_远端Shell接口.md#ga834254727aeba7c1e29cc1e6df22f23f)

---

[上一章](P002_远端Shell头文件参考.md) · [返回大纲](大纲.md) · [下一章](P004_远端Shell命令行头文件参考.md)

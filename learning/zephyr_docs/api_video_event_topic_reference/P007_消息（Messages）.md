---
id: learning.zephyr-docs.api-video-event-topic-reference.page-7
title: 消息（Messages）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__message.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_消息（Messages）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__message.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

元素向应用程序反馈的内容。

<a id="details"></a>

元素（Element）向应用报告的信息，即消息（Message）。消息与分派（Dispatch）的传递方向不同：分派沿连接端口（Pad）链路在两个元素之间传递；消息则完全离开图结构，经容器（Bin）的通道向上传递给驱动管线（Pipeline）的使用方，告知流已结束或发生故障。消息是小型值类型（Value Type），进出通道时都按值复制，发布消息不会移交任何所有权。消息携带故障发生位置，即发出消息的元素，以及发生了什么，即类型；对于故障，还携带指出出错阶段的域（Domain）和说明原因的 errno。这些信息用于回答管线无法运行时的两个问题：哪个元素、哪个阶段。消息刻意采用机器可读形式，不携带面向用户的文本字符串；故障描述应由检测到问题的位置写入日志，应用则根据域和 errno 决定处理分支。消息发布到包含其来源元素的容器总线上，该总线是可通过 `mpipe_element_get_bus_chan` 获取的 zbus 通道。任何 zbus 观察者（Observer）都可观察它：监听器（Listener）在发布线程内联运行，不得阻塞，也不得改变管线状态；消息订阅者（Message Subscriber，`CONFIG_ZBUS_MSG_SUBSCRIBER`）在自己的线程通过 `zbus_sub_wait_msg()` 读取，不会丢失消息。容器销毁前须分离观察者。消息类型使用单独的位表示，消费者可通过按位或组合多个类型为掩码。`MPIPE_MESSAGE_UNKNOWN` 为 0，不匹配任何类型：它表示未初始化消息，不是可选择的类型。

<a id="header-files"></a>
<a id="files"></a>

## 7.1\_文件（Files）

<a id="r_mpipe_5Fmessage_2Eh"></a>

```c
file mpipe_message.h
```

相关声明：[mpipe_message.h](../api_file_service_reference/P025_zephyr__mpipe__mpipe_message.h_文件参考.md)。

总线消息（Bus Message）：元素向应用报告的内容。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 7.2\_数据结构（Data Structures）

<a id="r_mpipe_5Fmessage"></a>

```c
struct mpipe_message
```

相关声明：[mpipe_message](../audio_video_model_reference/P023_mpipe_message_结构体.md)。

携带消息类型和来源的消息结构（Message Structure）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 7.3\_宏定义（Macros）

<a id="r_gac446a0608709579c28f1eec01ffa3890"></a>

```c
#define MPIPE_MESSAGE_ANY UINT32_MAX
```

相关声明：[MPIPE_MESSAGE_ANY](#gac446a0608709579c28f1eec01ffa3890)、[UINT32_MAX](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ab5eb23180f7cc12b7d6c04a8ec067fdd)。

匹配任意消息类型（Message Type）的过滤掩码（Filter Mask）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 7.4\_枚举（Enumerations）

<a id="r_ga2cbfffc03b1b703e80f73c70207cf049"></a>

```c
enum mpipe_message_type { MPIPE_MESSAGE_UNKNOWN = 0 , MPIPE_MESSAGE_EOS = BIT(0) , MPIPE_MESSAGE_ERROR = BIT(1) }
```

相关声明：[mpipe_message_type](#ga2cbfffc03b1b703e80f73c70207cf049)、[MPIPE_MESSAGE_UNKNOWN](#gga2cbfffc03b1b703e80f73c70207cf049a134a8207baabf7e3f75aa6a8d0d03c7f)、[MPIPE_MESSAGE_EOS](#gga2cbfffc03b1b703e80f73c70207cf049a0cfb22ae656d98b8915937035314e32c)、[MPIPE_MESSAGE_ERROR](#gga2cbfffc03b1b703e80f73c70207cf049a0ce944a0bd05b7b9d035a1dd717726cc)。

可用作位掩码过滤器（Bitmask Filters）的消息类型（Message Types）。

<a id="r_ga686a716e86c28adfbb11dc0c1e172c22"></a>

```c
enum mpipe_error_domain { MPIPE_ERROR_FAILED = 0 , MPIPE_ERROR_CAPS , MPIPE_ERROR_BUFFER_POOL , MPIPE_ERROR_FLOW , MPIPE_ERROR_RESOURCE , MPIPE_ERROR_DOMAIN_END }
```

相关声明：[mpipe_error_domain](#ga686a716e86c28adfbb11dc0c1e172c22)、[MPIPE_ERROR_FAILED](#gga686a716e86c28adfbb11dc0c1e172c22a3c3ba67cbdbccb5b4771b38854d384c3)、[MPIPE_ERROR_CAPS](#gga686a716e86c28adfbb11dc0c1e172c22a1e75a9bfcc4498a13c83629832d5b121)、[MPIPE_ERROR_BUFFER_POOL](#gga686a716e86c28adfbb11dc0c1e172c22a4319b9de20494144e9d9dc1330acbdba)、[MPIPE_ERROR_FLOW](#gga686a716e86c28adfbb11dc0c1e172c22a0d6250f8be21799d179e0e381ac50e79)、[MPIPE_ERROR_RESOURCE](#gga686a716e86c28adfbb11dc0c1e172c22aea01f57f830f9db7a23673aea2b02fb6)、[MPIPE_ERROR_DOMAIN_END](#gga686a716e86c28adfbb11dc0c1e172c22a23e26086d682f178fa75ce423c8e341a)。

发生失败的领域（Domain），即元素当时正在执行的操作。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 7.5\_函数（Functions）

<a id="r_ga371e6503fe08971ce1a2606d0a034b41"></a>

```c
int mpipe_message_post (const struct mpipe_message *message)
```

相关声明：[mpipe_message_post](#ga371e6503fe08971ce1a2606d0a034b41)、[mpipe_message](../audio_video_model_reference/P023_mpipe_message_结构体.md)。

向包含消息源元素的元素容器（Bin）之总线（Bus）发布消息（Message）。

## 7.6\_详细说明（Detailed Documentation）

<a id="gac446a0608709579c28f1eec01ffa3890"></a>

### `MPIPE_MESSAGE_ANY`

```c
#define MPIPE_MESSAGE_ANY UINT32_MAX
```

```c
#include <zephyr/mpipe/mpipe_message.h>
```

匹配任意消息类型（Message Type）的过滤掩码（Filter Mask）。

这里使用宏而非枚举项（Enumerator）：`UINT32_MAX` 无法装入 `int`，而筛选掩码（Filter Mask）与其匹配的类型字段一样，使用普通 `uint32_t`。

<a id="ga686a716e86c28adfbb11dc0c1e172c22"></a>

### `mpipe_error_domain`

```c
enum mpipe_error_domain
```

```c
#include <zephyr/mpipe/mpipe_message.h>
```

发生失败的领域（Domain），即元素当时正在执行的操作。

管线可能在少数几个不同阶段失败，确定阶段便有助于判断原因。此处为这些阶段命名，使报告能够说明元素当时在做什么，而不只是说明发生了错误。

域（Domain）与 `mpipe_message::code` 中的 errno 共同构成应用处理分支的依据：

原始示例（Example）：

```c
if (msg.domain == MPIPE_ERROR_RESOURCE && msg.code == -ENOENT) {
     // the input file does not exist
}
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MPIPE_ERROR_FAILED` | 没有更具体的类别适用。这也是中性值（Neutral Value）：非故障消息使用它，因此省略 `domain` 的指定初始化器（Designated Initializer）也是正确的。 |
| `MPIPE_ERROR_CAPS` | 能力协商（Capability Negotiation）：格式无法求交，尝试其他配置。 |
| `MPIPE_ERROR_BUFFER_POOL` | 缓冲区协商（Buffer Negotiation）：缓冲池无法配置或启动，减少数量或大小。 |
| `MPIPE_ERROR_FLOW` | 缓冲区流转（Buffer Flow）：流式运行期间，处理、获取或推送失败，停止或重启。 |
| `MPIPE_ERROR_RESOURCE` | 设备、文件或驱动拒绝操作；检查介质或硬件。 |
| `MPIPE_ERROR_DOMAIN_END` | 最后一个域之后的值，本身不是一个域（Domain）。 |

<a id="ga2cbfffc03b1b703e80f73c70207cf049"></a>

### `mpipe_message_type`

```c
enum mpipe_message_type
```

```c
#include <zephyr/mpipe/mpipe_message.h>
```

可用作位掩码过滤器（Bitmask Filters）的消息类型（Message Types）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MPIPE_MESSAGE_UNKNOWN` | 未初始化（Uninitialized）：清零后的消息所具有的状态，不可发布。 |
| `MPIPE_MESSAGE_EOS` | 流结束（End of Stream）。 |
| `MPIPE_MESSAGE_ERROR` | 错误（Error）。 |

<a id="ga371e6503fe08971ce1a2606d0a034b41"></a>

### `mpipe_message_post()`

```c
int mpipe_message_post ( const struct mpipe_message * message)
```

```c
#include <zephyr/mpipe/mpipe_message.h>
```

向包含消息源元素的元素容器（Bin）之总线（Bus）发布消息（Message）。

通过 `mpipe_element_get_bus_chan` 根据消息来源查找总线，并在该总线上发布。总线按值复制消息，因此使用栈上存储（Stack Storage）是可行的。这是发布消息的唯一方式：消息来源必须是一个元素，由该来源确定消息属于哪条总线。

调用方声明并初始化消息。指定初始化器（Designated Initializer）中省略的字段会为 0，这是所有字段的中性值：域为 `MPIPE_ERROR_FAILED`，无错误码。

当故障对数据流是致命的（Fatal）时，发布错误消息，因为应用需要获知这种情况。能够通过返回 errno 报告的失败仍通过 errno 报告；并非每次调用失败都应发送错误消息。

在中断服务例程（ISR）之外，此调用会等待总线，因此不得从同一总线的监听器（Listener）内调用。

原始示例（Example）：

```c
struct mpipe_message msg = {
     .origin = &sink->element,
     .type = MPIPE_MESSAGE_EOS,
};

(void)mpipe_message_post(&msg);
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `message` | 要发布的消息（Message），至少须设置来源（Origin）和类型（Type）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | 消息没有来源或没有类型。 |
| `-ENODEV` | 来源元素没有总线（Bus）。 |
| `-ENOMSG` | 总线验证器（Bus Validator）丢弃了此消息；管线会对除最后一个之外的所有流结束消息执行此操作。 |
| `-EBUSY` | 总线正在使用时，从中断服务例程（ISR）发布消息。 |

**返回（Returns）**：返回值：`zbus_chan_pub()` 的任何其他负 errno 值。


## 7.7\_原页交叉引用（Cross References）

- [mpipe_message.h](../api_file_service_reference/P025_zephyr__mpipe__mpipe_message.h_文件参考.md)
- [mpipe_message](../audio_video_model_reference/P023_mpipe_message_结构体.md)
- [UINT32_MAX](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ab5eb23180f7cc12b7d6c04a8ec067fdd)
- [mpipe_element_get_bus_chan](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#gadd1c172f5ce2f4eb6fffeb40ecc931b6)
- [CONFIG_ZBUS_MSG_SUBSCRIBER](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZBUS_MSG_SUBSCRIBER)
- [zbus_sub_wait_msg()](https://docs.zephyrproject.org/latest/doxygen/html/group__zbus__apis.html#gaeffce45446509e488192a4e6442453fb)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [mpipe_message::code](../audio_video_model_reference/P023_mpipe_message_结构体.md#a8559ee9f5039c992ed46636e3d953c49)
- [ENOENT](../error_reference/P003_系统错误号公共接口.md#ga03e689f378f643d16ea7537918528a48)
- [zbus_chan_pub()](https://docs.zephyrproject.org/latest/doxygen/html/group__zbus__apis.html#gadfcaba65b397c1d8c31836ef3cf61244)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="agroup__mpipe__message_html_gga686a716e86c28adfbb11dc0c1e172c22aea01f57f830f9db7a23673aea2b02fb6"></a>
<a id="agroup__system__errno_html_ga03e689f378f643d16ea7537918528a48"></a>
<a id="gga686a716e86c28adfbb11dc0c1e172c22a3c3ba67cbdbccb5b4771b38854d384c3"></a>
<a id="gga686a716e86c28adfbb11dc0c1e172c22a1e75a9bfcc4498a13c83629832d5b121"></a>
<a id="gga686a716e86c28adfbb11dc0c1e172c22a4319b9de20494144e9d9dc1330acbdba"></a>
<a id="gga686a716e86c28adfbb11dc0c1e172c22a0d6250f8be21799d179e0e381ac50e79"></a>
<a id="gga686a716e86c28adfbb11dc0c1e172c22aea01f57f830f9db7a23673aea2b02fb6"></a>
<a id="gga686a716e86c28adfbb11dc0c1e172c22a23e26086d682f178fa75ce423c8e341a"></a>
<a id="gga2cbfffc03b1b703e80f73c70207cf049a134a8207baabf7e3f75aa6a8d0d03c7f"></a>
<a id="gga2cbfffc03b1b703e80f73c70207cf049a0cfb22ae656d98b8915937035314e32c"></a>
<a id="gga2cbfffc03b1b703e80f73c70207cf049a0ce944a0bd05b7b9d035a1dd717726cc"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>
<a id="agroup__mpipe__message_html_ga371e6503fe08971ce1a2606d0a034b41"></a>
<a id="agroup__mpipe__message_html_gga2cbfffc03b1b703e80f73c70207cf049a0cfb22ae656d98b8915937035314e32c"></a>
<a id="astructmpipe__message_html"></a>

---

[上一章](P006_调制解调器管道（Modem Pipe）.md) · [返回大纲](大纲.md) · [下一章](P008_视频缓冲区（Video Buffers）.md)

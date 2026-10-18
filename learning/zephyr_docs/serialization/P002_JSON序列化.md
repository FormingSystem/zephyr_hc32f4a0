---
id: learning.zephyr-docs.serialization.page-2
title: JSON序列化
kind: reference
status: maintained
domains: [zephyr, serialization, development]
source_url: https://docs.zephyrproject.org/latest/services/serialization/json.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_JSON序列化

原文：[官方页面](https://docs.zephyrproject.org/latest/services/serialization/json.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 2.1\_概述

Zephyr 提供 JSON 库，可用于编码和解码 JSON 数据。

> 译注：JSON 是 JavaScript 对象表示法（JavaScript Object Notation）。下面保留官方示例；解析器的可写输入、返回位图和字段初始化要求见解码段旁的说明及[完整接口参考](P006_JSON接口参考.md)。

## 2.2\_用法（Usage）

### 定义数据结构（Defining the Data Structure）

首先定义与 JSON 对象对应的 C 结构体，以及将结构体字段映射到 JSON 词元（Token）的描述符（Descriptor）。

```c
#include <zephyr/data/json.h>

struct foo {
    int bar;
    const char *baz;
};

static const struct json_obj_descr foo_descr[] = {
    JSON_OBJ_DESCR_PRIM(struct foo, bar, JSON_TOK_NUMBER),
    JSON_OBJ_DESCR_PRIM(struct foo, baz, JSON_TOK_STRING),
};
```

### 编码（Encoding）

要把 C 结构体编码成 JSON 字符串，使用 [`json_obj_encode_buf()`](P006_JSON接口参考.md#gab758ad32cfb6369f4967a6842ac63245)。

```c
void encode_example(void)
{
    struct foo data = { .bar = 42, .baz = "hello" };
    char buffer[128];
    int ret;

    ret = json_obj_encode_buf(foo_descr, ARRAY_SIZE(foo_descr),
                              &data,
                              buffer, sizeof(buffer));
    if (ret < 0) {
        /* handle error */
    }
}
```

代码中的 `handle error` 注释表示“处理错误”。

### 解码（Decoding）

要把 JSON 字符串解码为 C 结构体，使用 [`json_obj_parse()`](P006_JSON接口参考.md#ga73997fa2154fcbc80f37edd7bcf3477a)。

```c
void decode_example(void)
{
    struct foo data;
    const char *json_text = "{\"bar\": 42, \"baz\": \"hello\"}";
    int ret;

    ret = json_obj_parse(json_text, strlen(json_text),
                         foo_descr, ARRAY_SIZE(foo_descr),
                         &data);
    if (ret < 0) {
        /* handle error */
    }
}
```

代码中的 `handle error` 注释同样表示“处理错误”。

> 译注：`json_obj_parse()` 接收 `char *`，字符串解析会向输入缓冲区写入终止字符；不能把字符串字面量经 `const char *` 传给它。解析返回类型是 `int64_t`，成功值是已解码字段的位图（Bitmap），不是普通的“成功返回 0”。解析只写入实际出现的成员，因此目标结构体要先初始化。

可将原例中的对应声明改成以下形式，再使用原例的描述符调用解析函数。这是针对上方示例的译注补充：

```c
struct foo data = {0};
char json_text[] = "{\"bar\": 42, \"baz\": \"hello\"}";
int64_t ret;
```

> 译注：上例两个顶层描述符都成功解码时，位图为 `0x3`。非负返回值仍需按应用要求检查必需字段；`data.baz` 引用输入缓冲区内的数据，使用期间应保持缓冲区有效。依据为同批[接口参考](P006_JSON接口参考.md)及[官方实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/lib/utils/json.c)；读取摘要见[来源记录](../SOURCES.md)。本仓库的[JSON实现](../../../lib/utils/json.c)可用于对照，但不自动等同于官网版本。

## 2.3\_配置（Configuration）

启用 Kconfig 选项 [`CONFIG_JSON_LIBRARY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_JSON_LIBRARY)，即可启用 JSON 支持。

## 2.4\_API参考（API Reference）

见 [JSON接口参考](P006_JSON接口参考.md)。

## 2.5\_相关代码示例（Related Code Samples）

- [AWS IoT Core MQTT](../networking/P216_AWS物联网MQTT示例.md#aws-iot-mqtt)：连接 AWS IoT Core，并使用 MQTT 发布消息。
- [Eclipse hawkBit直接设备集成API](https://docs.zephyrproject.org/latest/samples/subsys/mgmt/hawkbit/README.html#hawkbit-api)：使用 Eclipse hawkBit 直接设备集成（Direct Device Integration，DDI）API 更新设备。
- [HTTP服务器](https://docs.zephyrproject.org/latest/samples/net/sockets/http_server/README.html#sockets-http-server)：实现展示多种资源类型的 HTTP(s) 服务器。
- [安全MQTT传感器／执行器](https://docs.zephyrproject.org/latest/samples/net/secure_mqtt_sensor_actuator/README.html#secure-mqtt-sensor-actuator)：实现基于 MQTT 的物联网（Internet of Things，IoT）传感器／执行器设备。

> 译注：MQTT 为消息队列遥测传输（Message Queuing Telemetry Transport）；HTTP 为超文本传输协议（Hypertext Transfer Protocol）。这些链接是原页列出的应用示例，不能由本页翻译完成推定为示例也已译完。


<a id="json"></a>
<a id="json-api"></a>
<a id="usage"></a>
<a id="defining-the-data-structure"></a>
<a id="encoding"></a>
<a id="decoding"></a>
<a id="configuration"></a>
<a id="api-reference"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：序列化概览](P001_序列化概览.md) · [本模块主线目录](../reading/serialization.md) · [全部主线](../reading/README.md) · [下一篇：CBOR序列化](P003_CBOR序列化.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P001_序列化概览.md) · [返回大纲](大纲.md) · [下一章](P003_CBOR序列化.md)

</details>

<!-- reading-navigation:end -->

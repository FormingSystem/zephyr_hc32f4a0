---
id: learning.zephyr-docs.audio-video-model-reference.page-9
title: i2s_driver_api_结构体
kind: reference
status: maintained
domains: [zephyr, multimedia, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structi2s__driver__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_i2s\_driver\_api\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structi2s__driver__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

驱动操作（Driver Operations）：I2S驱动操作。

```c
#include <zephyr/drivers/i2s.h>
```

<a id="details"></a>

驱动操作（Driver Operations）：I2S 驱动操作。这是每个 I2S 驱动都需要定义的驱动 API 结构体，其中包含指向驱动所实现操作的函数指针，以及其他驱动专用常量数据。标记为 REQ 的成员必须由驱动设置，标记为 OPT 的成员为可选。另见 `DEVICE_DT_INST_DEFINE()`、`DEVICE_DT_DEFINE()` 和 `DEVICE_API()`。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 9.1\_数据成员（Data Fields）

<a id="r_a8d6eec41d35f812e1d75d4fcd4bcc88b"></a>

```c
int(* configure )(const struct device *dev, enum i2s_dir dir, const struct i2s_config *cfg)
```

相关声明：[configure](#a8d6eec41d35f812e1d75d4fcd4bcc88b)、[device](../device_reference/P002_设备对象结构.md)、[i2s_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga975a0f0901cadc789075078aa79f723f)、[i2s_config](P008_i2s_config_结构体.md)。

必需（REQ）：配置主机 I2S 控制器。参数说明参见 `i2s_configure()`。

<a id="r_a0744f7bf2e105e4cd8f1393703c2974c"></a>

```c
const struct i2s_config *(* config_get )(const struct device *dev, enum i2s_dir dir)
```

相关声明：[i2s_config](P008_i2s_config_结构体.md)、[config_get](#a0744f7bf2e105e4cd8f1393703c2974c)、[device](../device_reference/P002_设备对象结构.md)、[i2s_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga975a0f0901cadc789075078aa79f723f)。

必需（REQ）：获取主机 I2S 控制器的配置信息。参数说明参见 `i2s_config_get()`。

<a id="r_a91e7112e5f9b72032d9c163a49bad0f5"></a>

```c
int(* read )(const struct device *dev, void **mem_block, size_t *size)
```

相关声明：[read](#a91e7112e5f9b72032d9c163a49bad0f5)、[device](../device_reference/P002_设备对象结构.md)。

必需（REQ）：从接收队列读取数据。参数说明参见 `i2s_read()`。

<a id="r_a3b453b26bd97b2e16a4383e4ace00db9"></a>

```c
int(* write )(const struct device *dev, void *mem_block, size_t size)
```

相关声明：[write](#a3b453b26bd97b2e16a4383e4ace00db9)、[device](../device_reference/P002_设备对象结构.md)。

必需（REQ）：向发送队列写入数据。参数说明参见 `i2s_write()`。

<a id="r_a06d8b579cef57fc5b55ae1012afafd3d"></a>

```c
int(* trigger )(const struct device *dev, enum i2s_dir dir, enum i2s_trigger_cmd cmd)
```

相关声明：[trigger](#a06d8b579cef57fc5b55ae1012afafd3d)、[device](../device_reference/P002_设备对象结构.md)、[i2s_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga975a0f0901cadc789075078aa79f723f)、[i2s_trigger_cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#gac994676a89f1ea676475712a84003de6)、[cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)。

必需（REQ）：发送触发命令。参数说明参见 `i2s_trigger()`。

## 9.2\_详细说明（Detailed Documentation）

<a id="a0744f7bf2e105e4cd8f1393703c2974c"></a>

### `config_get`

```c
const struct i2s_config *(* i2s_driver_api::config_get) (const struct device *dev, enum i2s_dir dir)
```

必需（REQ）：获取主机 I2S 控制器的配置信息。参数说明参见 `i2s_config_get()`。

<a id="a8d6eec41d35f812e1d75d4fcd4bcc88b"></a>

### `configure`

```c
int(* i2s_driver_api::configure) (const struct device *dev, enum i2s_dir dir, const struct i2s_config *cfg)
```

必需（REQ）：配置主机 I2S 控制器。参数说明参见 `i2s_configure()`。

<a id="a91e7112e5f9b72032d9c163a49bad0f5"></a>

### `read`

```c
int(* i2s_driver_api::read) (const struct device *dev, void **mem_block, size_t *size)
```

必需（REQ）：从接收队列读取数据。参数说明参见 `i2s_read()`。

<a id="a06d8b579cef57fc5b55ae1012afafd3d"></a>

### `trigger`

```c
int(* i2s_driver_api::trigger) (const struct device *dev, enum i2s_dir dir, enum i2s_trigger_cmd cmd)
```

必需（REQ）：发送触发命令。参数说明参见 `i2s_trigger()`。

<a id="a3b453b26bd97b2e16a4383e4ace00db9"></a>

### `write`

```c
int(* i2s_driver_api::write) (const struct device *dev, void *mem_block, size_t size)
```

必需（REQ）：向发送队列写入数据。参数说明参见 `i2s_write()`。

本数据类型文档由以下文件生成：

- `zephyr/drivers/i2s.h`

## 9.3\_原页交叉引用（Cross References）

- [zephyr/drivers/i2s.h](https://docs.zephyrproject.org/latest/doxygen/html/i2s_8h_source.html)
- [device](../device_reference/P002_设备对象结构.md)
- [i2s_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga975a0f0901cadc789075078aa79f723f)
- [i2s_config](P008_i2s_config_结构体.md)
- [i2s_configure()](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga299003d72146c127f88d7c12c08889cc)
- [i2s_config_get()](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#gacf4d51fcfd07573582858cd50a76785d)
- [i2s_read()](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga7f23b7959280e1c4075a4305c3edd655)
- [i2s_write()](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga01edf23acc6c16bbaf718dab8061a7a0)
- [i2s_trigger_cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#gac994676a89f1ea676475712a84003de6)
- [cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)
- [i2s_trigger()](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#gaaa153e6c325f8f34f2fd5d550e4d3297)
- [DEVICE_DT_INST_DEFINE()](../device_reference/P001_设备模型公共接口.md#gada5ba4aca9e0662ccebb2232c7256419)
- [DEVICE_DT_DEFINE()](../device_reference/P001_设备模型公共接口.md#gac49e26fbe91a14307d5ea08d41561dd1)
- [DEVICE_API()](../device_reference/P007_设备模型头文件参考.md#aa0cdc799fc0b9c80eb29f989eec86707)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P008_i2s_config_结构体.md) · [返回大纲](大纲.md) · [下一章](P010_mic_privacy_api_funcs_结构体.md)

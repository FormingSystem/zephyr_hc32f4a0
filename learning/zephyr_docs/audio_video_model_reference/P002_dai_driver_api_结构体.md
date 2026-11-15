---
id: learning.zephyr-docs.audio-video-model-reference.page-2
title: dai_driver_api_结构体
kind: reference
status: maintained
domains: [zephyr, multimedia, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structdai__driver__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_dai\_driver\_api\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structdai__driver__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

驱动操作（Driver Operations）：数字音频接口（DAI）驱动操作。

```c
#include <zephyr/drivers/dai.h>
```

<a id="details"></a>

驱动操作（Driver Operations）：数字音频接口（DAI）驱动操作。这是每个 DAI 驱动都需要定义的驱动 API 结构体，其中包含指向驱动所实现操作的函数指针，以及其他驱动专用常量数据。标记为 REQ 的成员必须由驱动设置，标记为 OPT 的成员为可选。另见 `DEVICE_DT_INST_DEFINE()`、`DEVICE_DT_DEFINE()` 和 `DEVICE_API()`。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 2.1\_数据成员（Data Fields）

<a id="r_a4462ee3f3a8faab6b37454fae903ae01"></a>

```c
int(* probe )(const struct device *dev)
```

相关声明：[probe](#a4462ee3f3a8faab6b37454fae903ae01)、[device](../device_reference/P002_设备对象结构.md)。

必需（REQ）：DAI 驱动的探测（Probe）操作。

<a id="r_a0a59502c00c154c199f42e78cbd7d6b3"></a>

```c
int(* remove )(const struct device *dev)
```

相关声明：[remove](#a0a59502c00c154c199f42e78cbd7d6b3)、[device](../device_reference/P002_设备对象结构.md)。

必需（REQ）：DAI 驱动的移除（Remove）操作。

<a id="r_aed9c7791a77f71f68174ab02b85eebf8"></a>

```c
int(* config_set )(const struct device *dev, const struct dai_config *cfg, const void *bespoke_cfg, size_t size)
```

相关声明：[config_set](#aed9c7791a77f71f68174ab02b85eebf8)、[device](../device_reference/P002_设备对象结构.md)、[dai_config](P001_dai_config_结构体.md)。

必需（REQ）：配置 DAI 驱动的操作。

<a id="r_a6d6ca0c0a5cefda514dc23d3e61d6590"></a>

```c
int(* config_get )(const struct device *dev, struct dai_config *cfg, enum dai_dir dir)
```

相关声明：[config_get](#a6d6ca0c0a5cefda514dc23d3e61d6590)、[device](../device_reference/P002_设备对象结构.md)、[dai_config](P001_dai_config_结构体.md)、[dai_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gafa7b22e4250c6479301fc657fea8a60f)。

必需（REQ）：获取 DAI 驱动的配置信息。

<a id="r_a3a8e89d0d8cf8df19a807ffdadce1b29"></a>

```c
const struct dai_properties *(* get_properties )(const struct device *dev, enum dai_dir dir, int stream_id)
```

相关声明：[dai_properties](P003_dai_properties_结构体.md)、[get_properties](#a3a8e89d0d8cf8df19a807ffdadce1b29)、[device](../device_reference/P002_设备对象结构.md)、[dai_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gafa7b22e4250c6479301fc657fea8a60f)。

可选（OPT）：获取 DAI 驱动的属性。

<a id="r_ad2de08427255233cceaa7a2f0c2ba200"></a>

```c
int(* get_properties_copy )(const struct device *dev, enum dai_dir dir, int stream_id, struct dai_properties *dst)
```

相关声明：[get_properties_copy](#ad2de08427255233cceaa7a2f0c2ba200)、[device](../device_reference/P002_设备对象结构.md)、[dai_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gafa7b22e4250c6479301fc657fea8a60f)、[dai_properties](P003_dai_properties_结构体.md)。

可选（OPT）：获取 DAI 驱动的属性。

<a id="r_a3ff217a5967a2b6657b01b766a7061b2"></a>

```c
int(* trigger )(const struct device *dev, enum dai_dir dir, enum dai_trigger_cmd cmd)
```

相关声明：[trigger](#a3ff217a5967a2b6657b01b766a7061b2)、[device](../device_reference/P002_设备对象结构.md)、[dai_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gafa7b22e4250c6479301fc657fea8a60f)、[dai_trigger_cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gaee6445967afb3ecf2c0470ca0c104a1a)、[cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)。

必需（REQ）：发送触发命令（trigger command）。

<a id="r_a3cfd0430d2fdb7c7ab5719c142b9b7a4"></a>

```c
int(* ts_config )(const struct device *dev, struct dai_ts_cfg *cfg)
```

相关声明：[ts_config](#a3cfd0430d2fdb7c7ab5719c142b9b7a4)、[device](../device_reference/P002_设备对象结构.md)、[dai_ts_cfg](P004_dai_ts_cfg_结构体.md)。

可选（OPT）：在关联的 DAI 上配置时间戳（timestamping）功能。

<a id="r_a22f84e02f1eb735075498066d62a08d3"></a>

```c
int(* ts_start )(const struct device *dev, struct dai_ts_cfg *cfg)
```

相关声明：[ts_start](#a22f84e02f1eb735075498066d62a08d3)、[device](../device_reference/P002_设备对象结构.md)、[dai_ts_cfg](P004_dai_ts_cfg_结构体.md)。

可选（OPT）：启动时间戳功能。

<a id="r_a5dbed6fe2ab663ef97dd4aea7e4ef1df"></a>

```c
int(* ts_stop )(const struct device *dev, struct dai_ts_cfg *cfg)
```

相关声明：[ts_stop](#a5dbed6fe2ab663ef97dd4aea7e4ef1df)、[device](../device_reference/P002_设备对象结构.md)、[dai_ts_cfg](P004_dai_ts_cfg_结构体.md)。

可选（OPT）：停止时间戳功能。

<a id="r_ac0f88957ca2fe0bfc7b9e1eca5f81f1e"></a>

```c
int(* ts_get )(const struct device *dev, struct dai_ts_cfg *cfg, struct dai_ts_data *tsd)
```

相关声明：[ts_get](#ac0f88957ca2fe0bfc7b9e1eca5f81f1e)、[device](../device_reference/P002_设备对象结构.md)、[dai_ts_cfg](P004_dai_ts_cfg_结构体.md)、[dai_ts_data](P005_dai_ts_data_结构体.md)。

可选（OPT）：获取时间戳。

<a id="r_a4610c94767bfb81ed6d601aa44f1596b"></a>

```c
int(* config_update )(const struct device *dev, const void *bespoke_cfg, size_t size)
```

相关声明：[config_update](#a4610c94767bfb81ed6d601aa44f1596b)、[device](../device_reference/P002_设备对象结构.md)。

可选（OPT）：在运行时更新 DAI 配置。

## 2.2\_详细说明（Detailed Documentation）

<a id="a6d6ca0c0a5cefda514dc23d3e61d6590"></a>

### `config_get`

```c
int(* dai_driver_api::config_get) (const struct device *dev, struct dai_config *cfg, enum dai_dir dir)
```

必需（REQ）：获取 DAI 驱动的配置信息。

<a id="aed9c7791a77f71f68174ab02b85eebf8"></a>

### `config_set`

```c
int(* dai_driver_api::config_set) (const struct device *dev, const struct dai_config *cfg, const void *bespoke_cfg, size_t size)
```

必需（REQ）：配置 DAI 驱动的操作。

<a id="a4610c94767bfb81ed6d601aa44f1596b"></a>

### `config_update`

```c
int(* dai_driver_api::config_update) (const struct device *dev, const void *bespoke_cfg, size_t size)
```

可选（OPT）：在运行时更新 DAI 配置。

<a id="a3a8e89d0d8cf8df19a807ffdadce1b29"></a>

### `get_properties`

```c
const struct dai_properties *(* dai_driver_api::get_properties) (const struct device *dev, enum dai_dir dir, int stream_id)
```

可选（OPT）：获取 DAI 驱动的属性。

<a id="ad2de08427255233cceaa7a2f0c2ba200"></a>

### `get_properties_copy`

```c
int(* dai_driver_api::get_properties_copy) (const struct device *dev, enum dai_dir dir, int stream_id, struct dai_properties *dst)
```

可选（OPT）：获取 DAI 驱动的属性。

<a id="a4462ee3f3a8faab6b37454fae903ae01"></a>

### `probe`

```c
int(* dai_driver_api::probe) (const struct device *dev)
```

必需（REQ）：DAI 驱动的探测（Probe）操作。

<a id="a0a59502c00c154c199f42e78cbd7d6b3"></a>

### `remove`

```c
int(* dai_driver_api::remove) (const struct device *dev)
```

必需（REQ）：DAI 驱动的移除（Remove）操作。

<a id="a3ff217a5967a2b6657b01b766a7061b2"></a>

### `trigger`

```c
int(* dai_driver_api::trigger) (const struct device *dev, enum dai_dir dir, enum dai_trigger_cmd cmd)
```

必需（REQ）：发送触发命令（trigger command）。

<a id="a3cfd0430d2fdb7c7ab5719c142b9b7a4"></a>

### `ts_config`

```c
int(* dai_driver_api::ts_config) (const struct device *dev, struct dai_ts_cfg *cfg)
```

可选（OPT）：在关联的 DAI 上配置时间戳（timestamping）功能。

<a id="ac0f88957ca2fe0bfc7b9e1eca5f81f1e"></a>

### `ts_get`

```c
int(* dai_driver_api::ts_get) (const struct device *dev, struct dai_ts_cfg *cfg, struct dai_ts_data *tsd)
```

可选（OPT）：获取时间戳。

<a id="a22f84e02f1eb735075498066d62a08d3"></a>

### `ts_start`

```c
int(* dai_driver_api::ts_start) (const struct device *dev, struct dai_ts_cfg *cfg)
```

可选（OPT）：启动时间戳功能。

<a id="a5dbed6fe2ab663ef97dd4aea7e4ef1df"></a>

### `ts_stop`

```c
int(* dai_driver_api::ts_stop) (const struct device *dev, struct dai_ts_cfg *cfg)
```

可选（OPT）：停止时间戳功能。

本数据类型文档由以下文件生成：

- `zephyr/drivers/dai.h`

## 2.3\_原页交叉引用（Cross References）

- [zephyr/drivers/dai.h](https://docs.zephyrproject.org/latest/doxygen/html/dai_8h_source.html)
- [device](../device_reference/P002_设备对象结构.md)
- [dai_config](P001_dai_config_结构体.md)
- [dai_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gafa7b22e4250c6479301fc657fea8a60f)
- [dai_properties](P003_dai_properties_结构体.md)
- [dai_trigger_cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gaee6445967afb3ecf2c0470ca0c104a1a)
- [cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)
- [dai_ts_cfg](P004_dai_ts_cfg_结构体.md)
- [dai_ts_data](P005_dai_ts_data_结构体.md)
- [DEVICE_DT_INST_DEFINE()](../device_reference/P001_设备模型公共接口.md#gada5ba4aca9e0662ccebb2232c7256419)
- [DEVICE_DT_DEFINE()](../device_reference/P001_设备模型公共接口.md#gac49e26fbe91a14307d5ea08d41561dd1)
- [DEVICE_API()](../device_reference/P007_设备模型头文件参考.md#aa0cdc799fc0b9c80eb29f989eec86707)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P001_dai_config_结构体.md) · [返回大纲](大纲.md) · [下一章](P003_dai_properties_结构体.md)

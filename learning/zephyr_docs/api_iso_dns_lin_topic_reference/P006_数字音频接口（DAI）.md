---
id: learning.zephyr-docs.api-iso-dns-lin-topic-reference.page-6
title: 数字音频接口（DAI）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_数字音频接口（DAI）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

数字音频接口（Digital Audio Interfaces）相关接口。

<a id="details"></a>

数字音频接口（Digital Audio Interfaces，DAI）的接口。自 3.1 引入，版本 0.9.0。DAI API 支持标准 I2S（SSP）及其常见变体，也支持 DMIC、HDA 和 SDW 后端（Backend）。其配置函数通过专用数据参数承载设备／厂商特定配置；还提供可选的时间戳函数，用于获取设备特定的音频时钟时间。

<a id="header-groups"></a>
<a id="groups"></a>

## 6.1\_主题（Topics）

<a id="r_dai_5Finterface_5Fbackend"></a>

相关声明：[DAI 驱动后端 API（Driver Backend API）](../api_platform_topic_reference/P013_DAI 驱动后端 API（Driver Backend API）.md)。

<a id="header-files"></a>
<a id="files"></a>

## 6.2\_文件（Files）

<a id="r_dai_2Eh"></a>

```c
file dai.h
```

相关声明：[dai.h](../api_file_serial_motion_reference/P002_zephyr__drivers__dai.h_文件参考.md)。

数字音频接口（Digital Audio Interface，DAI）驱动API的主头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 6.3\_数据结构（Data Structures）

<a id="r_dai_5Fproperties"></a>

```c
struct dai_properties
```

相关声明：[dai_properties](../audio_video_model_reference/P003_dai_properties_结构体.md)。

数字音频接口（DAI）的属性。

<a id="r_dai_5Fconfig"></a>

```c
struct dai_config
```

相关声明：[dai_config](../audio_video_model_reference/P001_dai_config_结构体.md)。

数字音频接口（DAI）的主配置结构。

<a id="r_dai_5Fts_5Fcfg"></a>

```c
struct dai_ts_cfg
```

相关声明：[dai_ts_cfg](../audio_video_model_reference/P004_dai_ts_cfg_结构体.md)。

数字音频接口（DAI）的时间戳配置。

<a id="r_dai_5Fts_5Fdata"></a>

```c
struct dai_ts_data
```

相关声明：[dai_ts_data](../audio_video_model_reference/P005_dai_ts_data_结构体.md)。

数字音频接口（DAI）的时间戳数据。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 6.4\_宏定义（Macros）

<a id="r_ga2a51e43f9a14435a64e428df0b393703"></a>

```c
#define DAI_FORMAT_CLOCK_PROVIDER_MASK 0xf000
```

相关声明：[DAI_FORMAT_CLOCK_PROVIDER_MASK](#ga2a51e43f9a14435a64e428df0b393703)。

用于从 `struct dai_config` 的 `format` 属性提取时钟配置（Clock Configuration）。

<a id="r_gaef86b295b1a13cc91e53f8cdbb4cf008"></a>

```c
#define DAI_FORMAT_PROTOCOL_MASK 0x000f
```

相关声明：[DAI_FORMAT_PROTOCOL_MASK](#gaef86b295b1a13cc91e53f8cdbb4cf008)。

用于从 `struct dai_config` 的 `format` 属性提取协议（Protocol）。

<a id="r_ga8891542769e33930342bb5039b57fda8"></a>

```c
#define DAI_FORMAT_CLOCK_INVERSION_MASK 0x0f00
```

相关声明：[DAI_FORMAT_CLOCK_INVERSION_MASK](#ga8891542769e33930342bb5039b57fda8)。

用于从 `struct dai_config` 的 `format` 属性提取时钟反相设置（Clock Inversion）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 6.5\_枚举（Enumerations）

<a id="r_ga840116b8b56fd0263a17791e7156975d"></a>

```c
enum dai_clock_provider { DAI_CBP_CFP = (0 << 12) , DAI_CBC_CFP = (2 << 12) , DAI_CBP_CFC = (3 << 12) , DAI_CBC_CFC = (4 << 12) }
```

相关声明：[dai_clock_provider](#ga840116b8b56fd0263a17791e7156975d)、[DAI_CBP_CFP](#gga840116b8b56fd0263a17791e7156975da347440e41adadd2b6a91076f53abe2e3)、[DAI_CBC_CFP](#gga840116b8b56fd0263a17791e7156975daf4862a3af6fb46f6ac9ffc0cdbbcf0a1)、[DAI_CBP_CFC](#gga840116b8b56fd0263a17791e7156975da4baee3a3ab87e540b5f4caf26e8d8c4b)、[DAI_CBC_CFC](#gga840116b8b56fd0263a17791e7156975da9f8f99d63e607d9603f54d535bd89f84)。

数字音频接口（DAI）时钟配置（Clock Configurations）。

<a id="r_ga3fa4c114ad6a3dd6a6015b6ab3d119a2"></a>

```c
enum dai_protocol { DAI_PROTO_I2S = 1 , DAI_PROTO_RIGHT_J , DAI_PROTO_LEFT_J , DAI_PROTO_DSP_A , DAI_PROTO_DSP_B , DAI_PROTO_PDM }
```

相关声明：[dai_protocol](#ga3fa4c114ad6a3dd6a6015b6ab3d119a2)、[DAI_PROTO_I2S](#gga3fa4c114ad6a3dd6a6015b6ab3d119a2adf515857c95ea685a32bf18c0ebb9af2)、[DAI_PROTO_RIGHT_J](#gga3fa4c114ad6a3dd6a6015b6ab3d119a2a9ed5273ee9ea0761ccf9cbc7f7295a3f)、[DAI_PROTO_LEFT_J](#gga3fa4c114ad6a3dd6a6015b6ab3d119a2a0d0f5db48e33cef8aa6c59a00792866b)、[DAI_PROTO_DSP_A](#gga3fa4c114ad6a3dd6a6015b6ab3d119a2a6ffdc334c0f64feeb95297293f747bc3)、[DAI_PROTO_DSP_B](#gga3fa4c114ad6a3dd6a6015b6ab3d119a2aea1fd67c47f7d8d7e3ca18b2f2e806a0)、[DAI_PROTO_PDM](#gga3fa4c114ad6a3dd6a6015b6ab3d119a2a3235bf6888b65c9c6e3a0d2f95fc0758)。

数字音频接口（DAI）协议（Protocol）。

<a id="r_gaf66ca0bbc1f8ba2f2b81caf92bd09b60"></a>

```c
enum dai_clock_inversion { DAI_INVERSION_NB_NF = 0 , DAI_INVERSION_NB_IF = (2 << 8) , DAI_INVERSION_IB_NF = (3 << 8) , DAI_INVERSION_IB_IF = (4 << 8) }
```

相关声明：[dai_clock_inversion](#gaf66ca0bbc1f8ba2f2b81caf92bd09b60)、[DAI_INVERSION_NB_NF](#ggaf66ca0bbc1f8ba2f2b81caf92bd09b60a35606eb43c6d77204bff029bfab37698)、[DAI_INVERSION_NB_IF](#ggaf66ca0bbc1f8ba2f2b81caf92bd09b60ad6622f24986622cf16fdeada99356c43)、[DAI_INVERSION_IB_NF](#ggaf66ca0bbc1f8ba2f2b81caf92bd09b60ae0a56f8334363d4a1aa916ffe5d70e5c)、[DAI_INVERSION_IB_IF](#ggaf66ca0bbc1f8ba2f2b81caf92bd09b60ab35554010caadb69a5414c7f07649ee1)。

数字音频接口（DAI）时钟反相（Clock Inversion）。

<a id="r_gac95242d83a2c2b477fcb9eb3da420797"></a>

```c
enum dai_type { DAI_LEGACY_I2S = 0 , DAI_INTEL_SSP , DAI_INTEL_DMIC , DAI_INTEL_HDA , DAI_INTEL_ALH , DAI_IMX_SAI , DAI_IMX_ESAI , DAI_AMD_BT , DAI_AMD_SP , DAI_AMD_DMIC , DAI_MEDIATEK_AFE , DAI_INTEL_SSP_NHLT , DAI_INTEL_DMIC_NHLT , DAI_INTEL_HDA_NHLT , DAI_INTEL_ALH_NHLT , DAI_IMX_MICFIL , DAI_INTEL_UAOL , DAI_AMD_SDW , DAI_AMD_TDM }
```

相关声明：[dai_type](#gac95242d83a2c2b477fcb9eb3da420797)、[DAI_LEGACY_I2S](#ggac95242d83a2c2b477fcb9eb3da420797a2560d8f844796f647ed774748c44adfe)、[DAI_INTEL_SSP](#ggac95242d83a2c2b477fcb9eb3da420797a9301e2ec67fa75aefc0e59df727adcc9)、[DAI_INTEL_DMIC](#ggac95242d83a2c2b477fcb9eb3da420797a366db52bd49557d047f091cdb96b5e36)、[DAI_INTEL_HDA](#ggac95242d83a2c2b477fcb9eb3da420797a1a591d4c0b7a70e175fc967b59929326)、[DAI_INTEL_ALH](#ggac95242d83a2c2b477fcb9eb3da420797a19dd111b0d7f7772415bc60c1256d141)、[DAI_IMX_SAI](#ggac95242d83a2c2b477fcb9eb3da420797aa94ef995d95f9d0ad8b404e26b79faec)、[DAI_IMX_ESAI](#ggac95242d83a2c2b477fcb9eb3da420797a75bfaa3859321a283929ae033fcf22aa)、[DAI_AMD_BT](#ggac95242d83a2c2b477fcb9eb3da420797a6c0c4b31c71c9e779a2a9325dc119fd0)、[DAI_AMD_SP](#ggac95242d83a2c2b477fcb9eb3da420797ab675d7b5204a2cbc09f1f60a44f4ff3b)、[DAI_AMD_DMIC](#ggac95242d83a2c2b477fcb9eb3da420797a37f79dfe1804d4abeb89a9767bf37c75)、[DAI_MEDIATEK_AFE](#ggac95242d83a2c2b477fcb9eb3da420797ac5095e399162d248e638b87a61b59a00)、[DAI_INTEL_SSP_NHLT](#ggac95242d83a2c2b477fcb9eb3da420797a8d75b1d72f5fcff348c15281001f9aaa)、[DAI_INTEL_DMIC_NHLT](#ggac95242d83a2c2b477fcb9eb3da420797a3d759f9665a4db0c974913c4aa71e6f2)、[DAI_INTEL_HDA_NHLT](#ggac95242d83a2c2b477fcb9eb3da420797afd1f617fdd16363c1a10e9f45a67a99b)、[DAI_INTEL_ALH_NHLT](#ggac95242d83a2c2b477fcb9eb3da420797a2a12c2858722c553cb31f24aacd83976)、[DAI_IMX_MICFIL](#ggac95242d83a2c2b477fcb9eb3da420797a15cf161a5126110860c89ce9a118045b)、[DAI_INTEL_UAOL](#ggac95242d83a2c2b477fcb9eb3da420797a6d88cd52faa8d93716f81d68fabb794d)、[DAI_AMD_SDW](#ggac95242d83a2c2b477fcb9eb3da420797ae58e4acd79cd16d98976fef1978a231c)、[DAI_AMD_TDM](#ggac95242d83a2c2b477fcb9eb3da420797ab63816ace8bc3fc6f35d0435fd37931e)。

数字音频接口类型（Types of DAI）。

<a id="r_gafa7b22e4250c6479301fc657fea8a60f"></a>

```c
enum dai_dir { DAI_DIR_TX = 0 , DAI_DIR_RX , DAI_DIR_BOTH }
```

相关声明：[dai_dir](#gafa7b22e4250c6479301fc657fea8a60f)、[DAI_DIR_TX](#ggafa7b22e4250c6479301fc657fea8a60fadfdf2212e2d86296dbccc60cfd60368c)、[DAI_DIR_RX](#ggafa7b22e4250c6479301fc657fea8a60fa48cc817cda4907b94a03e13e8b9aa69b)、[DAI_DIR_BOTH](#ggafa7b22e4250c6479301fc657fea8a60fa58581d875a6a8c28adb0f6351a37f3e1)。

数字音频接口（DAI）方向（Direction）。

<a id="r_ga18f708594ea85d6b893906336047c3a5"></a>

```c
enum dai_state { DAI_STATE_NOT_READY = 0 , DAI_STATE_READY , DAI_STATE_RUNNING , DAI_STATE_PRE_RUNNING , DAI_STATE_PAUSED , DAI_STATE_STOPPING , DAI_STATE_ERROR }
```

相关声明：[dai_state](#ga18f708594ea85d6b893906336047c3a5)、[DAI_STATE_NOT_READY](#gga18f708594ea85d6b893906336047c3a5a8486be6ff6f6bf91ee4a8ad632377987)、[DAI_STATE_READY](#gga18f708594ea85d6b893906336047c3a5a095422b1a71b65e5a5902e0ca5cd3650)、[DAI_STATE_RUNNING](#gga18f708594ea85d6b893906336047c3a5a8692bbb3fce619aec3dfe5ed9697f73f)、[DAI_STATE_PRE_RUNNING](#gga18f708594ea85d6b893906336047c3a5a234306cd9cc97674455f8a9321834953)、[DAI_STATE_PAUSED](#gga18f708594ea85d6b893906336047c3a5acb4e0c1f9df9eb0b7cf965b710a2ad13)、[DAI_STATE_STOPPING](#gga18f708594ea85d6b893906336047c3a5aba10f89376d67abdc3dc704c6b283d2b)、[DAI_STATE_ERROR](#gga18f708594ea85d6b893906336047c3a5a5030da046fda46120d9b54a686fb35ef)。

接口状态（Interface State）。

<a id="r_gaee6445967afb3ecf2c0470ca0c104a1a"></a>

```c
enum dai_trigger_cmd { DAI_TRIGGER_START = 0 , DAI_TRIGGER_PRE_START , DAI_TRIGGER_STOP , DAI_TRIGGER_PAUSE , DAI_TRIGGER_POST_STOP , DAI_TRIGGER_DRAIN , DAI_TRIGGER_DROP , DAI_TRIGGER_PREPARE , DAI_TRIGGER_RESET , DAI_TRIGGER_COPY }
```

相关声明：[dai_trigger_cmd](#gaee6445967afb3ecf2c0470ca0c104a1a)、[DAI_TRIGGER_START](#ggaee6445967afb3ecf2c0470ca0c104a1aabcbb4f151183d54d51dde07d09b3f222)、[DAI_TRIGGER_PRE_START](#ggaee6445967afb3ecf2c0470ca0c104a1aac7647bb0111f043abcdaa4b3e703b2ec)、[DAI_TRIGGER_STOP](#ggaee6445967afb3ecf2c0470ca0c104a1aa23dd7f534a18f92cbf12ad957674ba35)、[DAI_TRIGGER_PAUSE](#ggaee6445967afb3ecf2c0470ca0c104a1aadb17f3981cf0e248187c4006f527a3a5)、[DAI_TRIGGER_POST_STOP](#ggaee6445967afb3ecf2c0470ca0c104a1aad2fcfa3c229bfc0a82ec7841ab9f88c3)、[DAI_TRIGGER_DRAIN](#ggaee6445967afb3ecf2c0470ca0c104a1aa1c17da0f6a54c2c25f2dd2349b5c0e02)、[DAI_TRIGGER_DROP](#ggaee6445967afb3ecf2c0470ca0c104a1aa1f004f7d4dcb67d2c3a89298400b2234)、[DAI_TRIGGER_PREPARE](#ggaee6445967afb3ecf2c0470ca0c104a1aad9d4e12f62ee2e106abaeb3bb341ee70)、[DAI_TRIGGER_RESET](#ggaee6445967afb3ecf2c0470ca0c104a1aafa607dff411961ae22e44f1a972c4711)、[DAI_TRIGGER_COPY](#ggaee6445967afb3ecf2c0470ca0c104a1aa6720f67f3bc6ab62eacf986316df0a9f)。

触发命令（Trigger Command）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 6.6\_函数（Functions）

<a id="r_ga0be1a87283a39f697e1eb4b4ab4bcdfe"></a>

```c
int dai_probe (const struct device *dev)
```

相关声明：[dai_probe](#ga0be1a87283a39f697e1eb4b4ab4bcdfe)、[device](../device_reference/P002_设备对象结构.md)。

数字音频接口（DAI）驱动的探测操作（Probe Operation）。

<a id="r_ga28ecaa76e8c6f4c32ffec6d6368bada0"></a>

```c
int dai_remove (const struct device *dev)
```

相关声明：[dai_remove](#ga28ecaa76e8c6f4c32ffec6d6368bada0)、[device](../device_reference/P002_设备对象结构.md)。

数字音频接口（DAI）驱动的移除操作（Remove Operation）。

<a id="r_ga8e0fa728ad9353ed008ba293808ab371"></a>

```c
int dai_config_set (const struct device *dev, const struct dai_config *cfg, const void *bespoke_cfg, size_t size)
```

相关声明：[dai_config_set](#ga8e0fa728ad9353ed008ba293808ab371)、[device](../device_reference/P002_设备对象结构.md)、[dai_config](../audio_video_model_reference/P001_dai_config_结构体.md)。

数字音频接口（DAI）驱动的配置操作（Configure Operation）。

<a id="r_ga0b27e890e1612a8afaa7b59d5293dc51"></a>

```c
int dai_config_get (const struct device *dev, struct dai_config *cfg, enum dai_dir dir)
```

相关声明：[dai_config_get](#ga0b27e890e1612a8afaa7b59d5293dc51)、[device](../device_reference/P002_设备对象结构.md)、[dai_config](../audio_video_model_reference/P001_dai_config_结构体.md)、[dai_dir](#gafa7b22e4250c6479301fc657fea8a60f)。

获取数字音频接口（DAI）驱动的配置信息（Configuration Information）。

<a id="r_gac732c8b3e737ecca187f38e308d95724"></a>

```c
static const struct dai_properties * dai_get_properties (const struct device *dev, enum dai_dir dir, int stream_id)
```

相关声明：[dai_properties](../audio_video_model_reference/P003_dai_properties_结构体.md)、[dai_get_properties](#gac732c8b3e737ecca187f38e308d95724)、[device](../device_reference/P002_设备对象结构.md)、[dai_dir](#gafa7b22e4250c6479301fc657fea8a60f)。

获取数字音频接口（DAI）驱动的属性（Properties）。

<a id="r_gae6f142de581bbf17fa31cc9cefb695c6"></a>

```c
int dai_get_properties_copy (const struct device *dev, enum dai_dir dir, int stream_id, struct dai_properties *dst)
```

相关声明：[dai_get_properties_copy](#gae6f142de581bbf17fa31cc9cefb695c6)、[device](../device_reference/P002_设备对象结构.md)、[dai_dir](#gafa7b22e4250c6479301fc657fea8a60f)、[dai_properties](../audio_video_model_reference/P003_dai_properties_结构体.md)。

获取数字音频接口（DAI）驱动的属性（Properties）。

<a id="r_ga6d98d1f42bcaba0eefef41bc96a04bc5"></a>

```c
int dai_trigger (const struct device *dev, enum dai_dir dir, enum dai_trigger_cmd cmd)
```

相关声明：[dai_trigger](#ga6d98d1f42bcaba0eefef41bc96a04bc5)、[device](../device_reference/P002_设备对象结构.md)、[dai_dir](#gafa7b22e4250c6479301fc657fea8a60f)、[dai_trigger_cmd](#gaee6445967afb3ecf2c0470ca0c104a1a)、[cmd](../api_scoped_clock_topic_reference/P012_FT8xx 参考 API.md#gacde1ca3945cbe6c828f65051c5c3a615)。

发送触发命令（Trigger Command）。

<a id="r_ga222336d75578f180ccf7f46f977fc12c"></a>

```c
int dai_ts_config (const struct device *dev, struct dai_ts_cfg *cfg)
```

相关声明：[dai_ts_config](#ga222336d75578f180ccf7f46f977fc12c)、[device](../device_reference/P002_设备对象结构.md)、[dai_ts_cfg](../audio_video_model_reference/P004_dai_ts_cfg_结构体.md)。

配置所连接数字音频接口（DAI）的时间戳功能（Timestamping）。

<a id="r_ga1adb2bf389fea3483361eaea078a7262"></a>

```c
int dai_ts_start (const struct device *dev, struct dai_ts_cfg *cfg)
```

相关声明：[dai_ts_start](#ga1adb2bf389fea3483361eaea078a7262)、[device](../device_reference/P002_设备对象结构.md)、[dai_ts_cfg](../audio_video_model_reference/P004_dai_ts_cfg_结构体.md)。

启动时间戳功能（Timestamping）。

<a id="r_ga040f4515aa67efb3a840b9b5e323d016"></a>

```c
int dai_ts_stop (const struct device *dev, struct dai_ts_cfg *cfg)
```

相关声明：[dai_ts_stop](#ga040f4515aa67efb3a840b9b5e323d016)、[device](../device_reference/P002_设备对象结构.md)、[dai_ts_cfg](../audio_video_model_reference/P004_dai_ts_cfg_结构体.md)。

停止时间戳功能（Timestamping）。

<a id="r_ga6588501e0369ddf1bc4c04a2e293bc2b"></a>

```c
int dai_ts_get (const struct device *dev, struct dai_ts_cfg *cfg, struct dai_ts_data *tsd)
```

相关声明：[dai_ts_get](#ga6588501e0369ddf1bc4c04a2e293bc2b)、[device](../device_reference/P002_设备对象结构.md)、[dai_ts_cfg](../audio_video_model_reference/P004_dai_ts_cfg_结构体.md)、[dai_ts_data](../audio_video_model_reference/P005_dai_ts_data_结构体.md)。

获取时间戳（Timestamp）。

<a id="r_gae6cf280d796744e2626e7b706af89003"></a>

```c
int dai_config_update (const struct device *dev, const void *bespoke_cfg, size_t size)
```

相关声明：[dai_config_update](#gae6cf280d796744e2626e7b706af89003)、[device](../device_reference/P002_设备对象结构.md)。

在运行时更新数字音频接口（DAI）配置。

## 6.7\_详细说明（Detailed Documentation）

<a id="ga8891542769e33930342bb5039b57fda8"></a>

### `DAI_FORMAT_CLOCK_INVERSION_MASK`

```c
#define DAI_FORMAT_CLOCK_INVERSION_MASK 0x0f00
```

```c
#include <zephyr/drivers/dai.h>
```

用于从 `struct dai_config` 的 `format` 属性提取时钟反相设置（Clock Inversion）。

<a id="ga2a51e43f9a14435a64e428df0b393703"></a>

### `DAI_FORMAT_CLOCK_PROVIDER_MASK`

```c
#define DAI_FORMAT_CLOCK_PROVIDER_MASK 0xf000
```

```c
#include <zephyr/drivers/dai.h>
```

用于从 `struct dai_config` 的 `format` 属性提取时钟配置（Clock Configuration）。

<a id="gaef86b295b1a13cc91e53f8cdbb4cf008"></a>

### `DAI_FORMAT_PROTOCOL_MASK`

```c
#define DAI_FORMAT_PROTOCOL_MASK 0x000f
```

```c
#include <zephyr/drivers/dai.h>
```

用于从 `struct dai_config` 的 `format` 属性提取协议（Protocol）。

<a id="gaf66ca0bbc1f8ba2f2b81caf92bd09b60"></a>

### `dai_clock_inversion`

```c
enum dai_clock_inversion
```

```c
#include <zephyr/drivers/dai.h>
```

数字音频接口（DAI）时钟反相（Clock Inversion）。

某些应用可能需要不同于协议默认选择的时钟极性（Clock Polarity），涉及 FSYNC／BCLK。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `DAI_INVERSION_NB_NF` | BCLK 不反相，FSYNC 不反相（No Inversion）。 |
| `DAI_INVERSION_NB_IF` | BCLK 不反相，FSYNC 反相（Inversion）。 |
| `DAI_INVERSION_IB_NF` | BCLK 反相（Inversion），FSYNC 不反相。 |
| `DAI_INVERSION_IB_IF` | BCLK 反相，FSYNC 反相（Inversion）。 |

<a id="ga840116b8b56fd0263a17791e7156975d"></a>

### `dai_clock_provider`

```c
enum dai_clock_provider
```

```c
#include <zephyr/drivers/dai.h>
```

数字音频接口（DAI）时钟配置（Clock Configurations）。

用于描述 DAI 与编解码器（Codec）之间所有可能的时钟相关配置（Clock-related Configurations）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `DAI_CBP_CFP` | 编解码器提供 BCLK，也提供 FSYNC（Provider）。 |
| `DAI_CBC_CFP` | 编解码器使用外部 BCLK（Consumer），提供 FSYNC（Provider）。 |
| `DAI_CBP_CFC` | 编解码器提供 BCLK（Provider），使用外部 FSYNC（Consumer）。 |
| `DAI_CBC_CFC` | 编解码器使用外部 BCLK 和 FSYNC（Consumer）。 |

<a id="gafa7b22e4250c6479301fc657fea8a60f"></a>

### `dai_dir`

```c
enum dai_dir
```

```c
#include <zephyr/drivers/dai.h>
```

数字音频接口（DAI）方向（Direction）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `DAI_DIR_TX` | 发送数据（Transmit Data）。 |
| `DAI_DIR_RX` | 接收数据（Receive Data）。 |
| `DAI_DIR_BOTH` | 同时接收和发送数据（Receive and Transmit）。 |

<a id="ga3fa4c114ad6a3dd6a6015b6ab3d119a2"></a>

### `dai_protocol`

```c
enum dai_protocol
```

```c
#include <zephyr/drivers/dai.h>
```

数字音频接口（DAI）协议（Protocol）。

DAI 与编解码器（CODEC）之间的通信可能随使用场景采用不同协议（Protocol）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `DAI_PROTO_I2S` | 集成电路间音频总线（I2S） |
| `DAI_PROTO_RIGHT_J` | 右对齐（Right Justified）。 |
| `DAI_PROTO_LEFT_J` | 左对齐（Left Justified）。 |
| `DAI_PROTO_DSP_A` | 时分复用（TDM），FSYNC 提前 1 个 BCLK 有效。 |
| `DAI_PROTO_DSP_B` | 时分复用（TDM），FSYNC 与最高有效位（MSB）同时有效。 |
| `DAI_PROTO_PDM` | 脉冲密度调制（Pulse Density Modulation，PDM）。 |

<a id="ga18f708594ea85d6b893906336047c3a5"></a>

### `dai_state`

```c
enum dai_state
```

```c
#include <zephyr/drivers/dai.h>
```

接口状态（Interface State）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `DAI_STATE_NOT_READY` | 接口未就绪（Not Ready）。接口已初始化，但尚未就绪，不能接收／发送数据。调用 dai_config_set() 配置接口，并将其状态变为 READY。 |
| `DAI_STATE_READY` | 接口已准备好接收／发送数据（Ready）。 |
| `DAI_STATE_RUNNING` | 接口正在接收／发送数据。 |
| `DAI_STATE_PRE_RUNNING` | 接口时钟正在运行（Clocking），但不接收／发送数据。 |
| `DAI_STATE_PAUSED` | 接口已暂停（Paused）。 |
| `DAI_STATE_STOPPING` | 接口正在排空发送队列（Draining）。 |
| `DAI_STATE_ERROR` | 发生了发送缓冲区欠载（TX Buffer Underrun）或接收缓冲区溢出（RX Buffer Overrun）。 |

<a id="gaee6445967afb3ecf2c0470ca0c104a1a"></a>

### `dai_trigger_cmd`

```c
enum dai_trigger_cmd
```

```c
#include <zephyr/drivers/dai.h>
```

触发命令（Trigger Command）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `DAI_TRIGGER_START` | 开始数据发送／接收。如果设置了 DAI_DIR_TX，必须先通过 dai_write() 将一些待发送数据加入队列。此触发（Trigger）只能在 READY 状态使用，并将接口状态变为 RUNNING。 |
| `DAI_TRIGGER_PRE_START` | 可选：预启动（Pre Start）数据发送／接收。启动下游锁相环／锁频环（PLL／FLL）锁定所需的时钟，使 DAI 与下游编解码器（Codec）为音频发送／接收（Tx／Rx）做好准备。 |
| `DAI_TRIGGER_STOP` | 停止发送／接收数据。在当前内存块结束时停止发送／接收数据。此触发操作（Trigger）仅可在 `RUNNING` 状态使用，首先将接口状态改为 `STOPPING`。当前 TX／RX 块发送／接收完毕后，状态改为 `READY`。随后执行 `START` 触发操作将从停止的位置继续发送／接收。 |
| `DAI_TRIGGER_PAUSE` | 暂停（Pause）数据发送／接收。在当前内存块（Memory Block）结束时暂停。具体行为取决于实现，但通常该状态不会完全停止时钟或传输。DAI 可能持续发送 0（静音），但不会消耗外部提供的数据。 |
| `DAI_TRIGGER_POST_STOP` | 可选：执行数据发送／接收的后停止（Post Stop）操作。在音频发送／接收（Tx／Rx）之后，停止下游音频完成过程所需的时钟，使 DAI 与下游编解码器（Codec）正常关闭。 |
| `DAI_TRIGGER_DRAIN` | 清空发送队列（Transmit Queue）。发送队列中的全部数据，然后停止发送。若将此触发应用于 RX 队列，则效果与 DAI_TRIGGER_STOP 相同。此触发只能在 RUNNING 状态使用，首先将接口状态变为 STOPPING；发送完全部 TX 块后，状态变为 READY。 |
| `DAI_TRIGGER_DROP` | 丢弃发送／接收队列（Transmit/Receive Queue）。立即停止发送／接收，并丢弃相应队列中的内容。此触发操作可用于除 `NOT_READY` 以外的任何状态，并将接口状态改为 `READY`。 |
| `DAI_TRIGGER_PREPARE` | 发生欠载／溢出（Underrun/Overrun）错误后，准备队列。此触发操作仅可在 `ERROR` 状态使用，并将接口状态改为 `READY`。 |
| `DAI_TRIGGER_RESET` | 复位（Reset）。此触发释放资源，并使驱动回到初始状态（Initial State）。 |
| `DAI_TRIGGER_COPY` | 复制（Copy）。此触发为数据复制做准备。 |

<a id="gac95242d83a2c2b477fcb9eb3da420797"></a>

### `dai_type`

```c
enum dai_type
```

```c
#include <zephyr/drivers/dai.h>
```

数字音频接口类型（Types of DAI）。

DAI 的类型（Type）。此 ID 类型用于配置 DAI 专用硬件设置（Bespoke HW Settings）。

DAI 的物理链路特性（Physical Link Features）变化很多，因此需要不同的配置数据来适应不同使用场景。通常必须在 DAI 启动前传入额外的专用配置（Bespoke Configuration）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `DAI_LEGACY_I2S` | 与 i2s.h 兼容的传统 I2S（Legacy I2S）。 |
| `DAI_INTEL_SSP` | Intel 同步串行端口（SSP）。 |
| `DAI_INTEL_DMIC` | Intel 数字麦克风（DMIC）。 |
| `DAI_INTEL_HDA` | Intel 高清音频（HD/A）。 |
| `DAI_INTEL_ALH` | Intel 音频链路集线器（ALH）。 |
| `DAI_IMX_SAI` | i.MX 同步音频接口（SAI）。 |
| `DAI_IMX_ESAI` | i.MX 增强型串行音频接口（ESAI）。 |
| `DAI_AMD_BT` | AMD 蓝牙（BT）。 |
| `DAI_AMD_SP` | AMD 串行端口（SP）。 |
| `DAI_AMD_DMIC` | AMD 数字麦克风（DMIC）。 |
| `DAI_MEDIATEK_AFE` | MediaTek 音频前端（AFE）。 |
| `DAI_INTEL_SSP_NHLT` | 非高清音频链路表（NHLT）SSP。 |
| `DAI_INTEL_DMIC_NHLT` | 非高清音频链路表（NHLT）SSP。 |
| `DAI_INTEL_HDA_NHLT` | 非高清音频链路表（NHLT）Intel HD/A。 |
| `DAI_INTEL_ALH_NHLT` | 非高清音频链路表（NHLT）Intel ALH。 |
| `DAI_IMX_MICFIL` | i.MX 脉冲密度调制（PDM）MICFIL。 |
| `DAI_INTEL_UAOL` | Intel UAOL 接口。 |
| `DAI_AMD_SDW` | AMD SoundWire 接口。 |
| `DAI_AMD_TDM` | AMD 时分复用（TDM）。 |

<a id="ga0b27e890e1612a8afaa7b59d5293dc51"></a>

### `dai_config_get()`

```c
int dai_config_get ( const struct device * dev, struct dai_config * cfg, enum dai_dir dir )
```

```c
#include <zephyr/drivers/dai.h>
```

获取数字音频接口（DAI）驱动的配置信息（Configuration Information）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `cfg` | 指向由该实例填写的配置结构体（Config Structure）的指针。 |
| `dir` | 流方向（Stream Direction）：RX 或 TX，由 DAI_DIR_* 定义。 |

**返回（Returns）**：返回：成功时为 0；参数无效或 DAI 尚未配置时为负值。

<a id="ga8e0fa728ad9353ed008ba293808ab371"></a>

### `dai_config_set()`

```c
int dai_config_set ( const struct device * dev, const struct dai_config * cfg, const void * bespoke_cfg, size_t size )
```

```c
#include <zephyr/drivers/dai.h>
```

数字音频接口（DAI）驱动的配置操作（Configure Operation）。

`dir` 参数指定使用 `cfg` 参数提供的数据来配置发送（TX）方向还是接收（RX）方向。

此函数仅可在 `NOT_READY` 或 `READY` 状态调用。执行成功后，将接口状态改为 `READY`。

调用此函数时，若参数 cfg->rate 设为 0，则接口状态变为 NOT_READY。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `cfg` | 指向包含配置参数（Configuration Parameters）的结构体的指针。 |
| `bespoke_cfg` | 指向包含专用配置（Bespoke Config）的结构体的指针。 |
| `size` | 专用配置大小（Bespoke Config Size）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-EINVAL` | 参数无效（Invalid Argument）。 |
| `-ENOSYS` | 不支持 DAI_DIR_BOTH 值。 |

<a id="gae6cf280d796744e2626e7b706af89003"></a>

### `dai_config_update()`

```c
int dai_config_update ( const struct device * dev, const void * bespoke_cfg, size_t size )
```

```c
#include <zephyr/drivers/dai.h>
```

在运行时更新数字音频接口（DAI）配置。

此函数在运行时更新 DAI 接口配置，允许设置 DAI 实现特有的专用配置参数（Bespoke Configuration Parameters），从而在使用完整配置数据块的常规流程之外进行更新。专用配置的细节取决于各 DAI 实现。仅应在 DAI 处于 READY 状态时调用此函数，以确保在开始数据发送或接收之前应用配置更新。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `bespoke_cfg` | 指向包含专用配置参数（Bespoke Configuration Parameters）的缓冲区的指针。 |
| `size` | bespoke_cfg 缓冲区的大小，单位为字节。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-ENOSYS` | 未实现配置更新操作（Configuration Update Operation）。 |
| `<0` | 失败时为负 errno 错误码。 |

<a id="gac732c8b3e737ecca187f38e308d95724"></a>

### `dai_get_properties()`

```c
const struct dai_properties * dai_get_properties ( const struct device * dev, enum dai_dir dir, int stream_id )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/dai.h>
```

获取数字音频接口（DAI）驱动的属性（Properties）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `dir` | 流方向（Stream Direction）：RX 或 TX，由 DAI_DIR_* 定义。 |
| `stream_id` | 流 ID（Stream ID）：某些驱动具有特定于流的属性，该 ID 用于指定流。 |

**返回（Returns）**：返回：指向包含属性（Properties）的结构体的指针；发生错误或没有属性时为 NULL。

<a id="gae6f142de581bbf17fa31cc9cefb695c6"></a>

### `dai_get_properties_copy()`

```c
int dai_get_properties_copy ( const struct device * dev, enum dai_dir dir, int stream_id, struct dai_properties * dst )
```

```c
#include <zephyr/drivers/dai.h>
```

获取数字音频接口（DAI）驱动的属性（Properties）。

可选方法（Optional Method）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `dir` | 流方向（Stream Direction）：RX 或 TX，由 DAI_DIR_* 定义。 |
| `stream_id` | 流 ID（Stream ID）：某些驱动具有特定于流的属性，该 ID 用于指定流。 |
| `dst` | 用于写入属性（Properties）的地址。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-EINVAL` | 参数不正确。 |
| `-ENOENT` | 设备没有属性（Properties）。 |
| `-ENOSYS` | 驱动未实现此方法（Method）。 |

<a id="ga0be1a87283a39f697e1eb4b4ab4bcdfe"></a>

### `dai_probe()`

```c
int dai_probe ( const struct device * dev)
```

```c
#include <zephyr/drivers/dai.h>
```

数字音频接口（DAI）驱动的探测操作（Probe Operation）。

调用此函数以给设备上电（Power Up），并更新相关信息，例如可能存在的使用者引用计数（Reference Count）。还可用它初始化内部变量、分配内存。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |

<a id="ga28ecaa76e8c6f4c32ffec6d6368bada0"></a>

### `dai_remove()`

```c
int dai_remove ( const struct device * dev)
```

```c
#include <zephyr/drivers/dai.h>
```

数字音频接口（DAI）驱动的移除操作（Remove Operation）。

调用此函数以注销／解绑设备（Unregister / Unbind），例如给设备断电或减少使用引用计数（Usage Reference Count）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |

<a id="ga6d98d1f42bcaba0eefef41bc96a04bc5"></a>

### `dai_trigger()`

```c
int dai_trigger ( const struct device * dev, enum dai_dir dir, enum dai_trigger_cmd cmd )
```

```c
#include <zephyr/drivers/dai.h>
```

发送触发命令（Trigger Command）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `dir` | 流方向（Stream Direction）：RX、TX 或两者，由 DAI_DIR_* 定义。某些驱动可能不支持 DAI_DIR_BOTH；对这些驱动，须分别触发 RX 和 TX 流。 |
| `cmd` | 触发命令（Trigger Command）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-EINVAL` | 参数无效（Invalid Argument）。 |
| `-EIO` | 当前状态无法执行此触发操作（Trigger），或无法分配 DMA 通道。 |
| `-ENOMEM` | 接收／发送内存块（RX/TX Memory Block）不可用。 |
| `-ENOSYS` | 不支持 DAI_DIR_BOTH 值。 |

<a id="ga222336d75578f180ccf7f46f977fc12c"></a>

### `dai_ts_config()`

```c
int dai_ts_config ( const struct device * dev, struct dai_ts_cfg * cfg )
```

```c
#include <zephyr/drivers/dai.h>
```

配置所连接数字音频接口（DAI）的时间戳功能（Timestamping）。

可选方法（Optional Method）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 组件设备（Component Device）。 |
| `cfg` | 时间戳配置（Timestamp Config）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |

<a id="ga6588501e0369ddf1bc4c04a2e293bc2b"></a>

### `dai_ts_get()`

```c
int dai_ts_get ( const struct device * dev, struct dai_ts_cfg * cfg, struct dai_ts_data * tsd )
```

```c
#include <zephyr/drivers/dai.h>
```

获取时间戳（Timestamp）。

可选方法（Optional Method）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 组件设备（Component Device）。 |
| `cfg` | 时间戳配置（Timestamp Config）。 |
| `tsd` | 接收时间戳数据（Timestamp Data）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |

<a id="ga1adb2bf389fea3483361eaea078a7262"></a>

### `dai_ts_start()`

```c
int dai_ts_start ( const struct device * dev, struct dai_ts_cfg * cfg )
```

```c
#include <zephyr/drivers/dai.h>
```

启动时间戳功能（Timestamping）。

可选方法（Optional Method）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 组件设备（Component Device）。 |
| `cfg` | 时间戳配置（Timestamp Config）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |

<a id="ga040f4515aa67efb3a840b9b5e323d016"></a>

### `dai_ts_stop()`

```c
int dai_ts_stop ( const struct device * dev, struct dai_ts_cfg * cfg )
```

```c
#include <zephyr/drivers/dai.h>
```

停止时间戳功能（Timestamping）。

可选方法（Optional Method）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 组件设备（Component Device）。 |
| `cfg` | 时间戳配置（Timestamp Config）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |


## 6.8\_原页交叉引用（Cross References）

- [DAI 驱动后端 API（Driver Backend API）](../api_platform_topic_reference/P013_DAI 驱动后端 API（Driver Backend API）.md)
- [dai.h](../api_file_serial_motion_reference/P002_zephyr__drivers__dai.h_文件参考.md)
- [dai_properties](../audio_video_model_reference/P003_dai_properties_结构体.md)
- [dai_config](../audio_video_model_reference/P001_dai_config_结构体.md)
- [dai_ts_cfg](../audio_video_model_reference/P004_dai_ts_cfg_结构体.md)
- [dai_ts_data](../audio_video_model_reference/P005_dai_ts_data_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [cmd](../api_scoped_clock_topic_reference/P012_FT8xx 参考 API.md#gacde1ca3945cbe6c828f65051c5c3a615)
- [i2s.h](../api_file_display_chat_reference/P011_zephyr__drivers__i2s.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggaf66ca0bbc1f8ba2f2b81caf92bd09b60a35606eb43c6d77204bff029bfab37698"></a>
<a id="ggaf66ca0bbc1f8ba2f2b81caf92bd09b60ad6622f24986622cf16fdeada99356c43"></a>
<a id="ggaf66ca0bbc1f8ba2f2b81caf92bd09b60ae0a56f8334363d4a1aa916ffe5d70e5c"></a>
<a id="ggaf66ca0bbc1f8ba2f2b81caf92bd09b60ab35554010caadb69a5414c7f07649ee1"></a>
<a id="gga840116b8b56fd0263a17791e7156975da347440e41adadd2b6a91076f53abe2e3"></a>
<a id="gga840116b8b56fd0263a17791e7156975daf4862a3af6fb46f6ac9ffc0cdbbcf0a1"></a>
<a id="gga840116b8b56fd0263a17791e7156975da4baee3a3ab87e540b5f4caf26e8d8c4b"></a>
<a id="gga840116b8b56fd0263a17791e7156975da9f8f99d63e607d9603f54d535bd89f84"></a>
<a id="ggafa7b22e4250c6479301fc657fea8a60fadfdf2212e2d86296dbccc60cfd60368c"></a>
<a id="ggafa7b22e4250c6479301fc657fea8a60fa48cc817cda4907b94a03e13e8b9aa69b"></a>
<a id="ggafa7b22e4250c6479301fc657fea8a60fa58581d875a6a8c28adb0f6351a37f3e1"></a>
<a id="gga3fa4c114ad6a3dd6a6015b6ab3d119a2adf515857c95ea685a32bf18c0ebb9af2"></a>
<a id="gga3fa4c114ad6a3dd6a6015b6ab3d119a2a9ed5273ee9ea0761ccf9cbc7f7295a3f"></a>
<a id="gga3fa4c114ad6a3dd6a6015b6ab3d119a2a0d0f5db48e33cef8aa6c59a00792866b"></a>
<a id="gga3fa4c114ad6a3dd6a6015b6ab3d119a2a6ffdc334c0f64feeb95297293f747bc3"></a>
<a id="gga3fa4c114ad6a3dd6a6015b6ab3d119a2aea1fd67c47f7d8d7e3ca18b2f2e806a0"></a>
<a id="gga3fa4c114ad6a3dd6a6015b6ab3d119a2a3235bf6888b65c9c6e3a0d2f95fc0758"></a>
<a id="gga18f708594ea85d6b893906336047c3a5a8486be6ff6f6bf91ee4a8ad632377987"></a>
<a id="gga18f708594ea85d6b893906336047c3a5a095422b1a71b65e5a5902e0ca5cd3650"></a>
<a id="gga18f708594ea85d6b893906336047c3a5a8692bbb3fce619aec3dfe5ed9697f73f"></a>
<a id="gga18f708594ea85d6b893906336047c3a5a234306cd9cc97674455f8a9321834953"></a>
<a id="gga18f708594ea85d6b893906336047c3a5acb4e0c1f9df9eb0b7cf965b710a2ad13"></a>
<a id="gga18f708594ea85d6b893906336047c3a5aba10f89376d67abdc3dc704c6b283d2b"></a>
<a id="gga18f708594ea85d6b893906336047c3a5a5030da046fda46120d9b54a686fb35ef"></a>
<a id="ggaee6445967afb3ecf2c0470ca0c104a1aabcbb4f151183d54d51dde07d09b3f222"></a>
<a id="ggaee6445967afb3ecf2c0470ca0c104a1aac7647bb0111f043abcdaa4b3e703b2ec"></a>
<a id="ggaee6445967afb3ecf2c0470ca0c104a1aa23dd7f534a18f92cbf12ad957674ba35"></a>
<a id="ggaee6445967afb3ecf2c0470ca0c104a1aadb17f3981cf0e248187c4006f527a3a5"></a>
<a id="ggaee6445967afb3ecf2c0470ca0c104a1aad2fcfa3c229bfc0a82ec7841ab9f88c3"></a>
<a id="ggaee6445967afb3ecf2c0470ca0c104a1aa1c17da0f6a54c2c25f2dd2349b5c0e02"></a>
<a id="ggaee6445967afb3ecf2c0470ca0c104a1aa1f004f7d4dcb67d2c3a89298400b2234"></a>
<a id="ggaee6445967afb3ecf2c0470ca0c104a1aad9d4e12f62ee2e106abaeb3bb341ee70"></a>
<a id="ggaee6445967afb3ecf2c0470ca0c104a1aafa607dff411961ae22e44f1a972c4711"></a>
<a id="ggaee6445967afb3ecf2c0470ca0c104a1aa6720f67f3bc6ab62eacf986316df0a9f"></a>
<a id="ggac95242d83a2c2b477fcb9eb3da420797a2560d8f844796f647ed774748c44adfe"></a>
<a id="ggac95242d83a2c2b477fcb9eb3da420797a9301e2ec67fa75aefc0e59df727adcc9"></a>
<a id="ggac95242d83a2c2b477fcb9eb3da420797a366db52bd49557d047f091cdb96b5e36"></a>
<a id="ggac95242d83a2c2b477fcb9eb3da420797a1a591d4c0b7a70e175fc967b59929326"></a>
<a id="ggac95242d83a2c2b477fcb9eb3da420797a19dd111b0d7f7772415bc60c1256d141"></a>
<a id="ggac95242d83a2c2b477fcb9eb3da420797aa94ef995d95f9d0ad8b404e26b79faec"></a>
<a id="ggac95242d83a2c2b477fcb9eb3da420797a75bfaa3859321a283929ae033fcf22aa"></a>
<a id="ggac95242d83a2c2b477fcb9eb3da420797a6c0c4b31c71c9e779a2a9325dc119fd0"></a>
<a id="ggac95242d83a2c2b477fcb9eb3da420797ab675d7b5204a2cbc09f1f60a44f4ff3b"></a>
<a id="ggac95242d83a2c2b477fcb9eb3da420797a37f79dfe1804d4abeb89a9767bf37c75"></a>
<a id="ggac95242d83a2c2b477fcb9eb3da420797ac5095e399162d248e638b87a61b59a00"></a>
<a id="ggac95242d83a2c2b477fcb9eb3da420797a8d75b1d72f5fcff348c15281001f9aaa"></a>
<a id="ggac95242d83a2c2b477fcb9eb3da420797a3d759f9665a4db0c974913c4aa71e6f2"></a>
<a id="ggac95242d83a2c2b477fcb9eb3da420797afd1f617fdd16363c1a10e9f45a67a99b"></a>
<a id="ggac95242d83a2c2b477fcb9eb3da420797a2a12c2858722c553cb31f24aacd83976"></a>
<a id="ggac95242d83a2c2b477fcb9eb3da420797a15cf161a5126110860c89ce9a118045b"></a>
<a id="ggac95242d83a2c2b477fcb9eb3da420797a6d88cd52faa8d93716f81d68fabb794d"></a>
<a id="ggac95242d83a2c2b477fcb9eb3da420797ae58e4acd79cd16d98976fef1978a231c"></a>
<a id="ggac95242d83a2c2b477fcb9eb3da420797ab63816ace8bc3fc6f35d0435fd37931e"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P005_对象传输服务（Object Transfer Service，OTS）.md) · [返回大纲](大纲.md) · [下一章](P007_域名解析库（DNS Resolve Library）.md)

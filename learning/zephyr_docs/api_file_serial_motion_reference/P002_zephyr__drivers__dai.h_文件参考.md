---
id: learning.zephyr-docs.api-file-serial-motion-reference.page-2
title: zephyr__drivers__dai.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dai_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_zephyr\_\_drivers\_\_dai.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/dai_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

数字音频接口（Digital Audio Interface，DAI）驱动API的主头文件。

<a id="details"></a>

```c
#include <errno.h>
#include <zephyr/types.h>
#include <zephyr/device.h>
#include <zephyr/syscalls/dai.h>
```

查看此文件的源码。

数字音频接口（Digital Audio Interface，DAI）驱动API的主头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 2.1\_数据结构（Data Structures）

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

<a id="r_dai_5Fdriver_5Fapi"></a>

```c
struct dai_driver_api
```

相关声明：[dai_driver_api](../audio_video_model_reference/P002_dai_driver_api_结构体.md)。

驱动操作（Driver Operations）：数字音频接口（DAI）驱动操作。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 2.2\_宏定义（Macros）

<a id="r_ga2a51e43f9a14435a64e428df0b393703"></a>

```c
#define DAI_FORMAT_CLOCK_PROVIDER_MASK 0xf000
```

相关声明：[DAI_FORMAT_CLOCK_PROVIDER_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ga2a51e43f9a14435a64e428df0b393703)。

用于从 `struct dai_config` 的 `format` 属性提取时钟配置（Clock Configuration）。

<a id="r_gaef86b295b1a13cc91e53f8cdbb4cf008"></a>

```c
#define DAI_FORMAT_PROTOCOL_MASK 0x000f
```

相关声明：[DAI_FORMAT_PROTOCOL_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gaef86b295b1a13cc91e53f8cdbb4cf008)。

用于从 `struct dai_config` 的 `format` 属性提取协议（Protocol）。

<a id="r_ga8891542769e33930342bb5039b57fda8"></a>

```c
#define DAI_FORMAT_CLOCK_INVERSION_MASK 0x0f00
```

相关声明：[DAI_FORMAT_CLOCK_INVERSION_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ga8891542769e33930342bb5039b57fda8)。

用于从 `struct dai_config` 的 `format` 属性提取时钟反相设置（Clock Inversion）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 2.3\_枚举（Enumerations）

<a id="r_ga840116b8b56fd0263a17791e7156975d"></a>

```c
enum dai_clock_provider { DAI_CBP_CFP = (0 << 12) , DAI_CBC_CFP = (2 << 12) , DAI_CBP_CFC = (3 << 12) , DAI_CBC_CFC = (4 << 12) }
```

相关声明：[dai_clock_provider](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ga840116b8b56fd0263a17791e7156975d)、[DAI_CBP_CFP](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gga840116b8b56fd0263a17791e7156975da347440e41adadd2b6a91076f53abe2e3)、[DAI_CBC_CFP](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gga840116b8b56fd0263a17791e7156975daf4862a3af6fb46f6ac9ffc0cdbbcf0a1)、[DAI_CBP_CFC](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gga840116b8b56fd0263a17791e7156975da4baee3a3ab87e540b5f4caf26e8d8c4b)、[DAI_CBC_CFC](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gga840116b8b56fd0263a17791e7156975da9f8f99d63e607d9603f54d535bd89f84)。

数字音频接口（DAI）时钟配置（Clock Configurations）。

<a id="r_ga3fa4c114ad6a3dd6a6015b6ab3d119a2"></a>

```c
enum dai_protocol { DAI_PROTO_I2S = 1 , DAI_PROTO_RIGHT_J , DAI_PROTO_LEFT_J , DAI_PROTO_DSP_A , DAI_PROTO_DSP_B , DAI_PROTO_PDM }
```

相关声明：[dai_protocol](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ga3fa4c114ad6a3dd6a6015b6ab3d119a2)、[DAI_PROTO_I2S](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gga3fa4c114ad6a3dd6a6015b6ab3d119a2adf515857c95ea685a32bf18c0ebb9af2)、[DAI_PROTO_RIGHT_J](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gga3fa4c114ad6a3dd6a6015b6ab3d119a2a9ed5273ee9ea0761ccf9cbc7f7295a3f)、[DAI_PROTO_LEFT_J](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gga3fa4c114ad6a3dd6a6015b6ab3d119a2a0d0f5db48e33cef8aa6c59a00792866b)、[DAI_PROTO_DSP_A](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gga3fa4c114ad6a3dd6a6015b6ab3d119a2a6ffdc334c0f64feeb95297293f747bc3)、[DAI_PROTO_DSP_B](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gga3fa4c114ad6a3dd6a6015b6ab3d119a2aea1fd67c47f7d8d7e3ca18b2f2e806a0)、[DAI_PROTO_PDM](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gga3fa4c114ad6a3dd6a6015b6ab3d119a2a3235bf6888b65c9c6e3a0d2f95fc0758)。

数字音频接口（DAI）协议（Protocol）。

<a id="r_gaf66ca0bbc1f8ba2f2b81caf92bd09b60"></a>

```c
enum dai_clock_inversion { DAI_INVERSION_NB_NF = 0 , DAI_INVERSION_NB_IF = (2 << 8) , DAI_INVERSION_IB_NF = (3 << 8) , DAI_INVERSION_IB_IF = (4 << 8) }
```

相关声明：[dai_clock_inversion](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gaf66ca0bbc1f8ba2f2b81caf92bd09b60)、[DAI_INVERSION_NB_NF](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggaf66ca0bbc1f8ba2f2b81caf92bd09b60a35606eb43c6d77204bff029bfab37698)、[DAI_INVERSION_NB_IF](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggaf66ca0bbc1f8ba2f2b81caf92bd09b60ad6622f24986622cf16fdeada99356c43)、[DAI_INVERSION_IB_NF](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggaf66ca0bbc1f8ba2f2b81caf92bd09b60ae0a56f8334363d4a1aa916ffe5d70e5c)、[DAI_INVERSION_IB_IF](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggaf66ca0bbc1f8ba2f2b81caf92bd09b60ab35554010caadb69a5414c7f07649ee1)。

数字音频接口（DAI）时钟反相（Clock Inversion）。

<a id="r_gac95242d83a2c2b477fcb9eb3da420797"></a>

```c
enum dai_type { DAI_LEGACY_I2S = 0 , DAI_INTEL_SSP , DAI_INTEL_DMIC , DAI_INTEL_HDA , DAI_INTEL_ALH , DAI_IMX_SAI , DAI_IMX_ESAI , DAI_AMD_BT , DAI_AMD_SP , DAI_AMD_DMIC , DAI_MEDIATEK_AFE , DAI_INTEL_SSP_NHLT , DAI_INTEL_DMIC_NHLT , DAI_INTEL_HDA_NHLT , DAI_INTEL_ALH_NHLT , DAI_IMX_MICFIL , DAI_INTEL_UAOL , DAI_AMD_SDW , DAI_AMD_TDM }
```

相关声明：[dai_type](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gac95242d83a2c2b477fcb9eb3da420797)、[DAI_LEGACY_I2S](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggac95242d83a2c2b477fcb9eb3da420797a2560d8f844796f647ed774748c44adfe)、[DAI_INTEL_SSP](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggac95242d83a2c2b477fcb9eb3da420797a9301e2ec67fa75aefc0e59df727adcc9)、[DAI_INTEL_DMIC](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggac95242d83a2c2b477fcb9eb3da420797a366db52bd49557d047f091cdb96b5e36)、[DAI_INTEL_HDA](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggac95242d83a2c2b477fcb9eb3da420797a1a591d4c0b7a70e175fc967b59929326)、[DAI_INTEL_ALH](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggac95242d83a2c2b477fcb9eb3da420797a19dd111b0d7f7772415bc60c1256d141)、[DAI_IMX_SAI](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggac95242d83a2c2b477fcb9eb3da420797aa94ef995d95f9d0ad8b404e26b79faec)、[DAI_IMX_ESAI](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggac95242d83a2c2b477fcb9eb3da420797a75bfaa3859321a283929ae033fcf22aa)、[DAI_AMD_BT](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggac95242d83a2c2b477fcb9eb3da420797a6c0c4b31c71c9e779a2a9325dc119fd0)、[DAI_AMD_SP](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggac95242d83a2c2b477fcb9eb3da420797ab675d7b5204a2cbc09f1f60a44f4ff3b)、[DAI_AMD_DMIC](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggac95242d83a2c2b477fcb9eb3da420797a37f79dfe1804d4abeb89a9767bf37c75)、[DAI_MEDIATEK_AFE](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggac95242d83a2c2b477fcb9eb3da420797ac5095e399162d248e638b87a61b59a00)、[DAI_INTEL_SSP_NHLT](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggac95242d83a2c2b477fcb9eb3da420797a8d75b1d72f5fcff348c15281001f9aaa)、[DAI_INTEL_DMIC_NHLT](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggac95242d83a2c2b477fcb9eb3da420797a3d759f9665a4db0c974913c4aa71e6f2)、[DAI_INTEL_HDA_NHLT](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggac95242d83a2c2b477fcb9eb3da420797afd1f617fdd16363c1a10e9f45a67a99b)、[DAI_INTEL_ALH_NHLT](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggac95242d83a2c2b477fcb9eb3da420797a2a12c2858722c553cb31f24aacd83976)、[DAI_IMX_MICFIL](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggac95242d83a2c2b477fcb9eb3da420797a15cf161a5126110860c89ce9a118045b)、[DAI_INTEL_UAOL](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggac95242d83a2c2b477fcb9eb3da420797a6d88cd52faa8d93716f81d68fabb794d)、[DAI_AMD_SDW](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggac95242d83a2c2b477fcb9eb3da420797ae58e4acd79cd16d98976fef1978a231c)、[DAI_AMD_TDM](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggac95242d83a2c2b477fcb9eb3da420797ab63816ace8bc3fc6f35d0435fd37931e)。

数字音频接口类型（Types of DAI）。

<a id="r_gafa7b22e4250c6479301fc657fea8a60f"></a>

```c
enum dai_dir { DAI_DIR_TX = 0 , DAI_DIR_RX , DAI_DIR_BOTH }
```

相关声明：[dai_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gafa7b22e4250c6479301fc657fea8a60f)、[DAI_DIR_TX](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggafa7b22e4250c6479301fc657fea8a60fadfdf2212e2d86296dbccc60cfd60368c)、[DAI_DIR_RX](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggafa7b22e4250c6479301fc657fea8a60fa48cc817cda4907b94a03e13e8b9aa69b)、[DAI_DIR_BOTH](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggafa7b22e4250c6479301fc657fea8a60fa58581d875a6a8c28adb0f6351a37f3e1)。

数字音频接口（DAI）方向（Direction）。

<a id="r_ga18f708594ea85d6b893906336047c3a5"></a>

```c
enum dai_state { DAI_STATE_NOT_READY = 0 , DAI_STATE_READY , DAI_STATE_RUNNING , DAI_STATE_PRE_RUNNING , DAI_STATE_PAUSED , DAI_STATE_STOPPING , DAI_STATE_ERROR }
```

相关声明：[dai_state](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ga18f708594ea85d6b893906336047c3a5)、[DAI_STATE_NOT_READY](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gga18f708594ea85d6b893906336047c3a5a8486be6ff6f6bf91ee4a8ad632377987)、[DAI_STATE_READY](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gga18f708594ea85d6b893906336047c3a5a095422b1a71b65e5a5902e0ca5cd3650)、[DAI_STATE_RUNNING](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gga18f708594ea85d6b893906336047c3a5a8692bbb3fce619aec3dfe5ed9697f73f)、[DAI_STATE_PRE_RUNNING](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gga18f708594ea85d6b893906336047c3a5a234306cd9cc97674455f8a9321834953)、[DAI_STATE_PAUSED](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gga18f708594ea85d6b893906336047c3a5acb4e0c1f9df9eb0b7cf965b710a2ad13)、[DAI_STATE_STOPPING](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gga18f708594ea85d6b893906336047c3a5aba10f89376d67abdc3dc704c6b283d2b)、[DAI_STATE_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gga18f708594ea85d6b893906336047c3a5a5030da046fda46120d9b54a686fb35ef)。

接口状态（Interface State）。

<a id="r_gaee6445967afb3ecf2c0470ca0c104a1a"></a>

```c
enum dai_trigger_cmd { DAI_TRIGGER_START = 0 , DAI_TRIGGER_PRE_START , DAI_TRIGGER_STOP , DAI_TRIGGER_PAUSE , DAI_TRIGGER_POST_STOP , DAI_TRIGGER_DRAIN , DAI_TRIGGER_DROP , DAI_TRIGGER_PREPARE , DAI_TRIGGER_RESET , DAI_TRIGGER_COPY }
```

相关声明：[dai_trigger_cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gaee6445967afb3ecf2c0470ca0c104a1a)、[DAI_TRIGGER_START](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggaee6445967afb3ecf2c0470ca0c104a1aabcbb4f151183d54d51dde07d09b3f222)、[DAI_TRIGGER_PRE_START](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggaee6445967afb3ecf2c0470ca0c104a1aac7647bb0111f043abcdaa4b3e703b2ec)、[DAI_TRIGGER_STOP](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggaee6445967afb3ecf2c0470ca0c104a1aa23dd7f534a18f92cbf12ad957674ba35)、[DAI_TRIGGER_PAUSE](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggaee6445967afb3ecf2c0470ca0c104a1aadb17f3981cf0e248187c4006f527a3a5)、[DAI_TRIGGER_POST_STOP](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggaee6445967afb3ecf2c0470ca0c104a1aad2fcfa3c229bfc0a82ec7841ab9f88c3)、[DAI_TRIGGER_DRAIN](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggaee6445967afb3ecf2c0470ca0c104a1aa1c17da0f6a54c2c25f2dd2349b5c0e02)、[DAI_TRIGGER_DROP](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggaee6445967afb3ecf2c0470ca0c104a1aa1f004f7d4dcb67d2c3a89298400b2234)、[DAI_TRIGGER_PREPARE](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggaee6445967afb3ecf2c0470ca0c104a1aad9d4e12f62ee2e106abaeb3bb341ee70)、[DAI_TRIGGER_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggaee6445967afb3ecf2c0470ca0c104a1aafa607dff411961ae22e44f1a972c4711)、[DAI_TRIGGER_COPY](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggaee6445967afb3ecf2c0470ca0c104a1aa6720f67f3bc6ab62eacf986316df0a9f)。

触发命令（Trigger Command）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 2.4\_函数（Functions）

<a id="r_ga0be1a87283a39f697e1eb4b4ab4bcdfe"></a>

```c
int dai_probe (const struct device *dev)
```

相关声明：[dai_probe](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ga0be1a87283a39f697e1eb4b4ab4bcdfe)、[device](../device_reference/P002_设备对象结构.md)。

数字音频接口（DAI）驱动的探测操作（Probe Operation）。

<a id="r_ga28ecaa76e8c6f4c32ffec6d6368bada0"></a>

```c
int dai_remove (const struct device *dev)
```

相关声明：[dai_remove](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ga28ecaa76e8c6f4c32ffec6d6368bada0)、[device](../device_reference/P002_设备对象结构.md)。

数字音频接口（DAI）驱动的移除操作（Remove Operation）。

<a id="r_ga8e0fa728ad9353ed008ba293808ab371"></a>

```c
int dai_config_set (const struct device *dev, const struct dai_config *cfg, const void *bespoke_cfg, size_t size)
```

相关声明：[dai_config_set](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ga8e0fa728ad9353ed008ba293808ab371)、[device](../device_reference/P002_设备对象结构.md)、[dai_config](../audio_video_model_reference/P001_dai_config_结构体.md)。

数字音频接口（DAI）驱动的配置操作（Configure Operation）。

<a id="r_ga0b27e890e1612a8afaa7b59d5293dc51"></a>

```c
int dai_config_get (const struct device *dev, struct dai_config *cfg, enum dai_dir dir)
```

相关声明：[dai_config_get](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ga0b27e890e1612a8afaa7b59d5293dc51)、[device](../device_reference/P002_设备对象结构.md)、[dai_config](../audio_video_model_reference/P001_dai_config_结构体.md)、[dai_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gafa7b22e4250c6479301fc657fea8a60f)。

获取数字音频接口（DAI）驱动的配置信息（Configuration Information）。

<a id="r_gac732c8b3e737ecca187f38e308d95724"></a>

```c
static const struct dai_properties * dai_get_properties (const struct device *dev, enum dai_dir dir, int stream_id)
```

相关声明：[dai_properties](../audio_video_model_reference/P003_dai_properties_结构体.md)、[dai_get_properties](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gac732c8b3e737ecca187f38e308d95724)、[device](../device_reference/P002_设备对象结构.md)、[dai_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gafa7b22e4250c6479301fc657fea8a60f)。

获取数字音频接口（DAI）驱动的属性（Properties）。

<a id="r_gae6f142de581bbf17fa31cc9cefb695c6"></a>

```c
int dai_get_properties_copy (const struct device *dev, enum dai_dir dir, int stream_id, struct dai_properties *dst)
```

相关声明：[dai_get_properties_copy](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gae6f142de581bbf17fa31cc9cefb695c6)、[device](../device_reference/P002_设备对象结构.md)、[dai_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gafa7b22e4250c6479301fc657fea8a60f)、[dai_properties](../audio_video_model_reference/P003_dai_properties_结构体.md)。

获取数字音频接口（DAI）驱动的属性（Properties）。

<a id="r_ga6d98d1f42bcaba0eefef41bc96a04bc5"></a>

```c
int dai_trigger (const struct device *dev, enum dai_dir dir, enum dai_trigger_cmd cmd)
```

相关声明：[dai_trigger](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ga6d98d1f42bcaba0eefef41bc96a04bc5)、[device](../device_reference/P002_设备对象结构.md)、[dai_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gafa7b22e4250c6479301fc657fea8a60f)、[dai_trigger_cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gaee6445967afb3ecf2c0470ca0c104a1a)、[cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)。

发送触发命令（Trigger Command）。

<a id="r_ga222336d75578f180ccf7f46f977fc12c"></a>

```c
int dai_ts_config (const struct device *dev, struct dai_ts_cfg *cfg)
```

相关声明：[dai_ts_config](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ga222336d75578f180ccf7f46f977fc12c)、[device](../device_reference/P002_设备对象结构.md)、[dai_ts_cfg](../audio_video_model_reference/P004_dai_ts_cfg_结构体.md)。

配置所连接数字音频接口（DAI）的时间戳功能（Timestamping）。

<a id="r_ga1adb2bf389fea3483361eaea078a7262"></a>

```c
int dai_ts_start (const struct device *dev, struct dai_ts_cfg *cfg)
```

相关声明：[dai_ts_start](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ga1adb2bf389fea3483361eaea078a7262)、[device](../device_reference/P002_设备对象结构.md)、[dai_ts_cfg](../audio_video_model_reference/P004_dai_ts_cfg_结构体.md)。

启动时间戳功能（Timestamping）。

<a id="r_ga040f4515aa67efb3a840b9b5e323d016"></a>

```c
int dai_ts_stop (const struct device *dev, struct dai_ts_cfg *cfg)
```

相关声明：[dai_ts_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ga040f4515aa67efb3a840b9b5e323d016)、[device](../device_reference/P002_设备对象结构.md)、[dai_ts_cfg](../audio_video_model_reference/P004_dai_ts_cfg_结构体.md)。

停止时间戳功能（Timestamping）。

<a id="r_ga6588501e0369ddf1bc4c04a2e293bc2b"></a>

```c
int dai_ts_get (const struct device *dev, struct dai_ts_cfg *cfg, struct dai_ts_data *tsd)
```

相关声明：[dai_ts_get](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ga6588501e0369ddf1bc4c04a2e293bc2b)、[device](../device_reference/P002_设备对象结构.md)、[dai_ts_cfg](../audio_video_model_reference/P004_dai_ts_cfg_结构体.md)、[dai_ts_data](../audio_video_model_reference/P005_dai_ts_data_结构体.md)。

获取时间戳（Timestamp）。

<a id="r_gae6cf280d796744e2626e7b706af89003"></a>

```c
int dai_config_update (const struct device *dev, const void *bespoke_cfg, size_t size)
```

相关声明：[dai_config_update](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gae6cf280d796744e2626e7b706af89003)、[device](../device_reference/P002_设备对象结构.md)。

在运行时更新数字音频接口（DAI）配置。


## 2.5\_原页交叉引用（Cross References）

- [errno.h](../error_reference/P005_错误号头文件源码.md)
- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P120_dai.h_源码浏览.md)
- [dai_properties](../audio_video_model_reference/P003_dai_properties_结构体.md)
- [dai_config](../audio_video_model_reference/P001_dai_config_结构体.md)
- [dai_ts_cfg](../audio_video_model_reference/P004_dai_ts_cfg_结构体.md)
- [dai_ts_data](../audio_video_model_reference/P005_dai_ts_data_结构体.md)
- [dai_driver_api](../audio_video_model_reference/P002_dai_driver_api_结构体.md)
- [DAI_FORMAT_CLOCK_PROVIDER_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ga2a51e43f9a14435a64e428df0b393703)
- [DAI_FORMAT_PROTOCOL_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gaef86b295b1a13cc91e53f8cdbb4cf008)
- [DAI_FORMAT_CLOCK_INVERSION_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ga8891542769e33930342bb5039b57fda8)
- [dai_clock_provider](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ga840116b8b56fd0263a17791e7156975d)
- [DAI_CBP_CFP](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gga840116b8b56fd0263a17791e7156975da347440e41adadd2b6a91076f53abe2e3)
- [DAI_CBC_CFP](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gga840116b8b56fd0263a17791e7156975daf4862a3af6fb46f6ac9ffc0cdbbcf0a1)
- [DAI_CBP_CFC](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gga840116b8b56fd0263a17791e7156975da4baee3a3ab87e540b5f4caf26e8d8c4b)
- [DAI_CBC_CFC](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gga840116b8b56fd0263a17791e7156975da9f8f99d63e607d9603f54d535bd89f84)
- [dai_protocol](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ga3fa4c114ad6a3dd6a6015b6ab3d119a2)
- [DAI_PROTO_I2S](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gga3fa4c114ad6a3dd6a6015b6ab3d119a2adf515857c95ea685a32bf18c0ebb9af2)
- [DAI_PROTO_RIGHT_J](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gga3fa4c114ad6a3dd6a6015b6ab3d119a2a9ed5273ee9ea0761ccf9cbc7f7295a3f)
- [DAI_PROTO_LEFT_J](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gga3fa4c114ad6a3dd6a6015b6ab3d119a2a0d0f5db48e33cef8aa6c59a00792866b)
- [DAI_PROTO_DSP_A](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gga3fa4c114ad6a3dd6a6015b6ab3d119a2a6ffdc334c0f64feeb95297293f747bc3)
- [DAI_PROTO_DSP_B](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gga3fa4c114ad6a3dd6a6015b6ab3d119a2aea1fd67c47f7d8d7e3ca18b2f2e806a0)
- [DAI_PROTO_PDM](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gga3fa4c114ad6a3dd6a6015b6ab3d119a2a3235bf6888b65c9c6e3a0d2f95fc0758)
- [dai_clock_inversion](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gaf66ca0bbc1f8ba2f2b81caf92bd09b60)
- [DAI_INVERSION_NB_NF](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggaf66ca0bbc1f8ba2f2b81caf92bd09b60a35606eb43c6d77204bff029bfab37698)
- [DAI_INVERSION_NB_IF](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggaf66ca0bbc1f8ba2f2b81caf92bd09b60ad6622f24986622cf16fdeada99356c43)
- [DAI_INVERSION_IB_NF](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggaf66ca0bbc1f8ba2f2b81caf92bd09b60ae0a56f8334363d4a1aa916ffe5d70e5c)
- [DAI_INVERSION_IB_IF](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggaf66ca0bbc1f8ba2f2b81caf92bd09b60ab35554010caadb69a5414c7f07649ee1)
- [dai_type](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gac95242d83a2c2b477fcb9eb3da420797)
- [DAI_LEGACY_I2S](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggac95242d83a2c2b477fcb9eb3da420797a2560d8f844796f647ed774748c44adfe)
- [DAI_INTEL_SSP](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggac95242d83a2c2b477fcb9eb3da420797a9301e2ec67fa75aefc0e59df727adcc9)
- [DAI_INTEL_DMIC](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggac95242d83a2c2b477fcb9eb3da420797a366db52bd49557d047f091cdb96b5e36)
- [DAI_INTEL_HDA](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggac95242d83a2c2b477fcb9eb3da420797a1a591d4c0b7a70e175fc967b59929326)
- [DAI_INTEL_ALH](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggac95242d83a2c2b477fcb9eb3da420797a19dd111b0d7f7772415bc60c1256d141)
- [DAI_IMX_SAI](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggac95242d83a2c2b477fcb9eb3da420797aa94ef995d95f9d0ad8b404e26b79faec)
- [DAI_IMX_ESAI](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggac95242d83a2c2b477fcb9eb3da420797a75bfaa3859321a283929ae033fcf22aa)
- [DAI_AMD_BT](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggac95242d83a2c2b477fcb9eb3da420797a6c0c4b31c71c9e779a2a9325dc119fd0)
- [DAI_AMD_SP](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggac95242d83a2c2b477fcb9eb3da420797ab675d7b5204a2cbc09f1f60a44f4ff3b)
- [DAI_AMD_DMIC](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggac95242d83a2c2b477fcb9eb3da420797a37f79dfe1804d4abeb89a9767bf37c75)
- [DAI_MEDIATEK_AFE](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggac95242d83a2c2b477fcb9eb3da420797ac5095e399162d248e638b87a61b59a00)
- [DAI_INTEL_SSP_NHLT](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggac95242d83a2c2b477fcb9eb3da420797a8d75b1d72f5fcff348c15281001f9aaa)
- [DAI_INTEL_DMIC_NHLT](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggac95242d83a2c2b477fcb9eb3da420797a3d759f9665a4db0c974913c4aa71e6f2)
- [DAI_INTEL_HDA_NHLT](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggac95242d83a2c2b477fcb9eb3da420797afd1f617fdd16363c1a10e9f45a67a99b)
- [DAI_INTEL_ALH_NHLT](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggac95242d83a2c2b477fcb9eb3da420797a2a12c2858722c553cb31f24aacd83976)
- [DAI_IMX_MICFIL](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggac95242d83a2c2b477fcb9eb3da420797a15cf161a5126110860c89ce9a118045b)
- [DAI_INTEL_UAOL](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggac95242d83a2c2b477fcb9eb3da420797a6d88cd52faa8d93716f81d68fabb794d)
- [DAI_AMD_SDW](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggac95242d83a2c2b477fcb9eb3da420797ae58e4acd79cd16d98976fef1978a231c)
- [DAI_AMD_TDM](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggac95242d83a2c2b477fcb9eb3da420797ab63816ace8bc3fc6f35d0435fd37931e)
- [dai_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gafa7b22e4250c6479301fc657fea8a60f)
- [DAI_DIR_TX](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggafa7b22e4250c6479301fc657fea8a60fadfdf2212e2d86296dbccc60cfd60368c)
- [DAI_DIR_RX](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggafa7b22e4250c6479301fc657fea8a60fa48cc817cda4907b94a03e13e8b9aa69b)
- [DAI_DIR_BOTH](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggafa7b22e4250c6479301fc657fea8a60fa58581d875a6a8c28adb0f6351a37f3e1)
- [dai_state](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ga18f708594ea85d6b893906336047c3a5)
- [DAI_STATE_NOT_READY](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gga18f708594ea85d6b893906336047c3a5a8486be6ff6f6bf91ee4a8ad632377987)
- [DAI_STATE_READY](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gga18f708594ea85d6b893906336047c3a5a095422b1a71b65e5a5902e0ca5cd3650)
- [DAI_STATE_RUNNING](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gga18f708594ea85d6b893906336047c3a5a8692bbb3fce619aec3dfe5ed9697f73f)
- [DAI_STATE_PRE_RUNNING](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gga18f708594ea85d6b893906336047c3a5a234306cd9cc97674455f8a9321834953)
- [DAI_STATE_PAUSED](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gga18f708594ea85d6b893906336047c3a5acb4e0c1f9df9eb0b7cf965b710a2ad13)
- [DAI_STATE_STOPPING](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gga18f708594ea85d6b893906336047c3a5aba10f89376d67abdc3dc704c6b283d2b)
- [DAI_STATE_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gga18f708594ea85d6b893906336047c3a5a5030da046fda46120d9b54a686fb35ef)
- [dai_trigger_cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gaee6445967afb3ecf2c0470ca0c104a1a)
- [DAI_TRIGGER_START](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggaee6445967afb3ecf2c0470ca0c104a1aabcbb4f151183d54d51dde07d09b3f222)
- [DAI_TRIGGER_PRE_START](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggaee6445967afb3ecf2c0470ca0c104a1aac7647bb0111f043abcdaa4b3e703b2ec)
- [DAI_TRIGGER_STOP](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggaee6445967afb3ecf2c0470ca0c104a1aa23dd7f534a18f92cbf12ad957674ba35)
- [DAI_TRIGGER_PAUSE](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggaee6445967afb3ecf2c0470ca0c104a1aadb17f3981cf0e248187c4006f527a3a5)
- [DAI_TRIGGER_POST_STOP](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggaee6445967afb3ecf2c0470ca0c104a1aad2fcfa3c229bfc0a82ec7841ab9f88c3)
- [DAI_TRIGGER_DRAIN](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggaee6445967afb3ecf2c0470ca0c104a1aa1c17da0f6a54c2c25f2dd2349b5c0e02)
- [DAI_TRIGGER_DROP](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggaee6445967afb3ecf2c0470ca0c104a1aa1f004f7d4dcb67d2c3a89298400b2234)
- [DAI_TRIGGER_PREPARE](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggaee6445967afb3ecf2c0470ca0c104a1aad9d4e12f62ee2e106abaeb3bb341ee70)
- [DAI_TRIGGER_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggaee6445967afb3ecf2c0470ca0c104a1aafa607dff411961ae22e44f1a972c4711)
- [DAI_TRIGGER_COPY](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggaee6445967afb3ecf2c0470ca0c104a1aa6720f67f3bc6ab62eacf986316df0a9f)
- [dai_probe](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ga0be1a87283a39f697e1eb4b4ab4bcdfe)
- [device](../device_reference/P002_设备对象结构.md)
- [dai_remove](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ga28ecaa76e8c6f4c32ffec6d6368bada0)
- [dai_config_set](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ga8e0fa728ad9353ed008ba293808ab371)
- [dai_config_get](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ga0b27e890e1612a8afaa7b59d5293dc51)
- [dai_get_properties](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gac732c8b3e737ecca187f38e308d95724)
- [dai_get_properties_copy](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gae6f142de581bbf17fa31cc9cefb695c6)
- [dai_trigger](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ga6d98d1f42bcaba0eefef41bc96a04bc5)
- [cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)
- [dai_ts_config](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ga222336d75578f180ccf7f46f977fc12c)
- [dai_ts_start](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ga1adb2bf389fea3483361eaea078a7262)
- [dai_ts_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ga040f4515aa67efb3a840b9b5e323d016)
- [dai_ts_get](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ga6588501e0369ddf1bc4c04a2e293bc2b)
- [dai_config_update](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gae6cf280d796744e2626e7b706af89003)

<a id="header-details"></a>

---

[上一章](P001_zephyr__console__tty.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P003_zephyr__drivers__gnss.h_文件参考.md)

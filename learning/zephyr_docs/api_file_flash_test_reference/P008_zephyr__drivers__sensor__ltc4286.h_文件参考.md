---
id: learning.zephyr-docs.api-file-flash-test-reference.page-8
title: zephyr__drivers__sensor__ltc4286.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ltc4286_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_zephyr\_\_drivers\_\_sensor\_\_ltc4286.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ltc4286_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

LTC4286传感器的扩展API头文件（Extended Sensor API Header）。

<a id="details"></a>

```c
#include <zephyr/types.h>
#include <zephyr/drivers/sensor.h>
```

查看此文件的源码。

LTC4286传感器的扩展API头文件（Extended Sensor API Header）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 8.1\_枚举（Enumerations）

<a id="r_gacfbf1c312a894cb8a9d796c910bf296e"></a>

```c
enum ltc4286_sensor_chan { SENSOR_CHAN_LTC4286_VIN = SENSOR_CHAN_PRIV_START , SENSOR_CHAN_LTC4286_ADC , SENSOR_CHAN_LTC4286_CONFIG , SENSOR_CHAN_LTC4286_END }
```

相关声明：[ltc4286_sensor_chan](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gacfbf1c312a894cb8a9d796c910bf296e)、[SENSOR_CHAN_LTC4286_VIN](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggacfbf1c312a894cb8a9d796c910bf296ea9611723fa128ef9b1d50ffc855e73555)、[SENSOR_CHAN_LTC4286_ADC](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggacfbf1c312a894cb8a9d796c910bf296ea7c56dcb401d4a1d31ed8ad48cca34e18)、[SENSOR_CHAN_LTC4286_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggacfbf1c312a894cb8a9d796c910bf296eae4375736913710f0bf8520045dd43dbd)、[SENSOR_CHAN_LTC4286_END](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggacfbf1c312a894cb8a9d796c910bf296eaf00f43f28f525bdd5720ddda9fd93b01)。

LTC4286 自定义传感器通道（Custom Sensor Channels）。

<a id="r_ga39fb4460d62a29a7171a6fee309f7e82"></a>

```c
enum ltc4286_trig_chan { SENSOR_CHAN_LTC4286_TRIG_POWER_GOOD , SENSOR_CHAN_LTC4286_TRIG_COMPARATOR , SENSOR_CHAN_LTC4286_TRIG_ALERT , SENSOR_CHAN_LTC4286_TRIG_END }
```

相关声明：[ltc4286_trig_chan](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ga39fb4460d62a29a7171a6fee309f7e82)、[SENSOR_CHAN_LTC4286_TRIG_POWER_GOOD](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga39fb4460d62a29a7171a6fee309f7e82ab763321fa67df532ef7bc6071522f4a5)、[SENSOR_CHAN_LTC4286_TRIG_COMPARATOR](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga39fb4460d62a29a7171a6fee309f7e82a5148bf77a9771e4f9de694eacbb2b52e)、[SENSOR_CHAN_LTC4286_TRIG_ALERT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga39fb4460d62a29a7171a6fee309f7e82a63f553a0bd36f2c92b24dc565768f10d)、[SENSOR_CHAN_LTC4286_TRIG_END](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga39fb4460d62a29a7171a6fee309f7e82a2a60329f625a951282498f0602b39429)。

LTC4286 中断源的触发通道（Trigger Channels）。

<a id="r_gaba2a3212fcfafcf12bf40fa6ac9a441f"></a>

```c
enum ltc4286_status_chan { SENSOR_CHAN_LTC4286_STATUS , SENSOR_CHAN_LTC4286_STATUS_VOUT , SENSOR_CHAN_LTC4286_STATUS_IOUT , SENSOR_CHAN_LTC4286_STATUS_INPUT , SENSOR_CHAN_LTC4286_STATUS_TEMP , SENSOR_CHAN_LTC4286_STATUS_CML , SENSOR_CHAN_LTC4286_STATUS_OTHER , SENSOR_CHAN_LTC4286_STATUS_MFR_SPEC , SENSOR_CHAN_LTC4286_STATUS_MFR_SYS_STATUS1 , SENSOR_CHAN_LTC4286_STATUS_MFR_SYS_STATUS2 , SENSOR_CHAN_LTC4286_STATUS_END }
```

相关声明：[ltc4286_status_chan](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gaba2a3212fcfafcf12bf40fa6ac9a441f)、[SENSOR_CHAN_LTC4286_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggaba2a3212fcfafcf12bf40fa6ac9a441fabff42a316554a78cce7c19d2767f6e68)、[SENSOR_CHAN_LTC4286_STATUS_VOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggaba2a3212fcfafcf12bf40fa6ac9a441fa8b9de62a5fd40e1bf76431dee84da14e)、[SENSOR_CHAN_LTC4286_STATUS_IOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggaba2a3212fcfafcf12bf40fa6ac9a441fa7ea188de23481a157d184eb361750b73)、[SENSOR_CHAN_LTC4286_STATUS_INPUT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggaba2a3212fcfafcf12bf40fa6ac9a441faa44da14585661383c7a0ec752db7ff18)、[SENSOR_CHAN_LTC4286_STATUS_TEMP](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggaba2a3212fcfafcf12bf40fa6ac9a441fa4d7b333ae63f31bb0b7f694cc098fe3d)、[SENSOR_CHAN_LTC4286_STATUS_CML](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggaba2a3212fcfafcf12bf40fa6ac9a441fa62e4dc6f4798d810167fd57006734090)、[SENSOR_CHAN_LTC4286_STATUS_OTHER](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggaba2a3212fcfafcf12bf40fa6ac9a441fa8587e0c8fe248edf784cba06c0f03148)、[SENSOR_CHAN_LTC4286_STATUS_MFR_SPEC](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggaba2a3212fcfafcf12bf40fa6ac9a441fa2e28f2362b8970258ada962fa3ace3a8)、[SENSOR_CHAN_LTC4286_STATUS_MFR_SYS_STATUS1](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggaba2a3212fcfafcf12bf40fa6ac9a441fa4e0e1dd867882f71f9e2150c13c65248)、[SENSOR_CHAN_LTC4286_STATUS_MFR_SYS_STATUS2](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggaba2a3212fcfafcf12bf40fa6ac9a441fae98f32b16cd9e4e054c3926e09002fa0)、[SENSOR_CHAN_LTC4286_STATUS_END](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggaba2a3212fcfafcf12bf40fa6ac9a441fadd16c3074a8460252ebbc6529be8579b)。

LTC4286 状态寄存器通道（Status Register Channels）。

<a id="r_ga3664558c0fae3685405ef754201c05c5"></a>

```c
enum ltc4286_mfr_chan { SENSOR_CHAN_LTC4286_MFR_CONFIG = SENSOR_CHAN_LTC4286_STATUS_END , SENSOR_CHAN_LTC4286_MFR_FLT_CONFIG , SENSOR_CHAN_LTC4286_MFR_PMB_STATUS , SENSOR_CHAN_LTC4286_MFR_PADS_LIVE_STATUS , SENSOR_CHAN_LTC4286_MFR_COMMON , SENSOR_CHAN_LTC4286_MFR_REBOOT_CONTROL , SENSOR_CHAN_LTC4286_MFR_SHUTDOWN_CAUSE , SENSOR_CHAN_LTC4286_MFR_END }
```

相关声明：[ltc4286_mfr_chan](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ga3664558c0fae3685405ef754201c05c5)、[SENSOR_CHAN_LTC4286_MFR_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga3664558c0fae3685405ef754201c05c5a48ae0d2df8804a920d8d439201be3f76)、[SENSOR_CHAN_LTC4286_MFR_FLT_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga3664558c0fae3685405ef754201c05c5ae22b5b4f105253f11350f32cf142496d)、[SENSOR_CHAN_LTC4286_MFR_PMB_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga3664558c0fae3685405ef754201c05c5a89ba0ad4cfac235d9eabbc8b617108cc)、[SENSOR_CHAN_LTC4286_MFR_PADS_LIVE_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga3664558c0fae3685405ef754201c05c5a785ac7ea8b666842f514f2e923e7da85)、[SENSOR_CHAN_LTC4286_MFR_COMMON](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga3664558c0fae3685405ef754201c05c5a50253d61a47c5d174bb991e4458c9ad8)、[SENSOR_CHAN_LTC4286_MFR_REBOOT_CONTROL](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga3664558c0fae3685405ef754201c05c5a4d6045f94cebbcc5862f535bd950cedc)、[SENSOR_CHAN_LTC4286_MFR_SHUTDOWN_CAUSE](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga3664558c0fae3685405ef754201c05c5a14f3038f12d9e11212b2aa3f4f28ad66)、[SENSOR_CHAN_LTC4286_MFR_END](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga3664558c0fae3685405ef754201c05c5a33c7b2566d02ba6cdbd4eaedddf16484)。

LTC4286 厂商专用配置通道（Manufacturer-specific Configuration Channels）。

<a id="r_ga9f50fb92d66bf9766aaa08e8937c53d8"></a>

```c
enum ltc4286_fault_response_chan { SENSOR_CHAN_LTC4286_FAULT_RESP_FET = SENSOR_CHAN_LTC4286_MFR_END , SENSOR_CHAN_LTC4286_FAULT_RESP_END }
```

相关声明：[ltc4286_fault_response_chan](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ga9f50fb92d66bf9766aaa08e8937c53d8)、[SENSOR_CHAN_LTC4286_FAULT_RESP_FET](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga9f50fb92d66bf9766aaa08e8937c53d8abd349590c733d2bc0ea4df82c07ee97a)、[SENSOR_CHAN_LTC4286_FAULT_RESP_END](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga9f50fb92d66bf9766aaa08e8937c53d8aa984ae896e5fd0de445ba821ef953975)。

LTC4286 故障响应配置通道（Fault Response Configuration Channels）。

<a id="r_ga648a72bf8571828c76f2502890b5792c"></a>

```c
enum ltc4286_config_attr { SENSOR_ATTR_LTC4286_CONFIG_OPERATION = SENSOR_ATTR_PRIV_START , SENSOR_ATTR_LTC4286_CONFIG_CLEAR_FAULTS , SENSOR_ATTR_LTC4286_CONFIG_WRITE_PROTECT , SENSOR_ATTR_LTC4286_CONFIG_END }
```

相关声明：[ltc4286_config_attr](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ga648a72bf8571828c76f2502890b5792c)、[SENSOR_ATTR_LTC4286_CONFIG_OPERATION](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga648a72bf8571828c76f2502890b5792cac1f645ee0e5d57e2e69f0014d861b2de)、[SENSOR_ATTR_LTC4286_CONFIG_CLEAR_FAULTS](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga648a72bf8571828c76f2502890b5792ca521e057ea28c7b8a341bdc1b915c799e)、[SENSOR_ATTR_LTC4286_CONFIG_WRITE_PROTECT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga648a72bf8571828c76f2502890b5792ca3509b911f31ce00998f015d7964a515d)、[SENSOR_ATTR_LTC4286_CONFIG_END](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga648a72bf8571828c76f2502890b5792ca0f07ea708da2f26ec732832b5500039d)。

LTC4286 配置属性（Configuration Attributes）。

<a id="r_gab354bb88b1c78717d85702a73541af1d"></a>

```c
enum ltc4286_status_attr { SENSOR_ATTR_LTC4286_STATUS_VOUT = SENSOR_ATTR_LTC4286_CONFIG_END , SENSOR_ATTR_LTC4286_STATUS_IOUT , SENSOR_ATTR_LTC4286_STATUS_INPUT , SENSOR_ATTR_LTC4286_STATUS_MFRSPEC , SENSOR_ATTR_LTC4286_STATUS_PG , SENSOR_ATTR_LTC4286_STATUS_OTHER , SENSOR_ATTR_LTC4286_STATUS_UNKNOWN , SENSOR_ATTR_LTC4286_STATUS_BUSY , SENSOR_ATTR_LTC4286_STATUS_OFF , SENSOR_ATTR_LTC4286_STATUS_IOUT_OC , SENSOR_ATTR_LTC4286_STATUS_VIN_UV , SENSOR_ATTR_LTC4286_STATUS_TEMP , SENSOR_ATTR_LTC4286_STATUS_CML , SENSOR_ATTR_LTC4286_STATUS_NOT_CLEAR , SENSOR_ATTR_LTC4286_STATUS_END }
```

相关声明：[ltc4286_status_attr](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gab354bb88b1c78717d85702a73541af1d)、[SENSOR_ATTR_LTC4286_STATUS_VOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggab354bb88b1c78717d85702a73541af1da6af831ea19e18e6659d1da7c67151f47)、[SENSOR_ATTR_LTC4286_STATUS_IOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggab354bb88b1c78717d85702a73541af1daf17e252d1124aa6c02dbdd5567128bc9)、[SENSOR_ATTR_LTC4286_STATUS_INPUT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggab354bb88b1c78717d85702a73541af1da0b131dae831a6b147b4ccca8aa816666)、[SENSOR_ATTR_LTC4286_STATUS_MFRSPEC](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggab354bb88b1c78717d85702a73541af1da3570149b2d45c32d4dc184de37776ff7)、[SENSOR_ATTR_LTC4286_STATUS_PG](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggab354bb88b1c78717d85702a73541af1da0db72574d917f22385d9b8ff2d1cc3fb)、[SENSOR_ATTR_LTC4286_STATUS_OTHER](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggab354bb88b1c78717d85702a73541af1dab37db70c1caadb4b556348ad99df1865)、[SENSOR_ATTR_LTC4286_STATUS_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggab354bb88b1c78717d85702a73541af1da5c39e27197da8cb25262de092402eba8)、[SENSOR_ATTR_LTC4286_STATUS_BUSY](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggab354bb88b1c78717d85702a73541af1da97878e0008bd7a1f56f6915e26b995c6)、[SENSOR_ATTR_LTC4286_STATUS_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggab354bb88b1c78717d85702a73541af1da9d5df56313e243060854649f7c41ff17)、[SENSOR_ATTR_LTC4286_STATUS_IOUT_OC](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggab354bb88b1c78717d85702a73541af1da7a07f03ba0244311f05571351c2ec76f)、[SENSOR_ATTR_LTC4286_STATUS_VIN_UV](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggab354bb88b1c78717d85702a73541af1daea9511cef4322ba6fc60004359373555)、[SENSOR_ATTR_LTC4286_STATUS_TEMP](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggab354bb88b1c78717d85702a73541af1da16924f500d4d18dcee894a2903983c6a)、[SENSOR_ATTR_LTC4286_STATUS_CML](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggab354bb88b1c78717d85702a73541af1dae14003b2fb9a321614aad48adfdbdd26)、[SENSOR_ATTR_LTC4286_STATUS_NOT_CLEAR](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggab354bb88b1c78717d85702a73541af1da427c27fba79e310f030c3568717e95ec)、[SENSOR_ATTR_LTC4286_STATUS_END](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggab354bb88b1c78717d85702a73541af1da083f748a6a433c49b00744983376dc23)。

LTC4286 通用状态字属性（General Status Word Attributes）。

<a id="r_ga6a529f1c24665a30a5ef81bcc7afce00"></a>

```c
enum ltc4286_status_vout_attr { SENSOR_ATTR_LTC4286_STATUS_VOUT_OV = SENSOR_ATTR_LTC4286_STATUS_END , SENSOR_ATTR_LTC4286_STATUS_VOUT_UV , SENSOR_ATTR_LTC4286_STATUS_VOUT_END }
```

相关声明：[ltc4286_status_vout_attr](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ga6a529f1c24665a30a5ef81bcc7afce00)、[SENSOR_ATTR_LTC4286_STATUS_VOUT_OV](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga6a529f1c24665a30a5ef81bcc7afce00a8e181ac73a9c23cbd9d88f0c442f11b9)、[SENSOR_ATTR_LTC4286_STATUS_VOUT_UV](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga6a529f1c24665a30a5ef81bcc7afce00a31d1451ea1c64e80e1253e3ec044a621)、[SENSOR_ATTR_LTC4286_STATUS_VOUT_END](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga6a529f1c24665a30a5ef81bcc7afce00a0d6e73324e4af4f8f4091c0bcb543d85)。

LTC4286 输出电压状态属性（Output Voltage Status Attributes）。

<a id="r_ga842e114c954b3a9cf827c822dafb1604"></a>

```c
enum ltc4286_status_iout_attr { SENSOR_ATTR_LTC4286_STATUS_IOUT_OC_FAULT = SENSOR_ATTR_LTC4286_STATUS_VOUT_END , SENSOR_ATTR_LTC4286_STATUS_IOUT_OC_WARN , SENSOR_ATTR_LTC4286_STATUS_IOUT_END }
```

相关声明：[ltc4286_status_iout_attr](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ga842e114c954b3a9cf827c822dafb1604)、[SENSOR_ATTR_LTC4286_STATUS_IOUT_OC_FAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga842e114c954b3a9cf827c822dafb1604abfd7a92938c1b8343a6fcc759fa4c011)、[SENSOR_ATTR_LTC4286_STATUS_IOUT_OC_WARN](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga842e114c954b3a9cf827c822dafb1604aa84944f5ac9074488d4b2550d2e9ae5b)、[SENSOR_ATTR_LTC4286_STATUS_IOUT_END](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga842e114c954b3a9cf827c822dafb1604ace0e6881a6771cc414dfddceb8331d5d)。

LTC4286 输出电流状态属性（Output Current Status Attributes）。

<a id="r_gac8e200c73c25bfbb1749eaa0f9e99eaf"></a>

```c
enum ltc4286_status_input_attr { SENSOR_ATTR_LTC4286_STATUS_VIN_OV_FAULT = SENSOR_ATTR_LTC4286_STATUS_IOUT_END , SENSOR_ATTR_LTC4286_STATUS_VIN_OV_WARN , SENSOR_ATTR_LTC4286_STATUS_VIN_UV_FAULT , SENSOR_ATTR_LTC4286_STATUS_VIN_UV_WARN , SENSOR_ATTR_LTC4286_STATUS_PIN_OP_WARN , SENSOR_ATTR_LTC4286_STATUS_INPUT_END }
```

相关声明：[ltc4286_status_input_attr](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gac8e200c73c25bfbb1749eaa0f9e99eaf)、[SENSOR_ATTR_LTC4286_STATUS_VIN_OV_FAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggac8e200c73c25bfbb1749eaa0f9e99eafa5ae7bd1dafe774396844c2b8b4230bab)、[SENSOR_ATTR_LTC4286_STATUS_VIN_OV_WARN](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggac8e200c73c25bfbb1749eaa0f9e99eafa756a7624990568f6730fea52f9eccb34)、[SENSOR_ATTR_LTC4286_STATUS_VIN_UV_FAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggac8e200c73c25bfbb1749eaa0f9e99eafa1df817f7f3851c387b1f115e28cb58d1)、[SENSOR_ATTR_LTC4286_STATUS_VIN_UV_WARN](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggac8e200c73c25bfbb1749eaa0f9e99eafaa1d93e8f91e6cf92999577612cad28b8)、[SENSOR_ATTR_LTC4286_STATUS_PIN_OP_WARN](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggac8e200c73c25bfbb1749eaa0f9e99eafa90502ea2a99ec5801101701faad57d93)、[SENSOR_ATTR_LTC4286_STATUS_INPUT_END](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggac8e200c73c25bfbb1749eaa0f9e99eafaef961684248efc937f0e4ae252085921)。

LTC4286 输入电压／功率状态属性（Input Voltage/Power Status Attributes）。

<a id="r_ga0c5c7496b1504cc0e87b6dd43363d672"></a>

```c
enum ltc4286_status_temp_attr { SENSOR_ATTR_LTC4286_STATUS_TEMP_OT_FAULT = SENSOR_ATTR_LTC4286_STATUS_INPUT_END , SENSOR_ATTR_LTC4286_STATUS_TEMP_OT_WARN , SENSOR_ATTR_LTC4286_STATUS_TEMP_UT_WARN , SENSOR_ATTR_LTC4286_STATUS_TEMP_END }
```

相关声明：[ltc4286_status_temp_attr](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ga0c5c7496b1504cc0e87b6dd43363d672)、[SENSOR_ATTR_LTC4286_STATUS_TEMP_OT_FAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga0c5c7496b1504cc0e87b6dd43363d672af2bb9cf3df964985d24456d81b2d4726)、[SENSOR_ATTR_LTC4286_STATUS_TEMP_OT_WARN](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga0c5c7496b1504cc0e87b6dd43363d672a42e9a9956e22fbbd0b8d71314d93ee10)、[SENSOR_ATTR_LTC4286_STATUS_TEMP_UT_WARN](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga0c5c7496b1504cc0e87b6dd43363d672a24fb6b3901d05bb4e7c34616889855cc)、[SENSOR_ATTR_LTC4286_STATUS_TEMP_END](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga0c5c7496b1504cc0e87b6dd43363d672a870a0fb2537908f0654e00a87cf30cde)。

LTC4286 温度状态属性（Temperature Status Attributes）。

<a id="r_ga4fd75f925b184e14d2451dfc4c480bf3"></a>

```c
enum ltc4286_status_cml_attr { SENSOR_ATTR_LTC4286_STATUS_CML_BAD_CMD = SENSOR_ATTR_LTC4286_STATUS_TEMP_END , SENSOR_ATTR_LTC4286_STATUS_CML_BAD_DATA , SENSOR_ATTR_LTC4286_STATUS_CML_BAD_PEC_FAIL , SENSOR_ATTR_LTC4286_STATUS_CML_MISC_FAULT , SENSOR_ATTR_LTC4286_STATUS_CML_END }
```

相关声明：[ltc4286_status_cml_attr](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ga4fd75f925b184e14d2451dfc4c480bf3)、[SENSOR_ATTR_LTC4286_STATUS_CML_BAD_CMD](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga4fd75f925b184e14d2451dfc4c480bf3a4b9df926c3a00ff0d5468a4eb8b0e663)、[SENSOR_ATTR_LTC4286_STATUS_CML_BAD_DATA](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga4fd75f925b184e14d2451dfc4c480bf3a27743758a50b029c327a8cf08e5bcc06)、[SENSOR_ATTR_LTC4286_STATUS_CML_BAD_PEC_FAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga4fd75f925b184e14d2451dfc4c480bf3ae86c062286e1b40d827484a33e0425a5)、[SENSOR_ATTR_LTC4286_STATUS_CML_MISC_FAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga4fd75f925b184e14d2451dfc4c480bf3aa95ce2242074826d6a0c9feb89adef49)、[SENSOR_ATTR_LTC4286_STATUS_CML_END](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga4fd75f925b184e14d2451dfc4c480bf3aea30aecd662487674a9c2e801b597ecd)。

LTC4286 通信／命令状态属性（Communication/Command Status Attributes）。

<a id="r_ga1f8bec0c84f5ffdc2b0ab6e049987df8"></a>

```c
enum ltc4286_status_mfr_spec_attr { SENSOR_ATTR_LTC4286_STATUS_MFR_SPEC_EN_CHANGED = SENSOR_ATTR_LTC4286_STATUS_CML_END , SENSOR_ATTR_LTC4286_STATUS_MFR_SPEC_TSD_FAULT , SENSOR_ATTR_LTC4286_STATUS_MFR_SPEC_VDD_UVLO , SENSOR_ATTR_LTC4286_STATUS_MFR_SPEC_PIN_OP2_FAULT , SENSOR_ATTR_LTC4286_STATUS_MFR_SPEC_PIN_OP1_FAULT , SENSOR_ATTR_LTC4286_STATUS_MFR_SPEC_FET_BAD_FAULT , SENSOR_ATTR_LTC4286_STATUS_MFR_SPEC_END }
```

相关声明：[ltc4286_status_mfr_spec_attr](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ga1f8bec0c84f5ffdc2b0ab6e049987df8)、[SENSOR_ATTR_LTC4286_STATUS_MFR_SPEC_EN_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga1f8bec0c84f5ffdc2b0ab6e049987df8aa37f746bf6a18fdb33f8968c160be9bf)、[SENSOR_ATTR_LTC4286_STATUS_MFR_SPEC_TSD_FAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga1f8bec0c84f5ffdc2b0ab6e049987df8a2e5299de14b2ea6c65f519c32ec0e46c)、[SENSOR_ATTR_LTC4286_STATUS_MFR_SPEC_VDD_UVLO](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga1f8bec0c84f5ffdc2b0ab6e049987df8abd5691720d953779171f049ff4113c6f)、[SENSOR_ATTR_LTC4286_STATUS_MFR_SPEC_PIN_OP2_FAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga1f8bec0c84f5ffdc2b0ab6e049987df8ae12ba54d704e2575923650969194dc2e)、[SENSOR_ATTR_LTC4286_STATUS_MFR_SPEC_PIN_OP1_FAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga1f8bec0c84f5ffdc2b0ab6e049987df8a1a4e883e855c4c524dcd1c2fc0a26072)、[SENSOR_ATTR_LTC4286_STATUS_MFR_SPEC_FET_BAD_FAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga1f8bec0c84f5ffdc2b0ab6e049987df8a19ca2f34e4452c983823a725cffde402)、[SENSOR_ATTR_LTC4286_STATUS_MFR_SPEC_END](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga1f8bec0c84f5ffdc2b0ab6e049987df8ab8a25e6a1ef623417920b50971de1d34)。

LTC4286 厂商专用状态属性（Manufacturer-specific Status Attributes）。

<a id="r_ga85039255a2611470ce1a2293f8a0f9b1"></a>

```c
enum ltc4286_status_other_attr { SENSOR_ATTR_LTC4286_STATUS_OTHER_FIRST_ALERT = SENSOR_ATTR_LTC4286_STATUS_MFR_SPEC_END , SENSOR_ATTR_LTC4286_STATUS_OTHER_END }
```

相关声明：[ltc4286_status_other_attr](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ga85039255a2611470ce1a2293f8a0f9b1)、[SENSOR_ATTR_LTC4286_STATUS_OTHER_FIRST_ALERT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga85039255a2611470ce1a2293f8a0f9b1a825d75e525060c2fb7ffbe51bfa67db5)、[SENSOR_ATTR_LTC4286_STATUS_OTHER_END](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga85039255a2611470ce1a2293f8a0f9b1a17c5101095c645f91dd465eb4c5aacfa)。

LTC4286 其他状态属性（Other Status Attributes）。

<a id="r_ga6eedfb02e2dca41346990a7e28d6fdb6"></a>

```c
enum ltc4286_status_mfr_sys_status_attr { SENSOR_ATTR_LTC4286_STATUS_MFR_SYS_STAT1_ALERT = SENSOR_ATTR_LTC4286_STATUS_OTHER_END , SENSOR_ATTR_LTC4286_STATUS_MFR_SYS_STAT1_L_ALERT , SENSOR_ATTR_LTC4286_STATUS_MFR_SYS_POWER_LOSS , SENSOR_ATTR_LTC4286_STATUS_MFR_SYS_RESET_DONE , SENSOR_ATTR_LTC4286_STATUS_MFR_SYS_AVG_DONE , SENSOR_ATTR_LTC4286_STATUS_MFR_SYS_ADC_CONV , SENSOR_ATTR_LTC4286_STATUS_MFR_SYS_STAT2_SET , SENSOR_ATTR_LTC4286_STATUS_MFR_SYS_POWER_FAILED_WARN , SENSOR_ATTR_LTC4286_STATUS_MFR_SYS_FET_SHORT_WARN , SENSOR_ATTR_LTC4286_STATUS_MFR_SYS_VDS_UV_WARN , SENSOR_ATTR_LTC4286_STATUS_MFR_SYS_VDS_OV_WARN , SENSOR_ATTR_LTC4286_STATUS_MFR_SYS_IOUT_UC_WARN , SENSOR_ATTR_LTC4286_STATUS_MFR_SYS_PIN_UP_WARN , SENSOR_ATTR_LTC4286_STATUS_MFR_SYS_END }
```

相关声明：[ltc4286_status_mfr_sys_status_attr](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ga6eedfb02e2dca41346990a7e28d6fdb6)、[SENSOR_ATTR_LTC4286_STATUS_MFR_SYS_STAT1_ALERT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga6eedfb02e2dca41346990a7e28d6fdb6ab73c0f5cb152744ab7a65e1b774639b3)、[SENSOR_ATTR_LTC4286_STATUS_MFR_SYS_STAT1_L_ALERT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga6eedfb02e2dca41346990a7e28d6fdb6abeeb00d6b5fa5841e1a7cf098fe8896f)、[SENSOR_ATTR_LTC4286_STATUS_MFR_SYS_POWER_LOSS](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga6eedfb02e2dca41346990a7e28d6fdb6a2e6a49b9a80679ac3db0d16d2bbfc416)、[SENSOR_ATTR_LTC4286_STATUS_MFR_SYS_RESET_DONE](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga6eedfb02e2dca41346990a7e28d6fdb6a9cafb7301150d97d54f9db5de0c4a839)、[SENSOR_ATTR_LTC4286_STATUS_MFR_SYS_AVG_DONE](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga6eedfb02e2dca41346990a7e28d6fdb6a8bc8b2437114994ce23bc3fd222bd746)、[SENSOR_ATTR_LTC4286_STATUS_MFR_SYS_ADC_CONV](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga6eedfb02e2dca41346990a7e28d6fdb6afabb7590aa82d45509d18f8f65df8d8c)、[SENSOR_ATTR_LTC4286_STATUS_MFR_SYS_STAT2_SET](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga6eedfb02e2dca41346990a7e28d6fdb6a18c7eba895ed70aa0a9f4c6964810474)、[SENSOR_ATTR_LTC4286_STATUS_MFR_SYS_POWER_FAILED_WARN](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga6eedfb02e2dca41346990a7e28d6fdb6a692e04be3bac9ea7fcc936caede7260e)、[SENSOR_ATTR_LTC4286_STATUS_MFR_SYS_FET_SHORT_WARN](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga6eedfb02e2dca41346990a7e28d6fdb6a6aeea2c54ee697cce4c83071ab615a34)、[SENSOR_ATTR_LTC4286_STATUS_MFR_SYS_VDS_UV_WARN](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga6eedfb02e2dca41346990a7e28d6fdb6a5b5ffafd9bb3f1f132a3d88b3d0e647c)、[SENSOR_ATTR_LTC4286_STATUS_MFR_SYS_VDS_OV_WARN](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga6eedfb02e2dca41346990a7e28d6fdb6a89dc42832ef0c1385cf2e250d1a77778)、[SENSOR_ATTR_LTC4286_STATUS_MFR_SYS_IOUT_UC_WARN](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga6eedfb02e2dca41346990a7e28d6fdb6a1dff38241b681226edc7086b5ae63234)、[SENSOR_ATTR_LTC4286_STATUS_MFR_SYS_PIN_UP_WARN](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga6eedfb02e2dca41346990a7e28d6fdb6ab0fc47d97df92d27ca70c633553fe138)、[SENSOR_ATTR_LTC4286_STATUS_MFR_SYS_END](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga6eedfb02e2dca41346990a7e28d6fdb6a08c5b57565d26823d920a092f243ed99)。

LTC4286 厂商系统状态属性（Manufacturer System Status Attributes）。

<a id="r_ga2e6b4da32c15bdc32757b8d70150668c"></a>

```c
enum ltc4286_adc_attr { SENSOR_ATTR_LTC4286_ADC_VDS_SELECT = SENSOR_ATTR_LTC4286_STATUS_MFR_SYS_END , SENSOR_ATTR_LTC4286_ADC_VIN_VOUT_SELECT , SENSOR_ATTR_LTC4286_ADC_DISP_AVG , SENSOR_ATTR_LTC4286_ADC_AVG_SELECT , SENSOR_ATTR_LTC4286_ADC_END }
```

相关声明：[ltc4286_adc_attr](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ga2e6b4da32c15bdc32757b8d70150668c)、[SENSOR_ATTR_LTC4286_ADC_VDS_SELECT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga2e6b4da32c15bdc32757b8d70150668ca62ac8ece70184f5ebb8f42b473c696c1)、[SENSOR_ATTR_LTC4286_ADC_VIN_VOUT_SELECT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga2e6b4da32c15bdc32757b8d70150668caf118081440de092c0f3f75259fdb0436)、[SENSOR_ATTR_LTC4286_ADC_DISP_AVG](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga2e6b4da32c15bdc32757b8d70150668ca0604e8b290ccca2b6cd6344f9632ac33)、[SENSOR_ATTR_LTC4286_ADC_AVG_SELECT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga2e6b4da32c15bdc32757b8d70150668ca1f07f3793542fe27b6c4d5a3fbaf0a15)、[SENSOR_ATTR_LTC4286_ADC_END](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga2e6b4da32c15bdc32757b8d70150668cabd49d589e8aa52e97dc6cc4a5d1c4d34)。

LTC4286 ADC 配置属性（ADC Configuration Attributes）。

<a id="r_ga6f7112063223c4239d44da489935d77d"></a>

```c
enum ltc4286_fault_response_attr { SENSOR_ATTR_LTC4286_FAULT_RESPONSE , SENSOR_ATTR_LTC4286_FAULT_RETRY , SENSOR_ATTR_LTC4286_FAULT_OP_TIMER , SENSOR_ATTR_LTC4286_FAULT_OV_RESPONSE , SENSOR_ATTR_LTC4286_FAULT_OV_RETRY , SENSOR_ATTR_LTC4286_FAULT_UV_RESPONSE , SENSOR_ATTR_LTC4286_FAULT_UV_RETRY , SENSOR_ATTR_LTC4286_FAULT_END }
```

相关声明：[ltc4286_fault_response_attr](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ga6f7112063223c4239d44da489935d77d)、[SENSOR_ATTR_LTC4286_FAULT_RESPONSE](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga6f7112063223c4239d44da489935d77da6aa180a6d86a9db7391709f23d35e8ce)、[SENSOR_ATTR_LTC4286_FAULT_RETRY](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga6f7112063223c4239d44da489935d77da5e35f3e09e0c6ff8a8341ada128f75d7)、[SENSOR_ATTR_LTC4286_FAULT_OP_TIMER](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga6f7112063223c4239d44da489935d77da6377166c22b256b607718cdd2c8c074f)、[SENSOR_ATTR_LTC4286_FAULT_OV_RESPONSE](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga6f7112063223c4239d44da489935d77daacab96f7f4c1eb036912bc4daf1fc4c1)、[SENSOR_ATTR_LTC4286_FAULT_OV_RETRY](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga6f7112063223c4239d44da489935d77dac1ffcae5766160fca39ea49b97e09b86)、[SENSOR_ATTR_LTC4286_FAULT_UV_RESPONSE](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga6f7112063223c4239d44da489935d77daea8dd7b2943a49c093710949de7f4421)、[SENSOR_ATTR_LTC4286_FAULT_UV_RETRY](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga6f7112063223c4239d44da489935d77da4f26ecf0df081f65f6cf05bcb92cf2bc)、[SENSOR_ATTR_LTC4286_FAULT_END](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga6f7112063223c4239d44da489935d77dab727e59dc5722e57ab9648a6f197d9e1)。

LTC4286 故障响应配置属性（Fault Response Configuration Attributes）。

<a id="r_gaa0f79aba4e22cce5f3e870928f946ce2"></a>

```c
enum ltc4286_mfr_flt_attr { SENSOR_ATTR_LTC4286_MFR_FLT_OP_TO_FAULT = SENSOR_ATTR_LTC4286_FAULT_END , SENSOR_ATTR_LTC4286_MFR_FLT_OT_TO_FAULT , SENSOR_ATTR_LTC4286_MFR_FLT_END }
```

相关声明：[ltc4286_mfr_flt_attr](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gaa0f79aba4e22cce5f3e870928f946ce2)、[SENSOR_ATTR_LTC4286_MFR_FLT_OP_TO_FAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggaa0f79aba4e22cce5f3e870928f946ce2aafedaa8e82311ea8fe3b7788b652e41c)、[SENSOR_ATTR_LTC4286_MFR_FLT_OT_TO_FAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggaa0f79aba4e22cce5f3e870928f946ce2a1e78d93f08b9017c39641719ff520e34)、[SENSOR_ATTR_LTC4286_MFR_FLT_END](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggaa0f79aba4e22cce5f3e870928f946ce2ad6f4e9771760b64ba601375a8a5ceb92)。

LTC4286 厂商故障配置属性（Manufacturer Fault Configuration Attributes）。

<a id="r_ga1938c61b0c0bad9fa44ac235b2ee93ff"></a>

```c
enum ltc4286_reboot_control_attr { SENSOR_ATTR_LTC4286_REBOOT_CONTROL_INIT = SENSOR_ATTR_LTC4286_MFR_FLT_END , SENSOR_ATTR_LTC4286_REBOOT_CONTROL_DELAY , SENSOR_ATTR_LTC4286_REBOOT_CONTROL_END }
```

相关声明：[ltc4286_reboot_control_attr](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ga1938c61b0c0bad9fa44ac235b2ee93ff)、[SENSOR_ATTR_LTC4286_REBOOT_CONTROL_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga1938c61b0c0bad9fa44ac235b2ee93ffa97048b9a51696ba28f249a6a4c9ad60a)、[SENSOR_ATTR_LTC4286_REBOOT_CONTROL_DELAY](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga1938c61b0c0bad9fa44ac235b2ee93ffa319fcfb878b3c67f5f073b2af3278173)、[SENSOR_ATTR_LTC4286_REBOOT_CONTROL_END](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga1938c61b0c0bad9fa44ac235b2ee93ffada0c1ec9e66c0ba1eab0e9610b960630)。

LTC4286 重启控制属性（Reboot Control Attributes）。

<a id="r_gac88db1417989518cdd4527f7a2e01e54"></a>

```c
enum ltc4286_mfr_config_attr { SENSOR_ATTR_LTC4286_MFR_CONFIG_ILIM = SENSOR_ATTR_LTC4286_REBOOT_CONTROL_END , SENSOR_ATTR_LTC4286_MFR_CONFIG_VRANGE_SEL , SENSOR_ATTR_LTC4286_MFR_CONFIG_VPWR_SEL , SENSOR_ATTR_LTC4286_MFR_CONFIG_PMBUS_1MBIT , SENSOR_ATTR_LTC4286_MFR_CONFIG_RESET_FAULT , SENSOR_ATTR_LTC4286_MFR_CONFIG_PWR_GOOD_RESET_CTRL , SENSOR_ATTR_LTC4286_MFR_CONFIG_MASS_WRITE , SENSOR_ATTR_LTC4286_MFR_CONFIG_EXT_TEMP , SENSOR_ATTR_LTC4286_MFR_CONFIG_DEBOUNCE_TIMER , SENSOR_ATTR_LTC4286_MFR_CONFIG_END }
```

相关声明：[ltc4286_mfr_config_attr](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gac88db1417989518cdd4527f7a2e01e54)、[SENSOR_ATTR_LTC4286_MFR_CONFIG_ILIM](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggac88db1417989518cdd4527f7a2e01e54ab0400e18f292468bb14d8827ad7e0c4a)、[SENSOR_ATTR_LTC4286_MFR_CONFIG_VRANGE_SEL](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggac88db1417989518cdd4527f7a2e01e54a1f5384899ac3bd9fce80bd6ca22431e3)、[SENSOR_ATTR_LTC4286_MFR_CONFIG_VPWR_SEL](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggac88db1417989518cdd4527f7a2e01e54a634f681d2371a7bb0aec6385d62e05b3)、[SENSOR_ATTR_LTC4286_MFR_CONFIG_PMBUS_1MBIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggac88db1417989518cdd4527f7a2e01e54aeeca57673eb29fb4d3950cfe0a48046d)、[SENSOR_ATTR_LTC4286_MFR_CONFIG_RESET_FAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggac88db1417989518cdd4527f7a2e01e54a43438d34b38ce27720f536817ab01b2b)、[SENSOR_ATTR_LTC4286_MFR_CONFIG_PWR_GOOD_RESET_CTRL](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggac88db1417989518cdd4527f7a2e01e54a01439e02c9f2a80b905357f198801bfa)、[SENSOR_ATTR_LTC4286_MFR_CONFIG_MASS_WRITE](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggac88db1417989518cdd4527f7a2e01e54a28d344bb18e17b837a040fc318ec4e0b)、[SENSOR_ATTR_LTC4286_MFR_CONFIG_EXT_TEMP](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggac88db1417989518cdd4527f7a2e01e54a3455b31b53d1fb3b80d6a98644a61b62)、[SENSOR_ATTR_LTC4286_MFR_CONFIG_DEBOUNCE_TIMER](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggac88db1417989518cdd4527f7a2e01e54a535dbd8ba286272fad039a79a761717d)、[SENSOR_ATTR_LTC4286_MFR_CONFIG_END](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggac88db1417989518cdd4527f7a2e01e54a77a13cc382f69b773f73a44c0da379a1)。

LTC4286 厂商配置属性（Manufacturer Configuration Attributes）。

<a id="r_gab6640bb8fd3260795923268b6b1de7bb"></a>

```c
enum ltc4286_status_word_field { LTC4286_STATUS_WORD_VOUT_BIT = BIT(15) , LTC4286_STATUS_WORD_IOUT_BIT = BIT(14) , LTC4286_STATUS_WORD_INPUT_BIT = BIT(13) , LTC4286_STATUS_WORD_MFRSPEC_BIT = BIT(12) , LTC4286_STATUS_WORD_FET_UV_THRES_BIT = BIT(11) , LTC4286_STATUS_WORD_OTHER_BIT = BIT(9) , LTC4286_STATUS_WORD_UNKNOWN_BIT = BIT(8) , LTC4286_STATUS_WORD_BUSY_BIT = BIT(7) , LTC4286_STATUS_WORD_OFF_BIT = BIT(6) , LTC4286_STATUS_WORD_IOUT_OTHRES_BIT , LTC4286_STATUS_WORD_VIN_UTHRES_BIT , LTC4286_STATUS_WORD_TEMP_BIT = BIT(2) , LTC4286_STATUS_WORD_COMLINE_BIT = BIT(1) , LTC4286_STATUS_WORD_NOT_CLEAR_BIT = BIT(0) }
```

相关声明：[ltc4286_status_word_field](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gab6640bb8fd3260795923268b6b1de7bb)、[LTC4286_STATUS_WORD_VOUT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggab6640bb8fd3260795923268b6b1de7bba308f513149ab916045f7e94b3867fc41)、[LTC4286_STATUS_WORD_IOUT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggab6640bb8fd3260795923268b6b1de7bba0a2c685152c954bb0f61c1fb1069b720)、[LTC4286_STATUS_WORD_INPUT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggab6640bb8fd3260795923268b6b1de7bbac7be0bb5c253eb935858bddb29ab1a71)、[LTC4286_STATUS_WORD_MFRSPEC_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggab6640bb8fd3260795923268b6b1de7bba8fac5dd2a6443cfe2cfd9e269ef9500d)、[LTC4286_STATUS_WORD_FET_UV_THRES_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggab6640bb8fd3260795923268b6b1de7bba3f0d7c311cdb59fbc546c911468d2e8e)、[LTC4286_STATUS_WORD_OTHER_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggab6640bb8fd3260795923268b6b1de7bba248ae6611c20ffc6d552ea5c5c7e0905)、[LTC4286_STATUS_WORD_UNKNOWN_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggab6640bb8fd3260795923268b6b1de7bba1dc7baa15f33a50107c3f661893f7115)、[LTC4286_STATUS_WORD_BUSY_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggab6640bb8fd3260795923268b6b1de7bba09bc4e777d9f2f48c28e41f83ae8e85d)、[LTC4286_STATUS_WORD_OFF_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggab6640bb8fd3260795923268b6b1de7bba4dca0688357b23f13d99b6ee58c73b0a)、[LTC4286_STATUS_WORD_IOUT_OTHRES_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggab6640bb8fd3260795923268b6b1de7bbae13e246de568e56e465470cc1e5f9929)、[LTC4286_STATUS_WORD_VIN_UTHRES_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggab6640bb8fd3260795923268b6b1de7bbaf5a5b2e03f910879af5e1ef416533524)、[LTC4286_STATUS_WORD_TEMP_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggab6640bb8fd3260795923268b6b1de7bbacfc1f7b8ee11a46b2ce695d85aafd20c)、[LTC4286_STATUS_WORD_COMLINE_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggab6640bb8fd3260795923268b6b1de7bba2aa72e38e64ea6d8a994f8bfb8948ee2)、[LTC4286_STATUS_WORD_NOT_CLEAR_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggab6640bb8fd3260795923268b6b1de7bba70d7028f9858fe0ce549a17e8361554e)。

LTC4286 状态字位字段定义（Status Word Bit Field Definitions）。

<a id="r_gaa6eaf3246ef40abc22725abcd7ae6012"></a>

```c
enum ltc4286_status_vout_field { LTC4286_VOUT_UV_WARNING_BIT = BIT(5) , LTC4286_VOUT_OV_WARNING_BIT = BIT(6) }
```

相关声明：[ltc4286_status_vout_field](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gaa6eaf3246ef40abc22725abcd7ae6012)、[LTC4286_VOUT_UV_WARNING_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggaa6eaf3246ef40abc22725abcd7ae6012a0da84e9a87aaa77f3ce416103a49aad9)、[LTC4286_VOUT_OV_WARNING_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggaa6eaf3246ef40abc22725abcd7ae6012a567f2837c67e457952eca8c326229b3a)。

LTC4286 输出电压状态位字段定义（Output Voltage Status Bit Field Definitions）。

<a id="r_ga421f54d62139840db517225de8c89460"></a>

```c
enum ltc4286_status_iout_field { LTC4286_IOUT_OC_WARNING_BIT = BIT(5) , LTC4286_IOUT_OC_FAULT_BIT = BIT(7) }
```

相关声明：[ltc4286_status_iout_field](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ga421f54d62139840db517225de8c89460)、[LTC4286_IOUT_OC_WARNING_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga421f54d62139840db517225de8c89460adb351f06ccfd05f6ccc3c19ecdac43d1)、[LTC4286_IOUT_OC_FAULT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga421f54d62139840db517225de8c89460a304579c60e9942fd90750c8bbe2470a3)。

LTC4286 输出电流状态位字段定义（Output Current Status Bit Field Definitions）。

<a id="r_ga7c3cb25fe7c8dae8e12e9c861a1c0952"></a>

```c
enum ltc4286_status_input_field { LTC4286_PIN_OP_WARNING_BIT = BIT(0) , LTC4286_VIN_UV_FAULT_BIT = BIT(4) , LTC4286_VIN_UV_WARNING_BIT = BIT(5) , LTC4286_VIN_OV_WARNING_BIT = BIT(6) , LTC4286_VIN_OV_FAULT_BIT = BIT(7) }
```

相关声明：[ltc4286_status_input_field](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ga7c3cb25fe7c8dae8e12e9c861a1c0952)、[LTC4286_PIN_OP_WARNING_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga7c3cb25fe7c8dae8e12e9c861a1c0952afaa9ba1964d8a9e02771b118135d5b03)、[LTC4286_VIN_UV_FAULT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga7c3cb25fe7c8dae8e12e9c861a1c0952a390b9abe80531006bc156d092cc47027)、[LTC4286_VIN_UV_WARNING_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga7c3cb25fe7c8dae8e12e9c861a1c0952aab0f5a3a4ece540f7193890e17ced6f7)、[LTC4286_VIN_OV_WARNING_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga7c3cb25fe7c8dae8e12e9c861a1c0952a61be92e1a593adaa3cd29728fde1c58c)、[LTC4286_VIN_OV_FAULT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga7c3cb25fe7c8dae8e12e9c861a1c0952a0d328f79596af042369e610973cd0045)。

LTC4286 输入电压／功率状态位字段定义（Input Voltage/Power Status Bit Field Definitions）。

<a id="r_ga9fce26b6b719d1a030c870651cc6aec8"></a>

```c
enum ltc4286_status_temp_field { LTC4286_TEMP_UT_WARNING_BIT = BIT(5) , LTC4286_TEMP_OT_WARNING_BIT = BIT(6) , LTC4286_TEMP_OT_FAULT_BIT = BIT(7) }
```

相关声明：[ltc4286_status_temp_field](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ga9fce26b6b719d1a030c870651cc6aec8)、[LTC4286_TEMP_UT_WARNING_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga9fce26b6b719d1a030c870651cc6aec8adf9fe69263b87c66f16e8ea28599952c)、[LTC4286_TEMP_OT_WARNING_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga9fce26b6b719d1a030c870651cc6aec8a0456e4913bc4c1c35bbd81b9ae15f432)、[LTC4286_TEMP_OT_FAULT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga9fce26b6b719d1a030c870651cc6aec8a08ed840142dbf146ec17e2abd59c6722)。

LTC4286 温度状态位字段定义（Temperature Status Bit Field Definitions）。

<a id="r_gab268b8865c4a1fc30719d09a8ba9c6fb"></a>

```c
enum ltc4286_status_cml_field { LTC4286_MISC_FAULT_BIT = BIT(1) , LTC4286_PEC_FAILED_BIT = BIT(5) , LTC4286_BAD_DATA_BIT = BIT(6) , LTC4286_BAD_CMD_BIT = BIT(7) }
```

相关声明：[ltc4286_status_cml_field](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gab268b8865c4a1fc30719d09a8ba9c6fb)、[LTC4286_MISC_FAULT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggab268b8865c4a1fc30719d09a8ba9c6fba16b198e9902806940e9474bebcb8ed1a)、[LTC4286_PEC_FAILED_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggab268b8865c4a1fc30719d09a8ba9c6fba97e37a21dd64ddfb2168bd24dde47170)、[LTC4286_BAD_DATA_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggab268b8865c4a1fc30719d09a8ba9c6fba486a7f6f829372515183ef1cf44582d8)、[LTC4286_BAD_CMD_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggab268b8865c4a1fc30719d09a8ba9c6fba2c23efc3d80d525d02b57c56bc2bfa45)。

LTC4286 通信／命令状态位字段定义（Communication/Command Status Bit Field Definitions）。

<a id="r_ga5988afbf2abc6e5c5e313d81b683a625"></a>

```c
enum ltc4286_status_other_field { LTC4286_OTHER_FIRST_ALERT_BIT = BIT(0) }
```

相关声明：[ltc4286_status_other_field](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ga5988afbf2abc6e5c5e313d81b683a625)、[LTC4286_OTHER_FIRST_ALERT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga5988afbf2abc6e5c5e313d81b683a625acb755b4721a106941af3f61546c900b2)。

LTC4286 其他状态位字段定义（Other Status Bit Field Definitions）。

<a id="r_ga0d9d60ecc24cdf24642d8d45ee228bf1"></a>

```c
enum ltc4286_status_mfr_spec_field { LTC4286_MFR_SPEC_FET_BAD_FAULT_BIT = BIT(2) , LTC4286_MFR_SPEC_PIN_OP1_FAULT_BIT = BIT(3) , LTC4286_MFR_SPEC_PIN_OP2_FAULT_BIT = BIT(4) , LTC4286_MFR_SPEC_VDD_UVLO_BIT = BIT(5) , LTC4286_MFR_SPEC_TSD_FAULT_BIT = BIT(6) , LTC4286_MFR_SPEC_EN_CHANGED_BIT = BIT(7) }
```

相关声明：[ltc4286_status_mfr_spec_field](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ga0d9d60ecc24cdf24642d8d45ee228bf1)、[LTC4286_MFR_SPEC_FET_BAD_FAULT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga0d9d60ecc24cdf24642d8d45ee228bf1a7da6c9efea8b135115b3aea9f484e1e3)、[LTC4286_MFR_SPEC_PIN_OP1_FAULT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga0d9d60ecc24cdf24642d8d45ee228bf1a437bc24955298f29d2e92839a67f7235)、[LTC4286_MFR_SPEC_PIN_OP2_FAULT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga0d9d60ecc24cdf24642d8d45ee228bf1a43bff18b66e0d4f0f81740066538a47d)、[LTC4286_MFR_SPEC_VDD_UVLO_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga0d9d60ecc24cdf24642d8d45ee228bf1a3f9e3c2436203afdf12029d230d77f1b)、[LTC4286_MFR_SPEC_TSD_FAULT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga0d9d60ecc24cdf24642d8d45ee228bf1a8e56294d86cf87b4ad4bd49a4057f128)、[LTC4286_MFR_SPEC_EN_CHANGED_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga0d9d60ecc24cdf24642d8d45ee228bf1aaad799bcf0ddd7c809f110ebbc68898b)。

LTC4286 厂商专用状态位字段定义（Manufacturer-specific Status Bit Field Definitions）。

<a id="r_gae371b2b0685c34a368909636fd63a9d0"></a>

```c
enum ltc4286_mfr_sys_status1_field { LTC4286_MFR_SYS_STATUS1_ADC_CONV_BIT = BIT(6) , LTC4286_MFR_SYS_STATUS1_AVERAGE_DONE_BIT = BIT(7) , LTC4286_MFR_SYS_STATUS1_RESET_DONE_BIT = BIT(10) , LTC4286_MFR_SYS_STATUS1_POWER_LOSS_BIT = BIT(11) , LTC4286_MFR_SYS_STATUS1_L_ALERT_BIT = BIT(14) , LTC4286_MFR_SYS_STATUS1_ALERT_BIT = BIT(15) }
```

相关声明：[ltc4286_mfr_sys_status1_field](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gae371b2b0685c34a368909636fd63a9d0)、[LTC4286_MFR_SYS_STATUS1_ADC_CONV_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggae371b2b0685c34a368909636fd63a9d0a2941657ebb7951dd2b3f56ebeb593e8b)、[LTC4286_MFR_SYS_STATUS1_AVERAGE_DONE_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggae371b2b0685c34a368909636fd63a9d0a408d62e976b770b1662f7d433363f393)、[LTC4286_MFR_SYS_STATUS1_RESET_DONE_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggae371b2b0685c34a368909636fd63a9d0a33171b5d99b2e7a867593a99523f817c)、[LTC4286_MFR_SYS_STATUS1_POWER_LOSS_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggae371b2b0685c34a368909636fd63a9d0ab7a202d2b6d9081d4cbae6e46bd7f824)、[LTC4286_MFR_SYS_STATUS1_L_ALERT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggae371b2b0685c34a368909636fd63a9d0a6138631a9dbcaa9db1b5af1cabc9add6)、[LTC4286_MFR_SYS_STATUS1_ALERT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggae371b2b0685c34a368909636fd63a9d0a634ea0ebce11fb4998cec9d4f265c5a0)。

LTC4286 厂商系统状态 1 位字段定义（Manufacturer System Status 1 Bit Field Definitions）。

<a id="r_ga93a666fb5258e905627800edbf68c136"></a>

```c
enum ltc4286_mfr_sys_status2_field { LTC4286_MFR_SYS_STATUS2_PIN_UP_WARNING_BIT = BIT(0) , LTC4286_MFR_SYS_STATUS2_IOUT_UC_WARNING_BIT = BIT(1) , LTC4286_MFR_SYS_STATUS2_VDS_UV_WARNING_BIT = BIT(2) , LTC4286_MFR_SYS_STATUS2_VDS_OV_WARNING_BIT = BIT(3) , LTC4286_MFR_SYS_STATUS2_FET_SHORT_WARNING_BIT = BIT(14) , LTC4286_MFR_SYS_STATUS2_POWER_FAILED_WARNING_BIT = BIT(15) }
```

相关声明：[ltc4286_mfr_sys_status2_field](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ga93a666fb5258e905627800edbf68c136)、[LTC4286_MFR_SYS_STATUS2_PIN_UP_WARNING_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga93a666fb5258e905627800edbf68c136a4d5e23e4ae55658b779c3eba74c4dd88)、[LTC4286_MFR_SYS_STATUS2_IOUT_UC_WARNING_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga93a666fb5258e905627800edbf68c136a5b6f270f484a04bda891b83b082cbe94)、[LTC4286_MFR_SYS_STATUS2_VDS_UV_WARNING_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga93a666fb5258e905627800edbf68c136ae4a4f6ee801e8c3f5af6ecd3fd709ffd)、[LTC4286_MFR_SYS_STATUS2_VDS_OV_WARNING_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga93a666fb5258e905627800edbf68c136a39098a539e90cdb34bf0e43babef4a6c)、[LTC4286_MFR_SYS_STATUS2_FET_SHORT_WARNING_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga93a666fb5258e905627800edbf68c136ae3aa56ba7b44dd284fc4972fe16f3768)、[LTC4286_MFR_SYS_STATUS2_POWER_FAILED_WARNING_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga93a666fb5258e905627800edbf68c136aa4c62a23cc0de36d33ae8416718872c0)。

LTC4286 厂商系统状态 2 位字段定义（Manufacturer System Status 2 Bit Field Definitions）。

<a id="r_ga87bd44a44c010f3217753ef01692d197"></a>

```c
enum ltc4286_trig_alert_mask { LTC4286_ALERT_STATUS_WORD_MASK = 0xD0 , LTC4286_ALERT_STATUS_VOUT_MASK = 0xD2 , LTC4286_ALERT_STATUS_IOUT_MASK , LTC4286_ALERT_STATUS_INPUT_MASK , LTC4286_ALERT_STATUS_TEMP_MASK , LTC4286_ALERT_STATUS_COMMS_MASK , LTC4286_ALERT_STATUS_SPEC_MASK = 0xD8 , LTC4286_ALERT_STATUS_SYS1_MASK = 0xDA , LTC4286_ALERT_STATUS_SYS2_MASK = 0xDC }
```

相关声明：[ltc4286_trig_alert_mask](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ga87bd44a44c010f3217753ef01692d197)、[LTC4286_ALERT_STATUS_WORD_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga87bd44a44c010f3217753ef01692d197a686fe737e40fcbe8c7687ef28e5eef1c)、[LTC4286_ALERT_STATUS_VOUT_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga87bd44a44c010f3217753ef01692d197a1158bafacebec83c24fe803db9ddcbc4)、[LTC4286_ALERT_STATUS_IOUT_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga87bd44a44c010f3217753ef01692d197a29a3ef4fed472087dd98a638f02170dd)、[LTC4286_ALERT_STATUS_INPUT_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga87bd44a44c010f3217753ef01692d197a530596e6edf454c0c7b51f014ffedcbd)、[LTC4286_ALERT_STATUS_TEMP_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga87bd44a44c010f3217753ef01692d197af6ecd677a77d5d346a473e7d406563af)、[LTC4286_ALERT_STATUS_COMMS_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga87bd44a44c010f3217753ef01692d197aeb6ecdbfc7a5a28ce0f8a088ef266229)、[LTC4286_ALERT_STATUS_SPEC_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga87bd44a44c010f3217753ef01692d197a5539b96ff27b9cf3d23556942d885890)、[LTC4286_ALERT_STATUS_SYS1_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga87bd44a44c010f3217753ef01692d197a3568c1477227384dd7cb1706d514c16c)、[LTC4286_ALERT_STATUS_SYS2_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga87bd44a44c010f3217753ef01692d197a2eaf109ed2286e4eea758524edc0e670)。

用于触发警报的警报掩码类型（Alert Mask Types）。

<a id="r_gac9d479a89a01f734c22ee50d6d4da320"></a>

```c
enum ltc4286_status_alert { LTC4286_ALERT_STATUS_BUSY_ALERT_BIT = BIT(7) }
```

相关声明：[ltc4286_status_alert](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gac9d479a89a01f734c22ee50d6d4da320)、[LTC4286_ALERT_STATUS_BUSY_ALERT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggac9d479a89a01f734c22ee50d6d4da320af8a362cbf236a827c6e7a002f0baf9f5)。

LTC4286 状态字警报位字段定义（Status Word Alert Bit Field Definitions）。

<a id="r_gaf8e9b09707496eeeb74f75928939d7b2"></a>

```c
enum ltc4286_vout_alert { LTC4286_ALERT_VOUT_UV_WARNING_ALERT_BIT = BIT(5) , LTC4286_ALERT_VOUT_OV_WARNING_ALERT_BIT = BIT(6) }
```

相关声明：[ltc4286_vout_alert](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gaf8e9b09707496eeeb74f75928939d7b2)、[LTC4286_ALERT_VOUT_UV_WARNING_ALERT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggaf8e9b09707496eeeb74f75928939d7b2a4649ef806ce413a712939ae2c0376f48)、[LTC4286_ALERT_VOUT_OV_WARNING_ALERT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggaf8e9b09707496eeeb74f75928939d7b2ac001fac5a12e81b747412386bf4cf1bf)。

LTC4286 输出电压警报位字段定义（Output Voltage Alert Bit Field Definitions）。

<a id="r_gad67f6528db32f57693c40d3dd703b681"></a>

```c
enum ltc4286_iout_alert { LTC4286_ALERT_IOUT_OC_WARNING_ALERT_BIT = BIT(5) , LTC4286_ALERT_IOUT_OC_FAULT_ALERT_BIT = BIT(7) }
```

相关声明：[ltc4286_iout_alert](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gad67f6528db32f57693c40d3dd703b681)、[LTC4286_ALERT_IOUT_OC_WARNING_ALERT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggad67f6528db32f57693c40d3dd703b681adcd36ec46ef007cd1eecb40b6ced7ec0)、[LTC4286_ALERT_IOUT_OC_FAULT_ALERT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggad67f6528db32f57693c40d3dd703b681aefcd18ed435f05b1d2b322a93f148791)。

LTC4286 输出电流警报位字段定义（Output Current Alert Bit Field Definitions）。

<a id="r_ga7526494801158c04caf40d182f6dce15"></a>

```c
enum ltc4286_input_alert { LTC4286_ALERT_PIN_OP_WARNING_ALERT_BIT = BIT(0) , LTC4286_ALERT_VIN_UV_FAULT_ALERT_BIT = BIT(4) , LTC4286_ALERT_VIN_UV_WARNING_ALERT_BIT = BIT(5) , LTC4286_ALERT_VIN_OV_WARNING_ALERT_BIT = BIT(6) , LTC4286_ALERT_VIN_OV_FAULT_ALERT_BIT = BIT(7) }
```

相关声明：[ltc4286_input_alert](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ga7526494801158c04caf40d182f6dce15)、[LTC4286_ALERT_PIN_OP_WARNING_ALERT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga7526494801158c04caf40d182f6dce15ad0c111fde33a734c79c1435a685e6892)、[LTC4286_ALERT_VIN_UV_FAULT_ALERT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga7526494801158c04caf40d182f6dce15a3831c49adc47592651a8a69b7d5917fe)、[LTC4286_ALERT_VIN_UV_WARNING_ALERT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga7526494801158c04caf40d182f6dce15afd4aa1521a27bbfdb6d35eda2091bc67)、[LTC4286_ALERT_VIN_OV_WARNING_ALERT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga7526494801158c04caf40d182f6dce15a5f8b52779738dc7927b4610b7ecc41e6)、[LTC4286_ALERT_VIN_OV_FAULT_ALERT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga7526494801158c04caf40d182f6dce15a3c9f198af6d725e871d8d5ee803af23c)。

LTC4286 输入电压／功率警报位字段定义（Input Voltage/Power Alert Bit Field Definitions）。

<a id="r_gabbe9371859d1a073a7d496e18c7e7fbf"></a>

```c
enum ltc4286_temp_alert { LTC4286_ALERT_TEMP_UT_WARNING_ALERT_BIT = BIT(5) , LTC4286_ALERT_TEMP_OT_WARNING_ALERT_BIT = BIT(6) , LTC4286_ALERT_TEMP_OT_FAULT_ALERT_BIT = BIT(7) }
```

相关声明：[ltc4286_temp_alert](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gabbe9371859d1a073a7d496e18c7e7fbf)、[LTC4286_ALERT_TEMP_UT_WARNING_ALERT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggabbe9371859d1a073a7d496e18c7e7fbfa286c47cdfd02d3d95003fbd9768a76fc)、[LTC4286_ALERT_TEMP_OT_WARNING_ALERT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggabbe9371859d1a073a7d496e18c7e7fbfabc3617a0ee54faba1a42168cf35a2ead)、[LTC4286_ALERT_TEMP_OT_FAULT_ALERT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggabbe9371859d1a073a7d496e18c7e7fbfa98b656ecf055b656e6d43bfbb3e1d430)。

LTC4286 温度警报位字段定义（Temperature Alert Bit Field Definitions）。

<a id="r_ga57e786e009c96bb70e3219f237a15c06"></a>

```c
enum ltc4286_cml_alert { LTC4286_ALERT_MISC_FAULT_ALERT_BIT = BIT(1) , LTC4286_ALERT_PEC_FAILED_ALERT_BIT = BIT(5) , LTC4286_ALERT_BAD_DATA_ALERT_BIT = BIT(6) , LTC4286_ALERT_BAD_CMD_ALERT_BIT = BIT(7) }
```

相关声明：[ltc4286_cml_alert](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ga57e786e009c96bb70e3219f237a15c06)、[LTC4286_ALERT_MISC_FAULT_ALERT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga57e786e009c96bb70e3219f237a15c06a278dff3fdd95b48545fa5115260ffaaf)、[LTC4286_ALERT_PEC_FAILED_ALERT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga57e786e009c96bb70e3219f237a15c06a4d08f5aec4bdafc87c7cffb7c0c7eedd)、[LTC4286_ALERT_BAD_DATA_ALERT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga57e786e009c96bb70e3219f237a15c06a3214d38cb44d5941c0f12f1f6c918926)、[LTC4286_ALERT_BAD_CMD_ALERT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga57e786e009c96bb70e3219f237a15c06a31560620795f69bc7413c40c966895e6)。

LTC4286 通信／命令警报位字段定义（Communication/Command Alert Bit Field Definitions）。

<a id="r_gaed0a6e6bfd48646648ca0be09c159cf9"></a>

```c
enum ltc4286_mfr_spec_alert { LTC4286_ALERT_MFR_SPEC_FET_BAD_FAULT_ALERT_BIT = BIT(2) , LTC4286_ALERT_MFR_SPEC_PIN_OP1_FAULT_ALERT_BIT = BIT(3) , LTC4286_ALERT_MFR_SPEC_PIN_OP2_FAULT_ALERT_BIT = BIT(4) , LTC4286_ALERT_MFR_SPEC_VDD_UVLO_ALERT_BIT = BIT(5) , LTC4286_ALERT_MFR_SPEC_TSD_FAULT_ALERT_BIT = BIT(6) , LTC4286_ALERT_MFR_SPEC_EN_CHANGED_ALERT_BIT = BIT(7) }
```

相关声明：[ltc4286_mfr_spec_alert](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gaed0a6e6bfd48646648ca0be09c159cf9)、[LTC4286_ALERT_MFR_SPEC_FET_BAD_FAULT_ALERT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggaed0a6e6bfd48646648ca0be09c159cf9a87f4fa895950d9372a0360f51eed2014)、[LTC4286_ALERT_MFR_SPEC_PIN_OP1_FAULT_ALERT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggaed0a6e6bfd48646648ca0be09c159cf9afa7a71ed3e9070edb29337defe59864d)、[LTC4286_ALERT_MFR_SPEC_PIN_OP2_FAULT_ALERT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggaed0a6e6bfd48646648ca0be09c159cf9a2fbb3b72a62a00dae31ac7182453c0df)、[LTC4286_ALERT_MFR_SPEC_VDD_UVLO_ALERT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggaed0a6e6bfd48646648ca0be09c159cf9a3db277ece640f40cd94335270121571e)、[LTC4286_ALERT_MFR_SPEC_TSD_FAULT_ALERT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggaed0a6e6bfd48646648ca0be09c159cf9a68841a5e5e02a6c86b1b843f34622fff)、[LTC4286_ALERT_MFR_SPEC_EN_CHANGED_ALERT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggaed0a6e6bfd48646648ca0be09c159cf9a341b004b65a366e1427fbcc2d97a5aea)。

LTC4286 厂商专用警报位字段定义（Manufacturer-specific Alert Bit Field Definitions）。

<a id="r_ga020ba354df79f5f303f1dec20921f437"></a>

```c
enum ltc4286_mfr_sys_status1_alert { LTC4286_ALERT_MFR_SYS_STATUS1_ADC_CONV_ALERT_BIT = BIT(6) , LTC4286_ALERT_MFR_SYS_STATUS1_AVERAGE_DONE_ALERT_BIT = BIT(7) , LTC4286_ALERT_MFR_SYS_STATUS1_RESET_DONE_ALERT_BIT = BIT(10) , LTC4286_ALERT_MFR_SYS_STATUS1_POWER_LOSS_ALERT_BIT = BIT(11) }
```

相关声明：[ltc4286_mfr_sys_status1_alert](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ga020ba354df79f5f303f1dec20921f437)、[LTC4286_ALERT_MFR_SYS_STATUS1_ADC_CONV_ALERT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga020ba354df79f5f303f1dec20921f437a71d5c851425aecf276735d683232cf73)、[LTC4286_ALERT_MFR_SYS_STATUS1_AVERAGE_DONE_ALERT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga020ba354df79f5f303f1dec20921f437a4849e58229af61943d3f2ebe3e5b571f)、[LTC4286_ALERT_MFR_SYS_STATUS1_RESET_DONE_ALERT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga020ba354df79f5f303f1dec20921f437ab52efeeb323fbf5e1a6cd463604c8ff0)、[LTC4286_ALERT_MFR_SYS_STATUS1_POWER_LOSS_ALERT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga020ba354df79f5f303f1dec20921f437a2bfd7d61084376bc321a98e4b6a3caa6)。

LTC4286 厂商系统状态 1 警报位字段定义（Manufacturer System Status 1 Alert Bit Field Definitions）。

<a id="r_ga03dbaeaf95da8e9301af652a85aa6c3b"></a>

```c
enum ltc4286_mfr_sys_status2_alert { LTC4286_ALERT_MFR_SYS_STATUS2_PIN_UP_WARNING_ALERT_BIT = BIT(0) , LTC4286_ALERT_MFR_SYS_STATUS2_IOUT_UC_WARNING_ALERT_BIT = BIT(1) , LTC4286_ALERT_MFR_SYS_STATUS2_VDS_UV_WARNING_ALERT_BIT = BIT(2) , LTC4286_ALERT_MFR_SYS_STATUS2_VDS_OV_WARNING_ALERT_BIT = BIT(3) , LTC4286_ALERT_MFR_SYS_STATUS2_FET_SHORT_WARNING_ALERT_BIT = BIT(14) , LTC4286_ALERT_MFR_SYS_STATUS2_POWER_FAILED_WARNING_ALERT_BIT = BIT(15) }
```

相关声明：[ltc4286_mfr_sys_status2_alert](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ga03dbaeaf95da8e9301af652a85aa6c3b)、[LTC4286_ALERT_MFR_SYS_STATUS2_PIN_UP_WARNING_ALERT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga03dbaeaf95da8e9301af652a85aa6c3ba778d69f3db4f343a9d39dd5e13dc9188)、[LTC4286_ALERT_MFR_SYS_STATUS2_IOUT_UC_WARNING_ALERT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga03dbaeaf95da8e9301af652a85aa6c3baf7a755ef4af37d545306054ef79754a0)、[LTC4286_ALERT_MFR_SYS_STATUS2_VDS_UV_WARNING_ALERT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga03dbaeaf95da8e9301af652a85aa6c3ba98b17102db6f41df3f864ed1e33a5a02)、[LTC4286_ALERT_MFR_SYS_STATUS2_VDS_OV_WARNING_ALERT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga03dbaeaf95da8e9301af652a85aa6c3ba1c7aaf3825fde01d85e013c78cb76314)、[LTC4286_ALERT_MFR_SYS_STATUS2_FET_SHORT_WARNING_ALERT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga03dbaeaf95da8e9301af652a85aa6c3ba963de7dee7857255e50d6835354808b2)、[LTC4286_ALERT_MFR_SYS_STATUS2_POWER_FAILED_WARNING_ALERT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga03dbaeaf95da8e9301af652a85aa6c3ba369bb3c1589e7c272def1c3c0caccc69)。

LTC4286 厂商系统状态 2 警报位字段定义（Manufacturer System Status 2 Alert Bit Field Definitions）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 8.2\_函数（Functions）

<a id="r_gafe5f106d027ee4660006d104dba5c162"></a>

```c
int ltc4286_enable_alert_mask (const struct device *dev, enum ltc4286_trig_alert_mask alert_reg, uint16_t alert_bit)
```

相关声明：[ltc4286_enable_alert_mask](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gafe5f106d027ee4660006d104dba5c162)、[device](../device_reference/P002_设备对象结构.md)、[ltc4286_trig_alert_mask](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ga87bd44a44c010f3217753ef01692d197)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

启用 LTC4286 警报掩码（Alert Mask）。

<a id="r_gafc1ccc72d2b1792f4b4144e4e0633cb5"></a>

```c
int ltc4286_disable_alert_mask (const struct device *dev, enum ltc4286_trig_alert_mask alert_reg, uint16_t alert_bit)
```

相关声明：[ltc4286_disable_alert_mask](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gafc1ccc72d2b1792f4b4144e4e0633cb5)、[device](../device_reference/P002_设备对象结构.md)、[ltc4286_trig_alert_mask](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ga87bd44a44c010f3217753ef01692d197)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

禁用 LTC4286 警报掩码（Alert Mask）。


## 8.3\_原页交叉引用（Cross References）

- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [zephyr/drivers/sensor.h](../api_source_transport_clock_reference/P024_sensor.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P466_ltc4286.h_源码浏览.md)
- [ltc4286_sensor_chan](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gacfbf1c312a894cb8a9d796c910bf296e)
- [SENSOR_CHAN_LTC4286_VIN](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggacfbf1c312a894cb8a9d796c910bf296ea9611723fa128ef9b1d50ffc855e73555)
- [SENSOR_CHAN_LTC4286_ADC](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggacfbf1c312a894cb8a9d796c910bf296ea7c56dcb401d4a1d31ed8ad48cca34e18)
- [SENSOR_CHAN_LTC4286_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggacfbf1c312a894cb8a9d796c910bf296eae4375736913710f0bf8520045dd43dbd)
- [SENSOR_CHAN_LTC4286_END](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggacfbf1c312a894cb8a9d796c910bf296eaf00f43f28f525bdd5720ddda9fd93b01)
- [ltc4286_trig_chan](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ga39fb4460d62a29a7171a6fee309f7e82)
- [SENSOR_CHAN_LTC4286_TRIG_POWER_GOOD](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga39fb4460d62a29a7171a6fee309f7e82ab763321fa67df532ef7bc6071522f4a5)
- [SENSOR_CHAN_LTC4286_TRIG_COMPARATOR](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga39fb4460d62a29a7171a6fee309f7e82a5148bf77a9771e4f9de694eacbb2b52e)
- [SENSOR_CHAN_LTC4286_TRIG_ALERT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga39fb4460d62a29a7171a6fee309f7e82a63f553a0bd36f2c92b24dc565768f10d)
- [SENSOR_CHAN_LTC4286_TRIG_END](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga39fb4460d62a29a7171a6fee309f7e82a2a60329f625a951282498f0602b39429)
- [ltc4286_status_chan](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gaba2a3212fcfafcf12bf40fa6ac9a441f)
- [SENSOR_CHAN_LTC4286_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggaba2a3212fcfafcf12bf40fa6ac9a441fabff42a316554a78cce7c19d2767f6e68)
- [SENSOR_CHAN_LTC4286_STATUS_VOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggaba2a3212fcfafcf12bf40fa6ac9a441fa8b9de62a5fd40e1bf76431dee84da14e)
- [SENSOR_CHAN_LTC4286_STATUS_IOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggaba2a3212fcfafcf12bf40fa6ac9a441fa7ea188de23481a157d184eb361750b73)
- [SENSOR_CHAN_LTC4286_STATUS_INPUT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggaba2a3212fcfafcf12bf40fa6ac9a441faa44da14585661383c7a0ec752db7ff18)
- [SENSOR_CHAN_LTC4286_STATUS_TEMP](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggaba2a3212fcfafcf12bf40fa6ac9a441fa4d7b333ae63f31bb0b7f694cc098fe3d)
- [SENSOR_CHAN_LTC4286_STATUS_CML](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggaba2a3212fcfafcf12bf40fa6ac9a441fa62e4dc6f4798d810167fd57006734090)
- [SENSOR_CHAN_LTC4286_STATUS_OTHER](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggaba2a3212fcfafcf12bf40fa6ac9a441fa8587e0c8fe248edf784cba06c0f03148)
- [SENSOR_CHAN_LTC4286_STATUS_MFR_SPEC](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggaba2a3212fcfafcf12bf40fa6ac9a441fa2e28f2362b8970258ada962fa3ace3a8)
- [SENSOR_CHAN_LTC4286_STATUS_MFR_SYS_STATUS1](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggaba2a3212fcfafcf12bf40fa6ac9a441fa4e0e1dd867882f71f9e2150c13c65248)
- [SENSOR_CHAN_LTC4286_STATUS_MFR_SYS_STATUS2](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggaba2a3212fcfafcf12bf40fa6ac9a441fae98f32b16cd9e4e054c3926e09002fa0)
- [SENSOR_CHAN_LTC4286_STATUS_END](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggaba2a3212fcfafcf12bf40fa6ac9a441fadd16c3074a8460252ebbc6529be8579b)
- [ltc4286_mfr_chan](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ga3664558c0fae3685405ef754201c05c5)
- [SENSOR_CHAN_LTC4286_MFR_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga3664558c0fae3685405ef754201c05c5a48ae0d2df8804a920d8d439201be3f76)
- [SENSOR_CHAN_LTC4286_MFR_FLT_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga3664558c0fae3685405ef754201c05c5ae22b5b4f105253f11350f32cf142496d)
- [SENSOR_CHAN_LTC4286_MFR_PMB_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga3664558c0fae3685405ef754201c05c5a89ba0ad4cfac235d9eabbc8b617108cc)
- [SENSOR_CHAN_LTC4286_MFR_PADS_LIVE_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga3664558c0fae3685405ef754201c05c5a785ac7ea8b666842f514f2e923e7da85)
- [SENSOR_CHAN_LTC4286_MFR_COMMON](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga3664558c0fae3685405ef754201c05c5a50253d61a47c5d174bb991e4458c9ad8)
- [SENSOR_CHAN_LTC4286_MFR_REBOOT_CONTROL](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga3664558c0fae3685405ef754201c05c5a4d6045f94cebbcc5862f535bd950cedc)
- [SENSOR_CHAN_LTC4286_MFR_SHUTDOWN_CAUSE](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga3664558c0fae3685405ef754201c05c5a14f3038f12d9e11212b2aa3f4f28ad66)
- [SENSOR_CHAN_LTC4286_MFR_END](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga3664558c0fae3685405ef754201c05c5a33c7b2566d02ba6cdbd4eaedddf16484)
- [ltc4286_fault_response_chan](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ga9f50fb92d66bf9766aaa08e8937c53d8)
- [SENSOR_CHAN_LTC4286_FAULT_RESP_FET](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga9f50fb92d66bf9766aaa08e8937c53d8abd349590c733d2bc0ea4df82c07ee97a)
- [SENSOR_CHAN_LTC4286_FAULT_RESP_END](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga9f50fb92d66bf9766aaa08e8937c53d8aa984ae896e5fd0de445ba821ef953975)
- [ltc4286_config_attr](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ga648a72bf8571828c76f2502890b5792c)
- [SENSOR_ATTR_LTC4286_CONFIG_OPERATION](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga648a72bf8571828c76f2502890b5792cac1f645ee0e5d57e2e69f0014d861b2de)
- [SENSOR_ATTR_LTC4286_CONFIG_CLEAR_FAULTS](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga648a72bf8571828c76f2502890b5792ca521e057ea28c7b8a341bdc1b915c799e)
- [SENSOR_ATTR_LTC4286_CONFIG_WRITE_PROTECT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga648a72bf8571828c76f2502890b5792ca3509b911f31ce00998f015d7964a515d)
- [SENSOR_ATTR_LTC4286_CONFIG_END](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga648a72bf8571828c76f2502890b5792ca0f07ea708da2f26ec732832b5500039d)
- [ltc4286_status_attr](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gab354bb88b1c78717d85702a73541af1d)
- [SENSOR_ATTR_LTC4286_STATUS_VOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggab354bb88b1c78717d85702a73541af1da6af831ea19e18e6659d1da7c67151f47)
- [SENSOR_ATTR_LTC4286_STATUS_IOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggab354bb88b1c78717d85702a73541af1daf17e252d1124aa6c02dbdd5567128bc9)
- [SENSOR_ATTR_LTC4286_STATUS_INPUT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggab354bb88b1c78717d85702a73541af1da0b131dae831a6b147b4ccca8aa816666)
- [SENSOR_ATTR_LTC4286_STATUS_MFRSPEC](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggab354bb88b1c78717d85702a73541af1da3570149b2d45c32d4dc184de37776ff7)
- [SENSOR_ATTR_LTC4286_STATUS_PG](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggab354bb88b1c78717d85702a73541af1da0db72574d917f22385d9b8ff2d1cc3fb)
- [SENSOR_ATTR_LTC4286_STATUS_OTHER](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggab354bb88b1c78717d85702a73541af1dab37db70c1caadb4b556348ad99df1865)
- [SENSOR_ATTR_LTC4286_STATUS_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggab354bb88b1c78717d85702a73541af1da5c39e27197da8cb25262de092402eba8)
- [SENSOR_ATTR_LTC4286_STATUS_BUSY](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggab354bb88b1c78717d85702a73541af1da97878e0008bd7a1f56f6915e26b995c6)
- [SENSOR_ATTR_LTC4286_STATUS_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggab354bb88b1c78717d85702a73541af1da9d5df56313e243060854649f7c41ff17)
- [SENSOR_ATTR_LTC4286_STATUS_IOUT_OC](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggab354bb88b1c78717d85702a73541af1da7a07f03ba0244311f05571351c2ec76f)
- [SENSOR_ATTR_LTC4286_STATUS_VIN_UV](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggab354bb88b1c78717d85702a73541af1daea9511cef4322ba6fc60004359373555)
- [SENSOR_ATTR_LTC4286_STATUS_TEMP](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggab354bb88b1c78717d85702a73541af1da16924f500d4d18dcee894a2903983c6a)
- [SENSOR_ATTR_LTC4286_STATUS_CML](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggab354bb88b1c78717d85702a73541af1dae14003b2fb9a321614aad48adfdbdd26)
- [SENSOR_ATTR_LTC4286_STATUS_NOT_CLEAR](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggab354bb88b1c78717d85702a73541af1da427c27fba79e310f030c3568717e95ec)
- [SENSOR_ATTR_LTC4286_STATUS_END](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggab354bb88b1c78717d85702a73541af1da083f748a6a433c49b00744983376dc23)
- [ltc4286_status_vout_attr](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ga6a529f1c24665a30a5ef81bcc7afce00)
- [SENSOR_ATTR_LTC4286_STATUS_VOUT_OV](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga6a529f1c24665a30a5ef81bcc7afce00a8e181ac73a9c23cbd9d88f0c442f11b9)
- [SENSOR_ATTR_LTC4286_STATUS_VOUT_UV](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga6a529f1c24665a30a5ef81bcc7afce00a31d1451ea1c64e80e1253e3ec044a621)
- [SENSOR_ATTR_LTC4286_STATUS_VOUT_END](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga6a529f1c24665a30a5ef81bcc7afce00a0d6e73324e4af4f8f4091c0bcb543d85)
- [ltc4286_status_iout_attr](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ga842e114c954b3a9cf827c822dafb1604)
- [SENSOR_ATTR_LTC4286_STATUS_IOUT_OC_FAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga842e114c954b3a9cf827c822dafb1604abfd7a92938c1b8343a6fcc759fa4c011)
- [SENSOR_ATTR_LTC4286_STATUS_IOUT_OC_WARN](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga842e114c954b3a9cf827c822dafb1604aa84944f5ac9074488d4b2550d2e9ae5b)
- [SENSOR_ATTR_LTC4286_STATUS_IOUT_END](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga842e114c954b3a9cf827c822dafb1604ace0e6881a6771cc414dfddceb8331d5d)
- [ltc4286_status_input_attr](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gac8e200c73c25bfbb1749eaa0f9e99eaf)
- [SENSOR_ATTR_LTC4286_STATUS_VIN_OV_FAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggac8e200c73c25bfbb1749eaa0f9e99eafa5ae7bd1dafe774396844c2b8b4230bab)
- [SENSOR_ATTR_LTC4286_STATUS_VIN_OV_WARN](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggac8e200c73c25bfbb1749eaa0f9e99eafa756a7624990568f6730fea52f9eccb34)
- [SENSOR_ATTR_LTC4286_STATUS_VIN_UV_FAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggac8e200c73c25bfbb1749eaa0f9e99eafa1df817f7f3851c387b1f115e28cb58d1)
- [SENSOR_ATTR_LTC4286_STATUS_VIN_UV_WARN](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggac8e200c73c25bfbb1749eaa0f9e99eafaa1d93e8f91e6cf92999577612cad28b8)
- [SENSOR_ATTR_LTC4286_STATUS_PIN_OP_WARN](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggac8e200c73c25bfbb1749eaa0f9e99eafa90502ea2a99ec5801101701faad57d93)
- [SENSOR_ATTR_LTC4286_STATUS_INPUT_END](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggac8e200c73c25bfbb1749eaa0f9e99eafaef961684248efc937f0e4ae252085921)
- [ltc4286_status_temp_attr](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ga0c5c7496b1504cc0e87b6dd43363d672)
- [SENSOR_ATTR_LTC4286_STATUS_TEMP_OT_FAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga0c5c7496b1504cc0e87b6dd43363d672af2bb9cf3df964985d24456d81b2d4726)
- [SENSOR_ATTR_LTC4286_STATUS_TEMP_OT_WARN](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga0c5c7496b1504cc0e87b6dd43363d672a42e9a9956e22fbbd0b8d71314d93ee10)
- [SENSOR_ATTR_LTC4286_STATUS_TEMP_UT_WARN](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga0c5c7496b1504cc0e87b6dd43363d672a24fb6b3901d05bb4e7c34616889855cc)
- [SENSOR_ATTR_LTC4286_STATUS_TEMP_END](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga0c5c7496b1504cc0e87b6dd43363d672a870a0fb2537908f0654e00a87cf30cde)
- [ltc4286_status_cml_attr](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ga4fd75f925b184e14d2451dfc4c480bf3)
- [SENSOR_ATTR_LTC4286_STATUS_CML_BAD_CMD](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga4fd75f925b184e14d2451dfc4c480bf3a4b9df926c3a00ff0d5468a4eb8b0e663)
- [SENSOR_ATTR_LTC4286_STATUS_CML_BAD_DATA](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga4fd75f925b184e14d2451dfc4c480bf3a27743758a50b029c327a8cf08e5bcc06)
- [SENSOR_ATTR_LTC4286_STATUS_CML_BAD_PEC_FAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga4fd75f925b184e14d2451dfc4c480bf3ae86c062286e1b40d827484a33e0425a5)
- [SENSOR_ATTR_LTC4286_STATUS_CML_MISC_FAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga4fd75f925b184e14d2451dfc4c480bf3aa95ce2242074826d6a0c9feb89adef49)
- [SENSOR_ATTR_LTC4286_STATUS_CML_END](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga4fd75f925b184e14d2451dfc4c480bf3aea30aecd662487674a9c2e801b597ecd)
- [ltc4286_status_mfr_spec_attr](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ga1f8bec0c84f5ffdc2b0ab6e049987df8)
- [SENSOR_ATTR_LTC4286_STATUS_MFR_SPEC_EN_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga1f8bec0c84f5ffdc2b0ab6e049987df8aa37f746bf6a18fdb33f8968c160be9bf)
- [SENSOR_ATTR_LTC4286_STATUS_MFR_SPEC_TSD_FAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga1f8bec0c84f5ffdc2b0ab6e049987df8a2e5299de14b2ea6c65f519c32ec0e46c)
- [SENSOR_ATTR_LTC4286_STATUS_MFR_SPEC_VDD_UVLO](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga1f8bec0c84f5ffdc2b0ab6e049987df8abd5691720d953779171f049ff4113c6f)
- [SENSOR_ATTR_LTC4286_STATUS_MFR_SPEC_PIN_OP2_FAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga1f8bec0c84f5ffdc2b0ab6e049987df8ae12ba54d704e2575923650969194dc2e)
- [SENSOR_ATTR_LTC4286_STATUS_MFR_SPEC_PIN_OP1_FAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga1f8bec0c84f5ffdc2b0ab6e049987df8a1a4e883e855c4c524dcd1c2fc0a26072)
- [SENSOR_ATTR_LTC4286_STATUS_MFR_SPEC_FET_BAD_FAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga1f8bec0c84f5ffdc2b0ab6e049987df8a19ca2f34e4452c983823a725cffde402)
- [SENSOR_ATTR_LTC4286_STATUS_MFR_SPEC_END](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga1f8bec0c84f5ffdc2b0ab6e049987df8ab8a25e6a1ef623417920b50971de1d34)
- [ltc4286_status_other_attr](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ga85039255a2611470ce1a2293f8a0f9b1)
- [SENSOR_ATTR_LTC4286_STATUS_OTHER_FIRST_ALERT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga85039255a2611470ce1a2293f8a0f9b1a825d75e525060c2fb7ffbe51bfa67db5)
- [SENSOR_ATTR_LTC4286_STATUS_OTHER_END](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga85039255a2611470ce1a2293f8a0f9b1a17c5101095c645f91dd465eb4c5aacfa)
- [ltc4286_status_mfr_sys_status_attr](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ga6eedfb02e2dca41346990a7e28d6fdb6)
- [SENSOR_ATTR_LTC4286_STATUS_MFR_SYS_STAT1_ALERT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga6eedfb02e2dca41346990a7e28d6fdb6ab73c0f5cb152744ab7a65e1b774639b3)
- [SENSOR_ATTR_LTC4286_STATUS_MFR_SYS_STAT1_L_ALERT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga6eedfb02e2dca41346990a7e28d6fdb6abeeb00d6b5fa5841e1a7cf098fe8896f)
- [SENSOR_ATTR_LTC4286_STATUS_MFR_SYS_POWER_LOSS](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga6eedfb02e2dca41346990a7e28d6fdb6a2e6a49b9a80679ac3db0d16d2bbfc416)
- [SENSOR_ATTR_LTC4286_STATUS_MFR_SYS_RESET_DONE](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga6eedfb02e2dca41346990a7e28d6fdb6a9cafb7301150d97d54f9db5de0c4a839)
- [SENSOR_ATTR_LTC4286_STATUS_MFR_SYS_AVG_DONE](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga6eedfb02e2dca41346990a7e28d6fdb6a8bc8b2437114994ce23bc3fd222bd746)
- [SENSOR_ATTR_LTC4286_STATUS_MFR_SYS_ADC_CONV](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga6eedfb02e2dca41346990a7e28d6fdb6afabb7590aa82d45509d18f8f65df8d8c)
- [SENSOR_ATTR_LTC4286_STATUS_MFR_SYS_STAT2_SET](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga6eedfb02e2dca41346990a7e28d6fdb6a18c7eba895ed70aa0a9f4c6964810474)
- [SENSOR_ATTR_LTC4286_STATUS_MFR_SYS_POWER_FAILED_WARN](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga6eedfb02e2dca41346990a7e28d6fdb6a692e04be3bac9ea7fcc936caede7260e)
- [SENSOR_ATTR_LTC4286_STATUS_MFR_SYS_FET_SHORT_WARN](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga6eedfb02e2dca41346990a7e28d6fdb6a6aeea2c54ee697cce4c83071ab615a34)
- [SENSOR_ATTR_LTC4286_STATUS_MFR_SYS_VDS_UV_WARN](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga6eedfb02e2dca41346990a7e28d6fdb6a5b5ffafd9bb3f1f132a3d88b3d0e647c)
- [SENSOR_ATTR_LTC4286_STATUS_MFR_SYS_VDS_OV_WARN](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga6eedfb02e2dca41346990a7e28d6fdb6a89dc42832ef0c1385cf2e250d1a77778)
- [SENSOR_ATTR_LTC4286_STATUS_MFR_SYS_IOUT_UC_WARN](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga6eedfb02e2dca41346990a7e28d6fdb6a1dff38241b681226edc7086b5ae63234)
- [SENSOR_ATTR_LTC4286_STATUS_MFR_SYS_PIN_UP_WARN](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga6eedfb02e2dca41346990a7e28d6fdb6ab0fc47d97df92d27ca70c633553fe138)
- [SENSOR_ATTR_LTC4286_STATUS_MFR_SYS_END](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga6eedfb02e2dca41346990a7e28d6fdb6a08c5b57565d26823d920a092f243ed99)
- [ltc4286_adc_attr](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ga2e6b4da32c15bdc32757b8d70150668c)
- [SENSOR_ATTR_LTC4286_ADC_VDS_SELECT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga2e6b4da32c15bdc32757b8d70150668ca62ac8ece70184f5ebb8f42b473c696c1)
- [SENSOR_ATTR_LTC4286_ADC_VIN_VOUT_SELECT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga2e6b4da32c15bdc32757b8d70150668caf118081440de092c0f3f75259fdb0436)
- [SENSOR_ATTR_LTC4286_ADC_DISP_AVG](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga2e6b4da32c15bdc32757b8d70150668ca0604e8b290ccca2b6cd6344f9632ac33)
- [SENSOR_ATTR_LTC4286_ADC_AVG_SELECT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga2e6b4da32c15bdc32757b8d70150668ca1f07f3793542fe27b6c4d5a3fbaf0a15)
- [SENSOR_ATTR_LTC4286_ADC_END](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga2e6b4da32c15bdc32757b8d70150668cabd49d589e8aa52e97dc6cc4a5d1c4d34)
- [ltc4286_fault_response_attr](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ga6f7112063223c4239d44da489935d77d)
- [SENSOR_ATTR_LTC4286_FAULT_RESPONSE](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga6f7112063223c4239d44da489935d77da6aa180a6d86a9db7391709f23d35e8ce)
- [SENSOR_ATTR_LTC4286_FAULT_RETRY](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga6f7112063223c4239d44da489935d77da5e35f3e09e0c6ff8a8341ada128f75d7)
- [SENSOR_ATTR_LTC4286_FAULT_OP_TIMER](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga6f7112063223c4239d44da489935d77da6377166c22b256b607718cdd2c8c074f)
- [SENSOR_ATTR_LTC4286_FAULT_OV_RESPONSE](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga6f7112063223c4239d44da489935d77daacab96f7f4c1eb036912bc4daf1fc4c1)
- [SENSOR_ATTR_LTC4286_FAULT_OV_RETRY](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga6f7112063223c4239d44da489935d77dac1ffcae5766160fca39ea49b97e09b86)
- [SENSOR_ATTR_LTC4286_FAULT_UV_RESPONSE](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga6f7112063223c4239d44da489935d77daea8dd7b2943a49c093710949de7f4421)
- [SENSOR_ATTR_LTC4286_FAULT_UV_RETRY](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga6f7112063223c4239d44da489935d77da4f26ecf0df081f65f6cf05bcb92cf2bc)
- [SENSOR_ATTR_LTC4286_FAULT_END](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga6f7112063223c4239d44da489935d77dab727e59dc5722e57ab9648a6f197d9e1)
- [ltc4286_mfr_flt_attr](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gaa0f79aba4e22cce5f3e870928f946ce2)
- [SENSOR_ATTR_LTC4286_MFR_FLT_OP_TO_FAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggaa0f79aba4e22cce5f3e870928f946ce2aafedaa8e82311ea8fe3b7788b652e41c)
- [SENSOR_ATTR_LTC4286_MFR_FLT_OT_TO_FAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggaa0f79aba4e22cce5f3e870928f946ce2a1e78d93f08b9017c39641719ff520e34)
- [SENSOR_ATTR_LTC4286_MFR_FLT_END](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggaa0f79aba4e22cce5f3e870928f946ce2ad6f4e9771760b64ba601375a8a5ceb92)
- [ltc4286_reboot_control_attr](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ga1938c61b0c0bad9fa44ac235b2ee93ff)
- [SENSOR_ATTR_LTC4286_REBOOT_CONTROL_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga1938c61b0c0bad9fa44ac235b2ee93ffa97048b9a51696ba28f249a6a4c9ad60a)
- [SENSOR_ATTR_LTC4286_REBOOT_CONTROL_DELAY](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga1938c61b0c0bad9fa44ac235b2ee93ffa319fcfb878b3c67f5f073b2af3278173)
- [SENSOR_ATTR_LTC4286_REBOOT_CONTROL_END](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga1938c61b0c0bad9fa44ac235b2ee93ffada0c1ec9e66c0ba1eab0e9610b960630)
- [ltc4286_mfr_config_attr](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gac88db1417989518cdd4527f7a2e01e54)
- [SENSOR_ATTR_LTC4286_MFR_CONFIG_ILIM](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggac88db1417989518cdd4527f7a2e01e54ab0400e18f292468bb14d8827ad7e0c4a)
- [SENSOR_ATTR_LTC4286_MFR_CONFIG_VRANGE_SEL](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggac88db1417989518cdd4527f7a2e01e54a1f5384899ac3bd9fce80bd6ca22431e3)
- [SENSOR_ATTR_LTC4286_MFR_CONFIG_VPWR_SEL](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggac88db1417989518cdd4527f7a2e01e54a634f681d2371a7bb0aec6385d62e05b3)
- [SENSOR_ATTR_LTC4286_MFR_CONFIG_PMBUS_1MBIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggac88db1417989518cdd4527f7a2e01e54aeeca57673eb29fb4d3950cfe0a48046d)
- [SENSOR_ATTR_LTC4286_MFR_CONFIG_RESET_FAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggac88db1417989518cdd4527f7a2e01e54a43438d34b38ce27720f536817ab01b2b)
- [SENSOR_ATTR_LTC4286_MFR_CONFIG_PWR_GOOD_RESET_CTRL](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggac88db1417989518cdd4527f7a2e01e54a01439e02c9f2a80b905357f198801bfa)
- [SENSOR_ATTR_LTC4286_MFR_CONFIG_MASS_WRITE](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggac88db1417989518cdd4527f7a2e01e54a28d344bb18e17b837a040fc318ec4e0b)
- [SENSOR_ATTR_LTC4286_MFR_CONFIG_EXT_TEMP](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggac88db1417989518cdd4527f7a2e01e54a3455b31b53d1fb3b80d6a98644a61b62)
- [SENSOR_ATTR_LTC4286_MFR_CONFIG_DEBOUNCE_TIMER](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggac88db1417989518cdd4527f7a2e01e54a535dbd8ba286272fad039a79a761717d)
- [SENSOR_ATTR_LTC4286_MFR_CONFIG_END](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggac88db1417989518cdd4527f7a2e01e54a77a13cc382f69b773f73a44c0da379a1)
- [ltc4286_status_word_field](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gab6640bb8fd3260795923268b6b1de7bb)
- [LTC4286_STATUS_WORD_VOUT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggab6640bb8fd3260795923268b6b1de7bba308f513149ab916045f7e94b3867fc41)
- [LTC4286_STATUS_WORD_IOUT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggab6640bb8fd3260795923268b6b1de7bba0a2c685152c954bb0f61c1fb1069b720)
- [LTC4286_STATUS_WORD_INPUT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggab6640bb8fd3260795923268b6b1de7bbac7be0bb5c253eb935858bddb29ab1a71)
- [LTC4286_STATUS_WORD_MFRSPEC_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggab6640bb8fd3260795923268b6b1de7bba8fac5dd2a6443cfe2cfd9e269ef9500d)
- [LTC4286_STATUS_WORD_FET_UV_THRES_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggab6640bb8fd3260795923268b6b1de7bba3f0d7c311cdb59fbc546c911468d2e8e)
- [LTC4286_STATUS_WORD_OTHER_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggab6640bb8fd3260795923268b6b1de7bba248ae6611c20ffc6d552ea5c5c7e0905)
- [LTC4286_STATUS_WORD_UNKNOWN_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggab6640bb8fd3260795923268b6b1de7bba1dc7baa15f33a50107c3f661893f7115)
- [LTC4286_STATUS_WORD_BUSY_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggab6640bb8fd3260795923268b6b1de7bba09bc4e777d9f2f48c28e41f83ae8e85d)
- [LTC4286_STATUS_WORD_OFF_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggab6640bb8fd3260795923268b6b1de7bba4dca0688357b23f13d99b6ee58c73b0a)
- [LTC4286_STATUS_WORD_IOUT_OTHRES_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggab6640bb8fd3260795923268b6b1de7bbae13e246de568e56e465470cc1e5f9929)
- [LTC4286_STATUS_WORD_VIN_UTHRES_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggab6640bb8fd3260795923268b6b1de7bbaf5a5b2e03f910879af5e1ef416533524)
- [LTC4286_STATUS_WORD_TEMP_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggab6640bb8fd3260795923268b6b1de7bbacfc1f7b8ee11a46b2ce695d85aafd20c)
- [LTC4286_STATUS_WORD_COMLINE_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggab6640bb8fd3260795923268b6b1de7bba2aa72e38e64ea6d8a994f8bfb8948ee2)
- [LTC4286_STATUS_WORD_NOT_CLEAR_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggab6640bb8fd3260795923268b6b1de7bba70d7028f9858fe0ce549a17e8361554e)
- [ltc4286_status_vout_field](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gaa6eaf3246ef40abc22725abcd7ae6012)
- [LTC4286_VOUT_UV_WARNING_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggaa6eaf3246ef40abc22725abcd7ae6012a0da84e9a87aaa77f3ce416103a49aad9)
- [LTC4286_VOUT_OV_WARNING_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggaa6eaf3246ef40abc22725abcd7ae6012a567f2837c67e457952eca8c326229b3a)
- [ltc4286_status_iout_field](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ga421f54d62139840db517225de8c89460)
- [LTC4286_IOUT_OC_WARNING_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga421f54d62139840db517225de8c89460adb351f06ccfd05f6ccc3c19ecdac43d1)
- [LTC4286_IOUT_OC_FAULT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga421f54d62139840db517225de8c89460a304579c60e9942fd90750c8bbe2470a3)
- [ltc4286_status_input_field](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ga7c3cb25fe7c8dae8e12e9c861a1c0952)
- [LTC4286_PIN_OP_WARNING_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga7c3cb25fe7c8dae8e12e9c861a1c0952afaa9ba1964d8a9e02771b118135d5b03)
- [LTC4286_VIN_UV_FAULT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga7c3cb25fe7c8dae8e12e9c861a1c0952a390b9abe80531006bc156d092cc47027)
- [LTC4286_VIN_UV_WARNING_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga7c3cb25fe7c8dae8e12e9c861a1c0952aab0f5a3a4ece540f7193890e17ced6f7)
- [LTC4286_VIN_OV_WARNING_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga7c3cb25fe7c8dae8e12e9c861a1c0952a61be92e1a593adaa3cd29728fde1c58c)
- [LTC4286_VIN_OV_FAULT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga7c3cb25fe7c8dae8e12e9c861a1c0952a0d328f79596af042369e610973cd0045)
- [ltc4286_status_temp_field](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ga9fce26b6b719d1a030c870651cc6aec8)
- [LTC4286_TEMP_UT_WARNING_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga9fce26b6b719d1a030c870651cc6aec8adf9fe69263b87c66f16e8ea28599952c)
- [LTC4286_TEMP_OT_WARNING_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga9fce26b6b719d1a030c870651cc6aec8a0456e4913bc4c1c35bbd81b9ae15f432)
- [LTC4286_TEMP_OT_FAULT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga9fce26b6b719d1a030c870651cc6aec8a08ed840142dbf146ec17e2abd59c6722)
- [ltc4286_status_cml_field](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gab268b8865c4a1fc30719d09a8ba9c6fb)
- [LTC4286_MISC_FAULT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggab268b8865c4a1fc30719d09a8ba9c6fba16b198e9902806940e9474bebcb8ed1a)
- [LTC4286_PEC_FAILED_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggab268b8865c4a1fc30719d09a8ba9c6fba97e37a21dd64ddfb2168bd24dde47170)
- [LTC4286_BAD_DATA_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggab268b8865c4a1fc30719d09a8ba9c6fba486a7f6f829372515183ef1cf44582d8)
- [LTC4286_BAD_CMD_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggab268b8865c4a1fc30719d09a8ba9c6fba2c23efc3d80d525d02b57c56bc2bfa45)
- [ltc4286_status_other_field](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ga5988afbf2abc6e5c5e313d81b683a625)
- [LTC4286_OTHER_FIRST_ALERT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga5988afbf2abc6e5c5e313d81b683a625acb755b4721a106941af3f61546c900b2)
- [ltc4286_status_mfr_spec_field](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ga0d9d60ecc24cdf24642d8d45ee228bf1)
- [LTC4286_MFR_SPEC_FET_BAD_FAULT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga0d9d60ecc24cdf24642d8d45ee228bf1a7da6c9efea8b135115b3aea9f484e1e3)
- [LTC4286_MFR_SPEC_PIN_OP1_FAULT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga0d9d60ecc24cdf24642d8d45ee228bf1a437bc24955298f29d2e92839a67f7235)
- [LTC4286_MFR_SPEC_PIN_OP2_FAULT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga0d9d60ecc24cdf24642d8d45ee228bf1a43bff18b66e0d4f0f81740066538a47d)
- [LTC4286_MFR_SPEC_VDD_UVLO_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga0d9d60ecc24cdf24642d8d45ee228bf1a3f9e3c2436203afdf12029d230d77f1b)
- [LTC4286_MFR_SPEC_TSD_FAULT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga0d9d60ecc24cdf24642d8d45ee228bf1a8e56294d86cf87b4ad4bd49a4057f128)
- [LTC4286_MFR_SPEC_EN_CHANGED_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga0d9d60ecc24cdf24642d8d45ee228bf1aaad799bcf0ddd7c809f110ebbc68898b)
- [ltc4286_mfr_sys_status1_field](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gae371b2b0685c34a368909636fd63a9d0)
- [LTC4286_MFR_SYS_STATUS1_ADC_CONV_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggae371b2b0685c34a368909636fd63a9d0a2941657ebb7951dd2b3f56ebeb593e8b)
- [LTC4286_MFR_SYS_STATUS1_AVERAGE_DONE_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggae371b2b0685c34a368909636fd63a9d0a408d62e976b770b1662f7d433363f393)
- [LTC4286_MFR_SYS_STATUS1_RESET_DONE_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggae371b2b0685c34a368909636fd63a9d0a33171b5d99b2e7a867593a99523f817c)
- [LTC4286_MFR_SYS_STATUS1_POWER_LOSS_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggae371b2b0685c34a368909636fd63a9d0ab7a202d2b6d9081d4cbae6e46bd7f824)
- [LTC4286_MFR_SYS_STATUS1_L_ALERT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggae371b2b0685c34a368909636fd63a9d0a6138631a9dbcaa9db1b5af1cabc9add6)
- [LTC4286_MFR_SYS_STATUS1_ALERT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggae371b2b0685c34a368909636fd63a9d0a634ea0ebce11fb4998cec9d4f265c5a0)
- [ltc4286_mfr_sys_status2_field](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ga93a666fb5258e905627800edbf68c136)
- [LTC4286_MFR_SYS_STATUS2_PIN_UP_WARNING_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga93a666fb5258e905627800edbf68c136a4d5e23e4ae55658b779c3eba74c4dd88)
- [LTC4286_MFR_SYS_STATUS2_IOUT_UC_WARNING_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga93a666fb5258e905627800edbf68c136a5b6f270f484a04bda891b83b082cbe94)
- [LTC4286_MFR_SYS_STATUS2_VDS_UV_WARNING_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga93a666fb5258e905627800edbf68c136ae4a4f6ee801e8c3f5af6ecd3fd709ffd)
- [LTC4286_MFR_SYS_STATUS2_VDS_OV_WARNING_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga93a666fb5258e905627800edbf68c136a39098a539e90cdb34bf0e43babef4a6c)
- [LTC4286_MFR_SYS_STATUS2_FET_SHORT_WARNING_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga93a666fb5258e905627800edbf68c136ae3aa56ba7b44dd284fc4972fe16f3768)
- [LTC4286_MFR_SYS_STATUS2_POWER_FAILED_WARNING_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga93a666fb5258e905627800edbf68c136aa4c62a23cc0de36d33ae8416718872c0)
- [ltc4286_trig_alert_mask](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ga87bd44a44c010f3217753ef01692d197)
- [LTC4286_ALERT_STATUS_WORD_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga87bd44a44c010f3217753ef01692d197a686fe737e40fcbe8c7687ef28e5eef1c)
- [LTC4286_ALERT_STATUS_VOUT_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga87bd44a44c010f3217753ef01692d197a1158bafacebec83c24fe803db9ddcbc4)
- [LTC4286_ALERT_STATUS_IOUT_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga87bd44a44c010f3217753ef01692d197a29a3ef4fed472087dd98a638f02170dd)
- [LTC4286_ALERT_STATUS_INPUT_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga87bd44a44c010f3217753ef01692d197a530596e6edf454c0c7b51f014ffedcbd)
- [LTC4286_ALERT_STATUS_TEMP_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga87bd44a44c010f3217753ef01692d197af6ecd677a77d5d346a473e7d406563af)
- [LTC4286_ALERT_STATUS_COMMS_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga87bd44a44c010f3217753ef01692d197aeb6ecdbfc7a5a28ce0f8a088ef266229)
- [LTC4286_ALERT_STATUS_SPEC_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga87bd44a44c010f3217753ef01692d197a5539b96ff27b9cf3d23556942d885890)
- [LTC4286_ALERT_STATUS_SYS1_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga87bd44a44c010f3217753ef01692d197a3568c1477227384dd7cb1706d514c16c)
- [LTC4286_ALERT_STATUS_SYS2_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga87bd44a44c010f3217753ef01692d197a2eaf109ed2286e4eea758524edc0e670)
- [ltc4286_status_alert](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gac9d479a89a01f734c22ee50d6d4da320)
- [LTC4286_ALERT_STATUS_BUSY_ALERT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggac9d479a89a01f734c22ee50d6d4da320af8a362cbf236a827c6e7a002f0baf9f5)
- [ltc4286_vout_alert](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gaf8e9b09707496eeeb74f75928939d7b2)
- [LTC4286_ALERT_VOUT_UV_WARNING_ALERT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggaf8e9b09707496eeeb74f75928939d7b2a4649ef806ce413a712939ae2c0376f48)
- [LTC4286_ALERT_VOUT_OV_WARNING_ALERT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggaf8e9b09707496eeeb74f75928939d7b2ac001fac5a12e81b747412386bf4cf1bf)
- [ltc4286_iout_alert](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gad67f6528db32f57693c40d3dd703b681)
- [LTC4286_ALERT_IOUT_OC_WARNING_ALERT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggad67f6528db32f57693c40d3dd703b681adcd36ec46ef007cd1eecb40b6ced7ec0)
- [LTC4286_ALERT_IOUT_OC_FAULT_ALERT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggad67f6528db32f57693c40d3dd703b681aefcd18ed435f05b1d2b322a93f148791)
- [ltc4286_input_alert](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ga7526494801158c04caf40d182f6dce15)
- [LTC4286_ALERT_PIN_OP_WARNING_ALERT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga7526494801158c04caf40d182f6dce15ad0c111fde33a734c79c1435a685e6892)
- [LTC4286_ALERT_VIN_UV_FAULT_ALERT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga7526494801158c04caf40d182f6dce15a3831c49adc47592651a8a69b7d5917fe)
- [LTC4286_ALERT_VIN_UV_WARNING_ALERT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga7526494801158c04caf40d182f6dce15afd4aa1521a27bbfdb6d35eda2091bc67)
- [LTC4286_ALERT_VIN_OV_WARNING_ALERT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga7526494801158c04caf40d182f6dce15a5f8b52779738dc7927b4610b7ecc41e6)
- [LTC4286_ALERT_VIN_OV_FAULT_ALERT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga7526494801158c04caf40d182f6dce15a3c9f198af6d725e871d8d5ee803af23c)
- [ltc4286_temp_alert](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gabbe9371859d1a073a7d496e18c7e7fbf)
- [LTC4286_ALERT_TEMP_UT_WARNING_ALERT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggabbe9371859d1a073a7d496e18c7e7fbfa286c47cdfd02d3d95003fbd9768a76fc)
- [LTC4286_ALERT_TEMP_OT_WARNING_ALERT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggabbe9371859d1a073a7d496e18c7e7fbfabc3617a0ee54faba1a42168cf35a2ead)
- [LTC4286_ALERT_TEMP_OT_FAULT_ALERT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggabbe9371859d1a073a7d496e18c7e7fbfa98b656ecf055b656e6d43bfbb3e1d430)
- [ltc4286_cml_alert](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ga57e786e009c96bb70e3219f237a15c06)
- [LTC4286_ALERT_MISC_FAULT_ALERT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga57e786e009c96bb70e3219f237a15c06a278dff3fdd95b48545fa5115260ffaaf)
- [LTC4286_ALERT_PEC_FAILED_ALERT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga57e786e009c96bb70e3219f237a15c06a4d08f5aec4bdafc87c7cffb7c0c7eedd)
- [LTC4286_ALERT_BAD_DATA_ALERT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga57e786e009c96bb70e3219f237a15c06a3214d38cb44d5941c0f12f1f6c918926)
- [LTC4286_ALERT_BAD_CMD_ALERT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga57e786e009c96bb70e3219f237a15c06a31560620795f69bc7413c40c966895e6)
- [ltc4286_mfr_spec_alert](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gaed0a6e6bfd48646648ca0be09c159cf9)
- [LTC4286_ALERT_MFR_SPEC_FET_BAD_FAULT_ALERT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggaed0a6e6bfd48646648ca0be09c159cf9a87f4fa895950d9372a0360f51eed2014)
- [LTC4286_ALERT_MFR_SPEC_PIN_OP1_FAULT_ALERT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggaed0a6e6bfd48646648ca0be09c159cf9afa7a71ed3e9070edb29337defe59864d)
- [LTC4286_ALERT_MFR_SPEC_PIN_OP2_FAULT_ALERT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggaed0a6e6bfd48646648ca0be09c159cf9a2fbb3b72a62a00dae31ac7182453c0df)
- [LTC4286_ALERT_MFR_SPEC_VDD_UVLO_ALERT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggaed0a6e6bfd48646648ca0be09c159cf9a3db277ece640f40cd94335270121571e)
- [LTC4286_ALERT_MFR_SPEC_TSD_FAULT_ALERT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggaed0a6e6bfd48646648ca0be09c159cf9a68841a5e5e02a6c86b1b843f34622fff)
- [LTC4286_ALERT_MFR_SPEC_EN_CHANGED_ALERT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ggaed0a6e6bfd48646648ca0be09c159cf9a341b004b65a366e1427fbcc2d97a5aea)
- [ltc4286_mfr_sys_status1_alert](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ga020ba354df79f5f303f1dec20921f437)
- [LTC4286_ALERT_MFR_SYS_STATUS1_ADC_CONV_ALERT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga020ba354df79f5f303f1dec20921f437a71d5c851425aecf276735d683232cf73)
- [LTC4286_ALERT_MFR_SYS_STATUS1_AVERAGE_DONE_ALERT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga020ba354df79f5f303f1dec20921f437a4849e58229af61943d3f2ebe3e5b571f)
- [LTC4286_ALERT_MFR_SYS_STATUS1_RESET_DONE_ALERT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga020ba354df79f5f303f1dec20921f437ab52efeeb323fbf5e1a6cd463604c8ff0)
- [LTC4286_ALERT_MFR_SYS_STATUS1_POWER_LOSS_ALERT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga020ba354df79f5f303f1dec20921f437a2bfd7d61084376bc321a98e4b6a3caa6)
- [ltc4286_mfr_sys_status2_alert](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#ga03dbaeaf95da8e9301af652a85aa6c3b)
- [LTC4286_ALERT_MFR_SYS_STATUS2_PIN_UP_WARNING_ALERT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga03dbaeaf95da8e9301af652a85aa6c3ba778d69f3db4f343a9d39dd5e13dc9188)
- [LTC4286_ALERT_MFR_SYS_STATUS2_IOUT_UC_WARNING_ALERT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga03dbaeaf95da8e9301af652a85aa6c3baf7a755ef4af37d545306054ef79754a0)
- [LTC4286_ALERT_MFR_SYS_STATUS2_VDS_UV_WARNING_ALERT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga03dbaeaf95da8e9301af652a85aa6c3ba98b17102db6f41df3f864ed1e33a5a02)
- [LTC4286_ALERT_MFR_SYS_STATUS2_VDS_OV_WARNING_ALERT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga03dbaeaf95da8e9301af652a85aa6c3ba1c7aaf3825fde01d85e013c78cb76314)
- [LTC4286_ALERT_MFR_SYS_STATUS2_FET_SHORT_WARNING_ALERT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga03dbaeaf95da8e9301af652a85aa6c3ba963de7dee7857255e50d6835354808b2)
- [LTC4286_ALERT_MFR_SYS_STATUS2_POWER_FAILED_WARNING_ALERT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gga03dbaeaf95da8e9301af652a85aa6c3ba369bb3c1589e7c272def1c3c0caccc69)
- [ltc4286_enable_alert_mask](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gafe5f106d027ee4660006d104dba5c162)
- [device](../device_reference/P002_设备对象结构.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [ltc4286_disable_alert_mask](https://docs.zephyrproject.org/latest/doxygen/html/group__ltc4286__interface.html#gafc1ccc72d2b1792f4b4144e4e0633cb5)

<a id="header-details"></a>

---

[上一章](P007_zephyr__dt-bindings__clock__lpc84x-clock.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P009_zephyr__dt-bindings__gpio__m2-memory-connector.h_文件参考.md)

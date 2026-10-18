---
id: learning.zephyr-docs.api-source-timing-sensor-reference.page-8
title: msos_desc.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/msos__desc_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_msos\_desc.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/msos__desc_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P232_zephyr__usb__msos_desc.h_文件参考.md)。

## 8.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="foldopen00018"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="foldopen00023"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="foldopen00035"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="foldopen00047"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="foldopen00057"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="foldopen00068"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="foldopen00077"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="foldopen00085"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="foldopen00096"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="foldopen00103"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="foldopen00111"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="foldopen00118"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="foldopen00124"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="amsos__desc_8h_html_a1afad4029116a837d4430a0ea976254f"></a>
<a id="amsos__desc_8h_html_a1afad4029116a837d4430a0ea976254fa404430118680c625a399662e981c4489"></a>
<a id="amsos__desc_8h_html_a1afad4029116a837d4430a0ea976254fa4050949a26b3a61f1aeecc996eb02d81"></a>
<a id="amsos__desc_8h_html_a1afad4029116a837d4430a0ea976254fa89b2d8dfbddc343879edc14a5c9f93f5"></a>
<a id="amsos__desc_8h_html_a1afad4029116a837d4430a0ea976254fa9245e361cbe8425c1b54958ba0c0902c"></a>
<a id="amsos__desc_8h_html_a1afad4029116a837d4430a0ea976254fa969e1f96f1582db317bbf96d183ae670"></a>
<a id="amsos__desc_8h_html_a1afad4029116a837d4430a0ea976254faa831bf4ba88de3eb768745c41a8dee10"></a>
<a id="amsos__desc_8h_html_a1afad4029116a837d4430a0ea976254fac1e0035b4badb15f714bff249514ef17"></a>
<a id="amsos__desc_8h_html_a1afad4029116a837d4430a0ea976254fae8bd325ca3f9cc1d33d229d0de14aba1"></a>
<a id="amsos__desc_8h_html_ab443ad91634b7a8fb19fc2aa7108e631"></a>
<a id="amsos__desc_8h_html_ab443ad91634b7a8fb19fc2aa7108e631a2ae9d4948f03b7d9623c547daa0a9116"></a>
<a id="amsos__desc_8h_html_ab443ad91634b7a8fb19fc2aa7108e631abe0e6e00164db250e4ad900f418a57d5"></a>
<a id="amsos__desc_8h_html_ae46389cacf4c5cca962702fcf0f6feb5"></a>
<a id="amsos__desc_8h_html_ae46389cacf4c5cca962702fcf0f6feb5a1200730075635cba8dea3420be41d1a7"></a>
<a id="amsos__desc_8h_html_ae46389cacf4c5cca962702fcf0f6feb5a2f7940f495e1a996692f474a456d63d6"></a>
<a id="amsos__desc_8h_html_ae46389cacf4c5cca962702fcf0f6feb5a7061acf1dbbeb7e2fbb88d149d295009"></a>
<a id="amsos__desc_8h_html_ae46389cacf4c5cca962702fcf0f6feb5ab457a91ffd658376d87d7d32ad770004"></a>
<a id="amsos__desc_8h_html_ae46389cacf4c5cca962702fcf0f6feb5ac74a28d4e873b255d5b027af5ffffb5d"></a>
<a id="amsos__desc_8h_html_ae46389cacf4c5cca962702fcf0f6feb5ac7fc46a0124656e986871ae3b085536c"></a>
<a id="amsos__desc_8h_html_ae46389cacf4c5cca962702fcf0f6feb5ad49ae449e2e2ff519a69018612ab5e62"></a>
<a id="amsos__desc_8h_html_ae46389cacf4c5cca962702fcf0f6feb5adf3b0e226fd373b882e27ed494fba265"></a>
<a id="amsos__desc_8h_html_ae46389cacf4c5cca962702fcf0f6feb5afe117782c0101a880e152a8a1110ecbc"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructmsosv2__ccgp__device_html"></a>
<a id="astructmsosv2__ccgp__device_html_a43cc94903315cb1a09418325630f936c"></a>
<a id="astructmsosv2__ccgp__device_html_af3713e6a6185c8725d21fd5f1edbf84a"></a>
<a id="astructmsosv2__compatible__id_html"></a>
<a id="astructmsosv2__compatible__id_html_a213f32b16fda92bc5526abee2d5922b5"></a>
<a id="astructmsosv2__compatible__id_html_ad2fabcbcfe86dd7f6c7e21607392ed9f"></a>
<a id="astructmsosv2__compatible__id_html_adfb121211a3e2519cdbf3afa91cd48e3"></a>
<a id="astructmsosv2__compatible__id_html_affc8c55b00ddcc20841054ac8d8c6844"></a>
<a id="astructmsosv2__configuration__subset__header_html"></a>
<a id="astructmsosv2__configuration__subset__header_html_a044cf7d76fa93bfaa265bd5c24d8d413"></a>
<a id="astructmsosv2__configuration__subset__header_html_a044e9d3a0ec479564406f04d895e353c"></a>
<a id="astructmsosv2__configuration__subset__header_html_a7468f6428046553abf5e97172b52d477"></a>
<a id="astructmsosv2__configuration__subset__header_html_aa063ff78775c00edde1de6e274a2b817"></a>
<a id="astructmsosv2__configuration__subset__header_html_ada03982dd6680a45d7cd2ba9e791c54e"></a>
<a id="astructmsosv2__descriptor__set__header_html"></a>
<a id="astructmsosv2__descriptor__set__header_html_a3bab654cec13541096f08b43adb55f40"></a>
<a id="astructmsosv2__descriptor__set__header_html_a4281eeb2128138b597fb53577ec8d57f"></a>
<a id="astructmsosv2__descriptor__set__header_html_acf91f874e365a7f8ef60eaa19da517b4"></a>
<a id="astructmsosv2__descriptor__set__header_html_ae4931afed75f035e9dff4856ddee8609"></a>
<a id="astructmsosv2__function__subset__header_html"></a>
<a id="astructmsosv2__function__subset__header_html_a07a64f2419014f41fa356fd85976985d"></a>
<a id="astructmsosv2__function__subset__header_html_a10e00ccb02a6e2c9c4c5f4d634414a0c"></a>
<a id="astructmsosv2__function__subset__header_html_a4a93fdd2d9ea65b5b9097f921629c644"></a>
<a id="astructmsosv2__function__subset__header_html_a7c3d3e7cd0577dc4ceab66615fefbe46"></a>
<a id="astructmsosv2__function__subset__header_html_abf8bbff467411af8f259d2f16dc73649"></a>
<a id="astructmsosv2__guids__property_html"></a>
<a id="astructmsosv2__guids__property_html_a1740a7fb0134313dba90cf794f0218f1"></a>
<a id="astructmsosv2__guids__property_html_a500199bebfa7f8bf300be51310497a0c"></a>
<a id="astructmsosv2__guids__property_html_a815f24af18f726244a9ab7d9f67e1cab"></a>
<a id="astructmsosv2__guids__property_html_abf28542190ae7fececadacd3e8dba58a"></a>
<a id="astructmsosv2__guids__property_html_ac447835ec1446a2e190228cab2b7dca8"></a>
<a id="astructmsosv2__guids__property_html_acaa81e6bbaaec95922a80ef5a6000cd9"></a>
<a id="astructmsosv2__guids__property_html_aee143372e2bd13a32ae61e68ab429fbe"></a>
<a id="astructmsosv2__model__id_html"></a>
<a id="astructmsosv2__model__id_html_a2355b2ab759e661462d61ffbdb7c29cd"></a>
<a id="astructmsosv2__model__id_html_ae87e515d83e0f979c993ef24d2486d08"></a>
<a id="astructmsosv2__model__id_html_af03a88860ff6086b0cda956f2ccff824"></a>
<a id="astructmsosv2__resume__time_html"></a>
<a id="astructmsosv2__resume__time_html_a1a08a4ec1b884a68ffc6b52a84e747aa"></a>
<a id="astructmsosv2__resume__time_html_a22fc11df55af95324cfeb2459a544bd4"></a>
<a id="astructmsosv2__resume__time_html_a33ff93b8c7d97dc9732158b2293cd377"></a>
<a id="astructmsosv2__resume__time_html_a95a1ba0d9e5d0019dfeabfea0ddaf205"></a>
<a id="astructmsosv2__vendor__revision_html"></a>
<a id="astructmsosv2__vendor__revision_html_a4b29a145268e89c416f50cddc28f0ff4"></a>
<a id="astructmsosv2__vendor__revision_html_a6ad0f9afb827947e4e2bfca339b70ceb"></a>
<a id="astructmsosv2__vendor__revision_html_aebed4cce3752a96a82fb25e3071a021c"></a>

```c
/*
 * Copyright (c) 2023 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_USB_MSOS_DESC_H
#define ZEPHYR_INCLUDE_USB_MSOS_DESC_H

#include <stdint.h>

enum msosv2_descriptor_index {
        MS_OS_20_DESCRIPTOR_INDEX               = 0x07,
        MS_OS_20_SET_ALT_ENUMERATION            = 0x08,
};

enum msosv2_descriptor_type {
        MS_OS_20_SET_HEADER_DESCRIPTOR          = 0x00,
        MS_OS_20_SUBSET_HEADER_CONFIGURATION    = 0x01,
        MS_OS_20_SUBSET_HEADER_FUNCTION         = 0x02,
        MS_OS_20_FEATURE_COMPATIBLE_ID          = 0x03,
        MS_OS_20_FEATURE_REG_PROPERTY           = 0x04,
        MS_OS_20_FEATURE_MIN_RESUME_TIME        = 0x05,
        MS_OS_20_FEATURE_MODEL_ID               = 0x06,
        MS_OS_20_FEATURE_CCGP_DEVICE            = 0x07,
        MS_OS_20_FEATURE_VENDOR_REVISION        = 0x08
};

enum msosv2_property_data_type {
        MS_OS_20_PROPERTY_DATA_RESERVED                 = 0,
        MS_OS_20_PROPERTY_DATA_REG_SZ                   = 1,
        MS_OS_20_PROPERTY_DATA_REG_EXPAND_SZ            = 2,
        MS_OS_20_PROPERTY_DATA_REG_BINARY               = 3,
        MS_OS_20_PROPERTY_DATA_REG_DWORD_LITTLE_ENDIAN  = 4,
        MS_OS_20_PROPERTY_DATA_REG_DWORD_BIG_ENDIAN     = 5,
        MS_OS_20_PROPERTY_DATA_REG_LINK                 = 6,
        MS_OS_20_PROPERTY_DATA_REG_MULTI_SZ             = 7
};

/* Microsoft OS 2.0 descriptor set header */
struct msosv2_descriptor_set_header {
        uint16_t wLength;
        uint16_t wDescriptorType;
        uint32_t dwWindowsVersion;
        uint16_t wTotalLength;
} __packed;

/* Microsoft OS 2.0 configuration subset header
 * This header is for composite devices with multiple configurations.
 */
struct msosv2_configuration_subset_header {
        uint16_t wLength;
        uint16_t wDescriptorType;
        uint8_t bConfigurationValue;
        uint8_t bReserved;
        uint16_t wTotalLength;
} __packed;

/* Microsoft OS 2.0 function subset header
 * Note: This must be used if your device has multiple interfaces and cannot be used otherwise.
 */
struct msosv2_function_subset_header {
        uint16_t wLength;
        uint16_t wDescriptorType;
        uint8_t bFirstInterface;
        uint8_t bReserved;
        uint16_t wSubsetLength;
} __packed;

/* Microsoft OS 2.0 compatible ID descriptor */
struct msosv2_compatible_id {
        uint16_t wLength;
        uint16_t wDescriptorType;
        uint8_t CompatibleID[8];
        uint8_t SubCompatibleID[8];
} __packed;

/* Microsoft OS 2.0 Registry property descriptor: DeviceInterfaceGUIDs */
struct msosv2_guids_property {
        uint16_t wLength;
        uint16_t wDescriptorType;
        uint16_t wPropertyDataType;
        uint16_t wPropertyNameLength;
        uint8_t PropertyName[42];
        uint16_t wPropertyDataLength;
        uint8_t bPropertyData[80];
} __packed;

/* DeviceInterfaceGUIDs */
#define DEVICE_INTERFACE_GUIDS_PROPERTY_NAME \
        'D', 0x00, 'e', 0x00, 'v', 0x00, 'i', 0x00, 'c', 0x00, 'e', 0x00, \
        'I', 0x00, 'n', 0x00, 't', 0x00, 'e', 0x00, 'r', 0x00, 'f', 0x00, \
        'a', 0x00, 'c', 0x00, 'e', 0x00, 'G', 0x00, 'U', 0x00, 'I', 0x00, \
        'D', 0x00, 's', 0x00, 0x00, 0x00

/* Microsoft OS 2.0 minimum USB resume time descriptor */
struct msosv2_resume_time {
        uint16_t wLength;
        uint16_t wDescriptorType;
        uint8_t bResumeRecoveryTime;
        uint8_t bResumeSignalingTime;
} __packed;

/* Microsoft OS 2.0 model ID descriptor */
struct msosv2_model_id {
        uint16_t wLength;
        uint16_t wDescriptorType;
        uint8_t ModelID[16];
} __packed;

/* Microsoft OS 2.0 CCGP device descriptor */
struct msosv2_ccgp_device {
        uint16_t wLength;
        uint16_t wDescriptorType;
} __packed;

/* Microsoft OS 2.0 vendor revision descriptor */
struct msosv2_vendor_revision {
        uint16_t wLength;
        uint16_t wDescriptorType;
        uint16_t VendorRevision;
} __packed;


#endif /* ZEPHYR_INCLUDE_USB_MSOS_DESC_H */
```

## 8.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 46 行

Microsoft OS 2.0 描述符集首部（descriptor set header）。

### 注释 3：原第 54 行

Microsoft OS 2.0 配置子集首部（configuration subset header）。此首部用于具有多个配置的复合设备（composite devices）。

### 注释 4：原第 65 行

Microsoft OS 2.0 功能子集首部（function subset header）。注意：设备具有多个接口时必须使用此首部；其他情况下不得使用。

### 注释 5：原第 76 行

Microsoft OS 2.0 兼容标识符描述符（compatible ID descriptor）。

### 注释 6：原第 84 行

Microsoft OS 2.0 注册表属性描述符（Registry property descriptor）：`DeviceInterfaceGUIDs`。

### 注释 7：原第 95 行

设备接口 GUID 属性：`DeviceInterfaceGUIDs`。

### 注释 8：原第 102 行

Microsoft OS 2.0 最短 USB 恢复时间描述符（minimum USB resume time descriptor）。

### 注释 9：原第 110 行

Microsoft OS 2.0 模型标识符描述符（model ID descriptor）。

### 注释 10：原第 117 行

Microsoft OS 2.0 CCGP 设备描述符（device descriptor）。

### 注释 11：原第 123 行

Microsoft OS 2.0 厂商修订版本描述符（vendor revision descriptor）。

### 注释 12：原第 131 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_USB_MSOS_DESC_H`。

## 8.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P232_zephyr__usb__msos_desc.h_文件参考.md)
- [stdint.h](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md)
- [msosv2_descriptor_index](../api_file_reference/P232_zephyr__usb__msos_desc.h_文件参考.md#ab443ad91634b7a8fb19fc2aa7108e631)
- [MS_OS_20_DESCRIPTOR_INDEX](../api_file_reference/P232_zephyr__usb__msos_desc.h_文件参考.md#ab443ad91634b7a8fb19fc2aa7108e631abe0e6e00164db250e4ad900f418a57d5)
- [MS_OS_20_SET_ALT_ENUMERATION](../api_file_reference/P232_zephyr__usb__msos_desc.h_文件参考.md#ab443ad91634b7a8fb19fc2aa7108e631a2ae9d4948f03b7d9623c547daa0a9116)
- [msosv2_descriptor_type](../api_file_reference/P232_zephyr__usb__msos_desc.h_文件参考.md#ae46389cacf4c5cca962702fcf0f6feb5)
- [MS_OS_20_SET_HEADER_DESCRIPTOR](../api_file_reference/P232_zephyr__usb__msos_desc.h_文件参考.md#ae46389cacf4c5cca962702fcf0f6feb5ac74a28d4e873b255d5b027af5ffffb5d)
- [MS_OS_20_SUBSET_HEADER_CONFIGURATION](../api_file_reference/P232_zephyr__usb__msos_desc.h_文件参考.md#ae46389cacf4c5cca962702fcf0f6feb5afe117782c0101a880e152a8a1110ecbc)
- [MS_OS_20_SUBSET_HEADER_FUNCTION](../api_file_reference/P232_zephyr__usb__msos_desc.h_文件参考.md#ae46389cacf4c5cca962702fcf0f6feb5a1200730075635cba8dea3420be41d1a7)
- [MS_OS_20_FEATURE_COMPATIBLE_ID](../api_file_reference/P232_zephyr__usb__msos_desc.h_文件参考.md#ae46389cacf4c5cca962702fcf0f6feb5adf3b0e226fd373b882e27ed494fba265)
- [MS_OS_20_FEATURE_REG_PROPERTY](../api_file_reference/P232_zephyr__usb__msos_desc.h_文件参考.md#ae46389cacf4c5cca962702fcf0f6feb5ad49ae449e2e2ff519a69018612ab5e62)
- [MS_OS_20_FEATURE_MIN_RESUME_TIME](../api_file_reference/P232_zephyr__usb__msos_desc.h_文件参考.md#ae46389cacf4c5cca962702fcf0f6feb5a7061acf1dbbeb7e2fbb88d149d295009)
- [MS_OS_20_FEATURE_MODEL_ID](../api_file_reference/P232_zephyr__usb__msos_desc.h_文件参考.md#ae46389cacf4c5cca962702fcf0f6feb5ac7fc46a0124656e986871ae3b085536c)
- [MS_OS_20_FEATURE_CCGP_DEVICE](../api_file_reference/P232_zephyr__usb__msos_desc.h_文件参考.md#ae46389cacf4c5cca962702fcf0f6feb5ab457a91ffd658376d87d7d32ad770004)
- [MS_OS_20_FEATURE_VENDOR_REVISION](../api_file_reference/P232_zephyr__usb__msos_desc.h_文件参考.md#ae46389cacf4c5cca962702fcf0f6feb5a2f7940f495e1a996692f474a456d63d6)
- [msosv2_property_data_type](../api_file_reference/P232_zephyr__usb__msos_desc.h_文件参考.md#a1afad4029116a837d4430a0ea976254f)
- [MS_OS_20_PROPERTY_DATA_RESERVED](../api_file_reference/P232_zephyr__usb__msos_desc.h_文件参考.md#a1afad4029116a837d4430a0ea976254fac1e0035b4badb15f714bff249514ef17)
- [MS_OS_20_PROPERTY_DATA_REG_SZ](../api_file_reference/P232_zephyr__usb__msos_desc.h_文件参考.md#a1afad4029116a837d4430a0ea976254fa404430118680c625a399662e981c4489)
- [MS_OS_20_PROPERTY_DATA_REG_EXPAND_SZ](../api_file_reference/P232_zephyr__usb__msos_desc.h_文件参考.md#a1afad4029116a837d4430a0ea976254fa9245e361cbe8425c1b54958ba0c0902c)
- [MS_OS_20_PROPERTY_DATA_REG_BINARY](../api_file_reference/P232_zephyr__usb__msos_desc.h_文件参考.md#a1afad4029116a837d4430a0ea976254fae8bd325ca3f9cc1d33d229d0de14aba1)
- [MS_OS_20_PROPERTY_DATA_REG_DWORD_LITTLE_ENDIAN](../api_file_reference/P232_zephyr__usb__msos_desc.h_文件参考.md#a1afad4029116a837d4430a0ea976254faa831bf4ba88de3eb768745c41a8dee10)
- [MS_OS_20_PROPERTY_DATA_REG_DWORD_BIG_ENDIAN](../api_file_reference/P232_zephyr__usb__msos_desc.h_文件参考.md#a1afad4029116a837d4430a0ea976254fa969e1f96f1582db317bbf96d183ae670)
- [MS_OS_20_PROPERTY_DATA_REG_LINK](../api_file_reference/P232_zephyr__usb__msos_desc.h_文件参考.md#a1afad4029116a837d4430a0ea976254fa4050949a26b3a61f1aeecc996eb02d81)
- [MS_OS_20_PROPERTY_DATA_REG_MULTI_SZ](../api_file_reference/P232_zephyr__usb__msos_desc.h_文件参考.md#a1afad4029116a837d4430a0ea976254fa89b2d8dfbddc343879edc14a5c9f93f5)
- [msosv2_descriptor_set_header](../device_power_control_model_reference/P037_msosv2_descriptor_set_header_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [wLength](../device_power_control_model_reference/P037_msosv2_descriptor_set_header_结构体.md#a4281eeb2128138b597fb53577ec8d57f)
- [wDescriptorType](../device_power_control_model_reference/P037_msosv2_descriptor_set_header_结构体.md#ae4931afed75f035e9dff4856ddee8609)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [dwWindowsVersion](../device_power_control_model_reference/P037_msosv2_descriptor_set_header_结构体.md#acf91f874e365a7f8ef60eaa19da517b4)
- [wTotalLength](../device_power_control_model_reference/P037_msosv2_descriptor_set_header_结构体.md#a3bab654cec13541096f08b43adb55f40)
- [msosv2_configuration_subset_header](../device_power_control_model_reference/P036_msosv2_configuration_subset_header_结构体.md)
- [wLength](../device_power_control_model_reference/P036_msosv2_configuration_subset_header_结构体.md#a7468f6428046553abf5e97172b52d477)
- [wDescriptorType](../device_power_control_model_reference/P036_msosv2_configuration_subset_header_结构体.md#ada03982dd6680a45d7cd2ba9e791c54e)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bConfigurationValue](../device_power_control_model_reference/P036_msosv2_configuration_subset_header_结构体.md#a044e9d3a0ec479564406f04d895e353c)
- [bReserved](../device_power_control_model_reference/P036_msosv2_configuration_subset_header_结构体.md#aa063ff78775c00edde1de6e274a2b817)
- [wTotalLength](../device_power_control_model_reference/P036_msosv2_configuration_subset_header_结构体.md#a044cf7d76fa93bfaa265bd5c24d8d413)
- [msosv2_function_subset_header](../device_power_control_model_reference/P038_msosv2_function_subset_header_结构体.md)
- [wLength](../device_power_control_model_reference/P038_msosv2_function_subset_header_结构体.md#a10e00ccb02a6e2c9c4c5f4d634414a0c)
- [wDescriptorType](../device_power_control_model_reference/P038_msosv2_function_subset_header_结构体.md#a4a93fdd2d9ea65b5b9097f921629c644)
- [bFirstInterface](../device_power_control_model_reference/P038_msosv2_function_subset_header_结构体.md#abf8bbff467411af8f259d2f16dc73649)
- [bReserved](../device_power_control_model_reference/P038_msosv2_function_subset_header_结构体.md#a07a64f2419014f41fa356fd85976985d)
- [wSubsetLength](../device_power_control_model_reference/P038_msosv2_function_subset_header_结构体.md#a7c3d3e7cd0577dc4ceab66615fefbe46)
- [msosv2_compatible_id](../device_power_control_model_reference/P035_msosv2_compatible_id_结构体.md)
- [wLength](../device_power_control_model_reference/P035_msosv2_compatible_id_结构体.md#ad2fabcbcfe86dd7f6c7e21607392ed9f)
- [wDescriptorType](../device_power_control_model_reference/P035_msosv2_compatible_id_结构体.md#adfb121211a3e2519cdbf3afa91cd48e3)
- [CompatibleID](../device_power_control_model_reference/P035_msosv2_compatible_id_结构体.md#a213f32b16fda92bc5526abee2d5922b5)
- [SubCompatibleID](../device_power_control_model_reference/P035_msosv2_compatible_id_结构体.md#affc8c55b00ddcc20841054ac8d8c6844)
- [msosv2_guids_property](../device_power_control_model_reference/P039_msosv2_guids_property_结构体.md)
- [wLength](../device_power_control_model_reference/P039_msosv2_guids_property_结构体.md#a500199bebfa7f8bf300be51310497a0c)
- [wDescriptorType](../device_power_control_model_reference/P039_msosv2_guids_property_结构体.md#acaa81e6bbaaec95922a80ef5a6000cd9)
- [wPropertyDataType](../device_power_control_model_reference/P039_msosv2_guids_property_结构体.md#aee143372e2bd13a32ae61e68ab429fbe)
- [wPropertyNameLength](../device_power_control_model_reference/P039_msosv2_guids_property_结构体.md#a815f24af18f726244a9ab7d9f67e1cab)
- [PropertyName](../device_power_control_model_reference/P039_msosv2_guids_property_结构体.md#ac447835ec1446a2e190228cab2b7dca8)
- [wPropertyDataLength](../device_power_control_model_reference/P039_msosv2_guids_property_结构体.md#a1740a7fb0134313dba90cf794f0218f1)
- [bPropertyData](../device_power_control_model_reference/P039_msosv2_guids_property_结构体.md#abf28542190ae7fececadacd3e8dba58a)
- [msosv2_resume_time](../device_power_control_model_reference/P041_msosv2_resume_time_结构体.md)
- [wLength](../device_power_control_model_reference/P041_msosv2_resume_time_结构体.md#a95a1ba0d9e5d0019dfeabfea0ddaf205)
- [wDescriptorType](../device_power_control_model_reference/P041_msosv2_resume_time_结构体.md#a22fc11df55af95324cfeb2459a544bd4)
- [bResumeRecoveryTime](../device_power_control_model_reference/P041_msosv2_resume_time_结构体.md#a33ff93b8c7d97dc9732158b2293cd377)
- [bResumeSignalingTime](../device_power_control_model_reference/P041_msosv2_resume_time_结构体.md#a1a08a4ec1b884a68ffc6b52a84e747aa)
- [msosv2_model_id](../device_power_control_model_reference/P040_msosv2_model_id_结构体.md)
- [wLength](../device_power_control_model_reference/P040_msosv2_model_id_结构体.md#a2355b2ab759e661462d61ffbdb7c29cd)
- [wDescriptorType](../device_power_control_model_reference/P040_msosv2_model_id_结构体.md#af03a88860ff6086b0cda956f2ccff824)
- [ModelID](../device_power_control_model_reference/P040_msosv2_model_id_结构体.md#ae87e515d83e0f979c993ef24d2486d08)
- [msosv2_ccgp_device](../device_power_control_model_reference/P034_msosv2_ccgp_device_结构体.md)
- [wLength](../device_power_control_model_reference/P034_msosv2_ccgp_device_结构体.md#a43cc94903315cb1a09418325630f936c)
- [wDescriptorType](../device_power_control_model_reference/P034_msosv2_ccgp_device_结构体.md#af3713e6a6185c8725d21fd5f1edbf84a)
- [msosv2_vendor_revision](../device_power_control_model_reference/P042_msosv2_vendor_revision_结构体.md)
- [wLength](../device_power_control_model_reference/P042_msosv2_vendor_revision_结构体.md#a4b29a145268e89c416f50cddc28f0ff4)
- [wDescriptorType](../device_power_control_model_reference/P042_msosv2_vendor_revision_结构体.md#a6ad0f9afb827947e4e2bfca339b70ceb)
- [VendorRevision](../device_power_control_model_reference/P042_msosv2_vendor_revision_结构体.md#aebed4cce3752a96a82fb25e3071a021c)
- [msosv2_ccgp_device::wLength](../device_power_control_model_reference/P034_msosv2_ccgp_device_结构体.md#a43cc94903315cb1a09418325630f936c)
- [msosv2_ccgp_device::wDescriptorType](../device_power_control_model_reference/P034_msosv2_ccgp_device_结构体.md#af3713e6a6185c8725d21fd5f1edbf84a)
- [msosv2_compatible_id::CompatibleID](../device_power_control_model_reference/P035_msosv2_compatible_id_结构体.md#a213f32b16fda92bc5526abee2d5922b5)
- [msosv2_compatible_id::wLength](../device_power_control_model_reference/P035_msosv2_compatible_id_结构体.md#ad2fabcbcfe86dd7f6c7e21607392ed9f)
- [msosv2_compatible_id::wDescriptorType](../device_power_control_model_reference/P035_msosv2_compatible_id_结构体.md#adfb121211a3e2519cdbf3afa91cd48e3)
- [msosv2_compatible_id::SubCompatibleID](../device_power_control_model_reference/P035_msosv2_compatible_id_结构体.md#affc8c55b00ddcc20841054ac8d8c6844)
- [msosv2_configuration_subset_header::wTotalLength](../device_power_control_model_reference/P036_msosv2_configuration_subset_header_结构体.md#a044cf7d76fa93bfaa265bd5c24d8d413)
- [msosv2_configuration_subset_header::bConfigurationValue](../device_power_control_model_reference/P036_msosv2_configuration_subset_header_结构体.md#a044e9d3a0ec479564406f04d895e353c)
- [msosv2_configuration_subset_header::wLength](../device_power_control_model_reference/P036_msosv2_configuration_subset_header_结构体.md#a7468f6428046553abf5e97172b52d477)
- [msosv2_configuration_subset_header::bReserved](../device_power_control_model_reference/P036_msosv2_configuration_subset_header_结构体.md#aa063ff78775c00edde1de6e274a2b817)
- [msosv2_configuration_subset_header::wDescriptorType](../device_power_control_model_reference/P036_msosv2_configuration_subset_header_结构体.md#ada03982dd6680a45d7cd2ba9e791c54e)
- [msosv2_descriptor_set_header::wTotalLength](../device_power_control_model_reference/P037_msosv2_descriptor_set_header_结构体.md#a3bab654cec13541096f08b43adb55f40)
- [msosv2_descriptor_set_header::wLength](../device_power_control_model_reference/P037_msosv2_descriptor_set_header_结构体.md#a4281eeb2128138b597fb53577ec8d57f)
- [msosv2_descriptor_set_header::dwWindowsVersion](../device_power_control_model_reference/P037_msosv2_descriptor_set_header_结构体.md#acf91f874e365a7f8ef60eaa19da517b4)
- [msosv2_descriptor_set_header::wDescriptorType](../device_power_control_model_reference/P037_msosv2_descriptor_set_header_结构体.md#ae4931afed75f035e9dff4856ddee8609)
- [msosv2_function_subset_header::bReserved](../device_power_control_model_reference/P038_msosv2_function_subset_header_结构体.md#a07a64f2419014f41fa356fd85976985d)
- [msosv2_function_subset_header::wLength](../device_power_control_model_reference/P038_msosv2_function_subset_header_结构体.md#a10e00ccb02a6e2c9c4c5f4d634414a0c)
- [msosv2_function_subset_header::wDescriptorType](../device_power_control_model_reference/P038_msosv2_function_subset_header_结构体.md#a4a93fdd2d9ea65b5b9097f921629c644)
- [msosv2_function_subset_header::wSubsetLength](../device_power_control_model_reference/P038_msosv2_function_subset_header_结构体.md#a7c3d3e7cd0577dc4ceab66615fefbe46)
- [msosv2_function_subset_header::bFirstInterface](../device_power_control_model_reference/P038_msosv2_function_subset_header_结构体.md#abf8bbff467411af8f259d2f16dc73649)
- [msosv2_guids_property::wPropertyDataLength](../device_power_control_model_reference/P039_msosv2_guids_property_结构体.md#a1740a7fb0134313dba90cf794f0218f1)
- [msosv2_guids_property::wLength](../device_power_control_model_reference/P039_msosv2_guids_property_结构体.md#a500199bebfa7f8bf300be51310497a0c)
- [msosv2_guids_property::wPropertyNameLength](../device_power_control_model_reference/P039_msosv2_guids_property_结构体.md#a815f24af18f726244a9ab7d9f67e1cab)
- [msosv2_guids_property::bPropertyData](../device_power_control_model_reference/P039_msosv2_guids_property_结构体.md#abf28542190ae7fececadacd3e8dba58a)
- [msosv2_guids_property::PropertyName](../device_power_control_model_reference/P039_msosv2_guids_property_结构体.md#ac447835ec1446a2e190228cab2b7dca8)
- [msosv2_guids_property::wDescriptorType](../device_power_control_model_reference/P039_msosv2_guids_property_结构体.md#acaa81e6bbaaec95922a80ef5a6000cd9)
- [msosv2_guids_property::wPropertyDataType](../device_power_control_model_reference/P039_msosv2_guids_property_结构体.md#aee143372e2bd13a32ae61e68ab429fbe)
- [msosv2_model_id::wLength](../device_power_control_model_reference/P040_msosv2_model_id_结构体.md#a2355b2ab759e661462d61ffbdb7c29cd)
- [msosv2_model_id::ModelID](../device_power_control_model_reference/P040_msosv2_model_id_结构体.md#ae87e515d83e0f979c993ef24d2486d08)
- [msosv2_model_id::wDescriptorType](../device_power_control_model_reference/P040_msosv2_model_id_结构体.md#af03a88860ff6086b0cda956f2ccff824)
- [msosv2_resume_time::bResumeSignalingTime](../device_power_control_model_reference/P041_msosv2_resume_time_结构体.md#a1a08a4ec1b884a68ffc6b52a84e747aa)
- [msosv2_resume_time::wDescriptorType](../device_power_control_model_reference/P041_msosv2_resume_time_结构体.md#a22fc11df55af95324cfeb2459a544bd4)
- [msosv2_resume_time::bResumeRecoveryTime](../device_power_control_model_reference/P041_msosv2_resume_time_结构体.md#a33ff93b8c7d97dc9732158b2293cd377)
- [msosv2_resume_time::wLength](../device_power_control_model_reference/P041_msosv2_resume_time_结构体.md#a95a1ba0d9e5d0019dfeabfea0ddaf205)
- [msosv2_vendor_revision::wLength](../device_power_control_model_reference/P042_msosv2_vendor_revision_结构体.md#a4b29a145268e89c416f50cddc28f0ff4)
- [msosv2_vendor_revision::wDescriptorType](../device_power_control_model_reference/P042_msosv2_vendor_revision_结构体.md#a6ad0f9afb827947e4e2bfca339b70ceb)
- [msosv2_vendor_revision::VendorRevision](../device_power_control_model_reference/P042_msosv2_vendor_revision_结构体.md#aebed4cce3752a96a82fb25e3071a021c)

---

[上一章](P007_max32664c.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P009_net_mgmt.h_源码浏览.md)

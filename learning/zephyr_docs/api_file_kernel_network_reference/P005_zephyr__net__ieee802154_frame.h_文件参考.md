---
id: learning.zephyr-docs.api-file-kernel-network-reference.page-5
title: zephyr__net__ieee802154_frame.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_zephyr\_\_net\_\_ieee802154\_frame.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

IEEE 802.15.4 MAC帧（Frame）的相关函数。

<a id="details"></a>

```c
#include <zephyr/kernel.h>
#include <zephyr/net/ieee802154.h>
#include <zephyr/net/net_pkt.h>
#include <zephyr/toolchain.h>
```

查看此文件的源码。

IEEE 802.15.4 媒体访问控制（MAC）帧相关函数。应用程序不应包含此文件。

注意（Note）：本文件对标准的所有引用均指 IEEE 802.15.4-2020。本文件中直接表示 IEEE 802.15.4 帧组成部分的所有结构体和属性（例如个域网标识符（PAN ID）、扩展地址和短地址）均采用小端字节序（Little Endian），参见第 4 节，尤其是第 4.3 节。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 5.1\_数据结构（Data Structures）

<a id="r_ieee802154_5Ffcf_5Fseq"></a>

```c
struct ieee802154_fcf_seq
```

相关声明：[ieee802154_fcf_seq](../network_core_model_reference/P016_ieee802154_fcf_seq_结构体.md)。

MAC头部（MHR）中的帧控制（Frame Control）字段与序列号。

<a id="r_ieee802154_5Faddress"></a>

```c
struct ieee802154_address
```

相关声明：[ieee802154_address](../network_core_model_reference/P001_ieee802154_address_结构体.md)。

MAC寻址字段（Addressing Fields）中的短地址值或扩展地址值。

<a id="r_ieee802154_5Faddress_5Ffield_5Fcomp"></a>

```c
struct ieee802154_address_field_comp
```

相关声明：[ieee802154_address_field_comp](../network_core_model_reference/P003_ieee802154_address_field_comp_结构体.md)。

PAN ID压缩（PAN ID Compression）省略PAN ID时的目的地址或源地址字段。

<a id="r_ieee802154_5Faddress_5Ffield_5Fplain"></a>

```c
struct ieee802154_address_field_plain
```

相关声明：[ieee802154_address_field_plain](../network_core_model_reference/P004_ieee802154_address_field_plain_结构体.md)。

包含PAN ID和地址的目的地址或源地址字段（Destination / Source Address）。

<a id="r_ieee802154_5Faddress_5Ffield"></a>

```c
struct ieee802154_address_field
```

相关声明：[ieee802154_address_field](../network_core_model_reference/P002_ieee802154_address_field_结构体.md)。

以压缩或原始形式表示的目的地址或源地址字段（Destination / Source Address）。

<a id="r_ieee802154_5Fsecurity_5Fcontrol_5Ffield"></a>

```c
struct ieee802154_security_control_field
```

相关声明：[ieee802154_security_control_field](../network_core_model_reference/P043_ieee802154_security_control_field_结构体.md)。

安全控制（Security Control）字段，即辅助安全头的第一个八位组。

<a id="r_ieee802154_5Fkey_5Fidentifier_5Ffield"></a>

```c
struct ieee802154_key_identifier_field
```

相关声明：[ieee802154_key_identifier_field](../network_core_model_reference/P033_ieee802154_key_identifier_field_结构体.md)。

辅助安全头（Auxiliary Security Header）的密钥标识符字段。

<a id="r_ieee802154_5Faux_5Fsecurity_5Fhdr"></a>

```c
struct ieee802154_aux_security_hdr
```

相关声明：[ieee802154_aux_security_hdr](../network_core_model_reference/P006_ieee802154_aux_security_hdr_结构体.md)。

启用安全机制时位于寻址字段之后的辅助安全头（Auxiliary Security Header，ASH）。

<a id="r_ieee802154_5Fmhr"></a>

```c
struct ieee802154_mhr
```

相关声明：[ieee802154_mhr](../network_core_model_reference/P034_ieee802154_mhr_结构体.md)。

MAC头部（MHR）及辅助安全头指针的已解析视图。

<a id="r_ieee802154_5Fgts_5Fdir"></a>

```c
struct ieee802154_gts_dir
```

相关声明：[ieee802154_gts_dir](../network_core_model_reference/P020_ieee802154_gts_dir_结构体.md)。

信标载荷中的保证时隙方向（GTS Direction）字段。

<a id="r_ieee802154_5Fgts"></a>

```c
struct ieee802154_gts
```

相关声明：[ieee802154_gts](../network_core_model_reference/P019_ieee802154_gts_结构体.md)。

保证时隙（GTS）列表字段中的一个GTS描述符。

<a id="r_ieee802154_5Fgts_5Fspec"></a>

```c
struct ieee802154_gts_spec
```

相关声明：[ieee802154_gts_spec](../network_core_model_reference/P022_ieee802154_gts_spec_结构体.md)。

信标载荷中的保证时隙规范（GTS Specification）字段。

<a id="r_ieee802154_5Fpas_5Fspec"></a>

```c
struct ieee802154_pas_spec
```

相关声明：[ieee802154_pas_spec](../network_core_model_reference/P038_ieee802154_pas_spec_结构体.md)。

信标载荷中的待处理地址规范（Pending Address Specification）字段。

<a id="r_ieee802154_5Fbeacon_5Fsf"></a>

```c
struct ieee802154_beacon_sf
```

相关声明：[ieee802154_beacon_sf](../network_core_model_reference/P008_ieee802154_beacon_sf_结构体.md)。

信标载荷中的超帧规范（Superframe Specification）字段。

<a id="r_ieee802154_5Fbeacon"></a>

```c
struct ieee802154_beacon
```

相关声明：[ieee802154_beacon](../network_core_model_reference/P007_ieee802154_beacon_结构体.md)。

信标载荷（Beacon Payload）的固定部分，即超帧规范和GTS规范。

<a id="r_ieee802154_5Fcmd_5Fassoc_5Freq"></a>

```c
struct ieee802154_cmd_assoc_req
```

相关声明：[ieee802154_cmd_assoc_req](../network_core_model_reference/P009_ieee802154_cmd_assoc_req_结构体.md)。

关联请求（Association Request）命令的载荷，即能力信息字段。

<a id="r_ieee802154_5Fcmd_5Fassoc_5Fres"></a>

```c
struct ieee802154_cmd_assoc_res
```

相关声明：[ieee802154_cmd_assoc_res](../network_core_model_reference/P010_ieee802154_cmd_assoc_res_结构体.md)。

关联响应（Association Response）命令的载荷。

<a id="r_ieee802154_5Fcmd_5Fdisassoc_5Fnote"></a>

```c
struct ieee802154_cmd_disassoc_note
```

相关声明：[ieee802154_cmd_disassoc_note](../network_core_model_reference/P012_ieee802154_cmd_disassoc_note_结构体.md)。

解除关联通知（Disassociation Notification）命令的载荷。

<a id="r_ieee802154_5Fcmd_5Fcoord_5Frealign"></a>

```c
struct ieee802154_cmd_coord_realign
```

相关声明：[ieee802154_cmd_coord_realign](../network_core_model_reference/P011_ieee802154_cmd_coord_realign_结构体.md)。

协调器重对齐（Coordinator Realignment）命令的载荷。

<a id="r_ieee802154_5Fgts_5Frequest"></a>

```c
struct ieee802154_gts_request
```

相关声明：[ieee802154_gts_request](../network_core_model_reference/P021_ieee802154_gts_request_结构体.md)。

保证时隙请求（GTS Request）命令的载荷。

<a id="r_ieee802154_5Fcommand"></a>

```c
struct ieee802154_command
```

相关声明：[ieee802154_command](../network_core_model_reference/P013_ieee802154_command_结构体.md)。

已解析的MAC命令帧（Command Frame）载荷。

<a id="r_ieee802154_5Fmpdu"></a>

```c
struct ieee802154_mpdu
```

相关声明：[ieee802154_mpdu](../network_core_model_reference/P035_ieee802154_mpdu_结构体.md)。

已解析的MAC服务数据单元（MSDU），包含MHR指针及载荷视图。

<a id="r_ieee802154_5Fframe_5Fparams"></a>

```c
struct ieee802154_frame_params
```

相关声明：[ieee802154_frame_params](../network_core_model_reference/P018_ieee802154_frame_params_结构体.md)。

构造MAC帧的参数，包括地址和个人区域网（PAN）标识。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 5.2\_宏定义（Macros）

<a id="r_a3f791448bce9ad9297401f7725835eb4"></a>

```c
#define IEEE802154_ACK_PKT_LENGTH 3
```

相关声明：[IEEE802154_ACK_PKT_LENGTH](#a3f791448bce9ad9297401f7725835eb4)。

立即确认（Immediate Acknowledgment，Imm-Ack）帧的 MAC 协议数据单元（MPDU）长度，单位为八位组（Octet）。

<a id="r_aa446d872aea406d4946c9c0e2f286c2e"></a>

```c
#define IEEE802154_MIN_LENGTH IEEE802154_ACK_PKT_LENGTH
```

相关声明：[IEEE802154_MIN_LENGTH](#aa446d872aea406d4946c9c0e2f286c2e)、[IEEE802154_ACK_PKT_LENGTH](#a3f791448bce9ad9297401f7725835eb4)。

此处支持的最小 MAC 帧 NMPDU 长度（与 `IEEE802154_ACK_PKT_LENGTH` 相同）。

<a id="r_a6ef8827cf387edee15d3252dd8af9a41"></a>

```c
#define IEEE802154_FCF_SEQ_LENGTH 3
```

相关声明：[IEEE802154_FCF_SEQ_LENGTH](#a6ef8827cf387edee15d3252dd8af9a41)。

帧控制（Frame Control）字段与序列号（Sequence Number）字段的总长度，单位为八位组（Octet）。

<a id="r_a78fb36a5e46dfa669d199eb630a3adda"></a>

```c
#define IEEE802154_PAN_ID_LENGTH 2
```

相关声明：[IEEE802154_PAN_ID_LENGTH](#a78fb36a5e46dfa669d199eb630a3adda)。

MAC 寻址字段中个域网标识符（PAN Identifier）的长度，单位为八位组（Octet）。

<a id="r_a953435b3c17981ebe7e3c8d27eb41f3e"></a>

```c
#define IEEE802154_BEACON_MIN_SIZE 4
```

相关声明：[IEEE802154_BEACON_MIN_SIZE](#a953435b3c17981ebe7e3c8d27eb41f3e)。

信标载荷（Beacon Payload）字段的最小长度，单位为八位组（Octet）。

<a id="r_a30b5cca2bcf74cce616ae8e901fc1c5b"></a>

```c
#define IEEE802154_BEACON_SF_SIZE 2
```

相关声明：[IEEE802154_BEACON_SF_SIZE](#a30b5cca2bcf74cce616ae8e901fc1c5b)。

超帧规范（Superframe Specification）字段的长度，单位为八位组（Octet）。

<a id="r_a3745048f0cf83f38e060978d6ffd1ccc"></a>

```c
#define IEEE802154_BEACON_GTS_SPEC_SIZE 1
```

相关声明：[IEEE802154_BEACON_GTS_SPEC_SIZE](#a3745048f0cf83f38e060978d6ffd1ccc)。

保障时隙规范（GTS Specification）字段的长度，单位为八位组（Octet）。

<a id="r_a04623eec2e0971b164b145ae365e7a8d"></a>

```c
#define IEEE802154_BEACON_GTS_IF_MIN_SIZE IEEE802154_BEACON_GTS_SPEC_SIZE
```

相关声明：[IEEE802154_BEACON_GTS_IF_MIN_SIZE](#a04623eec2e0971b164b145ae365e7a8d)、[IEEE802154_BEACON_GTS_SPEC_SIZE](#a3745048f0cf83f38e060978d6ffd1ccc)。

仅存在 GTS 规范（GTS Specification）时，保障时隙（GTS）字段的最小长度，单位为八位组（Octet）。

<a id="r_a83d3c27393203aba941af700eb82c739"></a>

```c
#define IEEE802154_BEACON_PAS_SPEC_SIZE 1
```

相关声明：[IEEE802154_BEACON_PAS_SPEC_SIZE](#a83d3c27393203aba941af700eb82c739)。

待处理地址规范（Pending Address Specification）字段的长度，单位为八位组（Octet）。

<a id="r_a60daa438820182fe4f9d8ad22e93c935"></a>

```c
#define IEEE802154_BEACON_PAS_IF_MIN_SIZE IEEE802154_BEACON_PAS_SPEC_SIZE
```

相关声明：[IEEE802154_BEACON_PAS_IF_MIN_SIZE](#a60daa438820182fe4f9d8ad22e93c935)、[IEEE802154_BEACON_PAS_SPEC_SIZE](#a83d3c27393203aba941af700eb82c739)。

仅存在规范字段时，待处理地址（Pending Address）字段的最小长度，单位为八位组（Octet）。

<a id="r_a5f7adf99bac9e2a46f3b013d960ff4b8"></a>

```c
#define IEEE802154_BEACON_GTS_DIR_SIZE 1
```

相关声明：[IEEE802154_BEACON_GTS_DIR_SIZE](#a5f7adf99bac9e2a46f3b013d960ff4b8)。

GTS 方向（GTS Direction）字段的长度，单位为八位组（Octet）。

<a id="r_acd065b4e0ce7a30a950d7a1ce1841d02"></a>

```c
#define IEEE802154_BEACON_GTS_SIZE 3
```

相关声明：[IEEE802154_BEACON_GTS_SIZE](#acd065b4e0ce7a30a950d7a1ce1841d02)。

GTS 列表（GTS List）字段中一个 GTS 描述符（Descriptor）的长度，单位为八位组（Octet）。

<a id="r_a3d3ff94ce6204f4b7abd972a53f27f26"></a>

```c
#define IEEE802154_BEACON_GTS_RX 1
```

相关声明：[IEEE802154_BEACON_GTS_RX](#a3d3ff94ce6204f4b7abd972a53f27f26)。

仅接收保障时隙（Receive-only GTS）的描述符方向值。

<a id="r_a77527e2b10568aefd0152d6b08aa33a9"></a>

```c
#define IEEE802154_BEACON_GTS_TX 0
```

相关声明：[IEEE802154_BEACON_GTS_TX](#a77527e2b10568aefd0152d6b08aa33a9)。

仅发送保障时隙（Transmit-only GTS）的描述符方向值。

<a id="r_a9fe069f17d6dc89ad8085056bd7f0956"></a>

```c
#define IEEE802154_SECURITY_LEVEL_ENC IEEE802154_SECURITY_LEVEL_RESERVED
```

相关声明：[IEEE802154_SECURITY_LEVEL_ENC](#a9fe069f17d6dc89ad8085056bd7f0956)、[IEEE802154_SECURITY_LEVEL_RESERVED](#aaf5ffabf140bf36c9076662e4b46e4a2a2155c782cf4074f240bcb087aecc8f06)。

将安全级别（Security Level）与此值比较，以识别加密模式（Encryption Mode）。

<a id="r_a3b252760d00618bf006c4939327a3cc2"></a>

```c
#define IEEE802154_AUTH_TAG_LENGTH_32 4
```

相关声明：[IEEE802154_AUTH_TAG_LENGTH_32](#a3b252760d00618bf006c4939327a3cc2)。

MIC-32 模式的认证标签（Authentication Tag）长度，单位为八位组（Octet）。

<a id="r_a5ce2b6b1b0aa9f166aac68fbf5d522e4"></a>

```c
#define IEEE802154_AUTH_TAG_LENGTH_64 8
```

相关声明：[IEEE802154_AUTH_TAG_LENGTH_64](#a5ce2b6b1b0aa9f166aac68fbf5d522e4)。

MIC-64 模式的认证标签（Authentication Tag）长度，单位为八位组（Octet）。

<a id="r_a041a677ab85038ad00ce3ff00132aaa7"></a>

```c
#define IEEE802154_AUTH_TAG_LENGTH_128 16
```

相关声明：[IEEE802154_AUTH_TAG_LENGTH_128](#a041a677ab85038ad00ce3ff00132aaa7)。

MIC-128 模式的认证标签（Authentication Tag）长度，单位为八位组（Octet）。

<a id="r_a4b7a12e735b0c3f7896480ec62818dc4"></a>

```c
#define IEEE802154_KEY_ID_FIELD_INDEX_LENGTH 1
```

相关声明：[IEEE802154_KEY_ID_FIELD_INDEX_LENGTH](#a4b7a12e735b0c3f7896480ec62818dc4)。

密钥标识符模式 1（Key Identifier Mode 1）中密钥标识符字段的长度，单位为八位组（Octet）。

<a id="r_a59da421480bdd7a4e0e00fd091d8a9ec"></a>

```c
#define IEEE802154_KEY_ID_FIELD_SRC_4_INDEX_LENGTH 5
```

相关声明：[IEEE802154_KEY_ID_FIELD_SRC_4_INDEX_LENGTH](#a59da421480bdd7a4e0e00fd091d8a9ec)。

密钥标识符模式 2（Key Identifier Mode 2）中密钥标识符字段的长度，单位为八位组（Octet）。

<a id="r_a30b9143792a736afc9a1e051cb07eeb5"></a>

```c
#define IEEE802154_KEY_ID_FIELD_SRC_8_INDEX_LENGTH 9
```

相关声明：[IEEE802154_KEY_ID_FIELD_SRC_8_INDEX_LENGTH](#a30b9143792a736afc9a1e051cb07eeb5)。

密钥标识符模式 3（Key Identifier Mode 3）中密钥标识符字段的长度，单位为八位组（Octet）。

<a id="r_a181095776e2bbe690d8b8d694d00cb5b"></a>

```c
#define IEEE802154_KEY_MAX_LEN 16
```

相关声明：[IEEE802154_KEY_MAX_LEN](#a181095776e2bbe690d8b8d694d00cb5b)。

本 API 中 MAC 安全操作的最大密钥（Key）长度，单位为八位组（Octet）。

<a id="r_ac05f9f47c969440174e2fb801fc08976"></a>

```c
#define IEEE802154_SECURITY_CF_LENGTH 1
```

相关声明：[IEEE802154_SECURITY_CF_LENGTH](#ac05f9f47c969440174e2fb801fc08976)。

安全控制（Security Control）字段的长度，单位为八位组（Octet）。

<a id="r_a065430381b20783ed8ef9a04708b3e54"></a>

```c
#define IEEE802154_SECURITY_FRAME_COUNTER_LENGTH 4
```

相关声明：[IEEE802154_SECURITY_FRAME_COUNTER_LENGTH](#a065430381b20783ed8ef9a04708b3e54)。

辅助安全头部（Auxiliary Security Header）中帧计数器（Frame Counter）字段的长度，单位为八位组（Octet）。

<a id="r_a848b45622662cb7d0f2653ebaab09bd9"></a>

```c
#define IEEE802154_CMD_ASSOC_REQ_LENGTH 1
```

相关声明：[IEEE802154_CMD_ASSOC_REQ_LENGTH](#a848b45622662cb7d0f2653ebaab09bd9)。

关联请求（Association Request）命令载荷（能力信息（Capability Information））的长度，单位为八位组（Octet）。

<a id="r_a950a98517a7c0068bcdc6d099d5e2997"></a>

```c
#define IEEE802154_CMD_ASSOC_RES_LENGTH 3
```

相关声明：[IEEE802154_CMD_ASSOC_RES_LENGTH](#a950a98517a7c0068bcdc6d099d5e2997)。

关联响应（Association Response）命令载荷的长度，单位为八位组（Octet）。

<a id="r_af141f1fa16d118eb2c2f786813745e6f"></a>

```c
#define IEEE802154_CMD_DISASSOC_NOTE_LENGTH 1
```

相关声明：[IEEE802154_CMD_DISASSOC_NOTE_LENGTH](#af141f1fa16d118eb2c2f786813745e6f)。

解除关联通知（Disassociation Notification）命令载荷的长度，单位为八位组（Octet）。

<a id="r_a3486e79bb2efb3dec6124ff4fa092b21"></a>

```c
#define IEEE802154_CMD_COORD_REALIGN_LENGTH 3
```

相关声明：[IEEE802154_CMD_COORD_REALIGN_LENGTH](#a3486e79bb2efb3dec6124ff4fa092b21)。

此处涵盖的协调器重对齐（Coordinator Realignment）命令载荷的最小长度，单位为八位组（Octet）。

<a id="r_a5fd880c4112671a1d17c31c84d41eb28"></a>

```c
#define IEEE802154_GTS_REQUEST_LENGTH 1
```

相关声明：[IEEE802154_GTS_REQUEST_LENGTH](#a5fd880c4112671a1d17c31c84d41eb28)。

GTS 请求（GTS Request）命令载荷的长度，单位为八位组（Octet）。

<a id="r_a9d7451a2c78857e0d9650c51e4f0a06a"></a>

```c
#define IEEE802154_CMD_CFI_LENGTH 1
```

相关声明：[IEEE802154_CMD_CFI_LENGTH](#a9d7451a2c78857e0d9650c51e4f0a06a)。

命令帧标识符（Command Frame Identifier）字段的长度，单位为八位组（Octet）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 5.3\_枚举（Enumerations）

<a id="r_a16702b800d3e4a51df6cb6f909ff79fd"></a>

```c
enum ieee802154_frame_type { IEEE802154_FRAME_TYPE_BEACON = 0x0 , IEEE802154_FRAME_TYPE_DATA = 0x1 , IEEE802154_FRAME_TYPE_ACK = 0x2 , IEEE802154_FRAME_TYPE_MAC_COMMAND = 0x3 , IEEE802154_FRAME_TYPE_RESERVED = 0x4 , IEEE802154_FRAME_TYPE_MULTIPURPOSE = 0x5 , IEEE802154_FRAME_TYPE_FRAK = 0x6 , IEEE802154_FRAME_TYPE_EXTENDED = 0x7 }
```

相关声明：[ieee802154_frame_type](#a16702b800d3e4a51df6cb6f909ff79fd)、[IEEE802154_FRAME_TYPE_BEACON](#a16702b800d3e4a51df6cb6f909ff79fda6253c6948e0ecbc79878bd1fd73473ec)、[IEEE802154_FRAME_TYPE_DATA](#a16702b800d3e4a51df6cb6f909ff79fda59490f8a40d1c65c365b3370ccabd3d8)、[IEEE802154_FRAME_TYPE_ACK](#a16702b800d3e4a51df6cb6f909ff79fdacd5ec548c6199b61912ed8a15df3b486)、[IEEE802154_FRAME_TYPE_MAC_COMMAND](#a16702b800d3e4a51df6cb6f909ff79fda69235bb8211a5a4a3c4fde6379d28644)、[IEEE802154_FRAME_TYPE_RESERVED](#a16702b800d3e4a51df6cb6f909ff79fdaf14e1c3c75c77dcfaf54d2d637b9b4ae)、[IEEE802154_FRAME_TYPE_MULTIPURPOSE](#a16702b800d3e4a51df6cb6f909ff79fda953e79789829eb3e220bccb94f21316f)、[IEEE802154_FRAME_TYPE_FRAK](#a16702b800d3e4a51df6cb6f909ff79fdaaabec4197346f0d36903217c1f68b90f)、[IEEE802154_FRAME_TYPE_EXTENDED](#a16702b800d3e4a51df6cb6f909ff79fdacb7f98a3d76846d411bc698572a5eeb5)。

帧控制（Frame Control）字段中帧类型（Frame Type）子字段的值。

<a id="r_a49f3241733da0a6dd0003d7bcaf55965"></a>

```c
enum ieee802154_addressing_mode { IEEE802154_ADDR_MODE_NONE = 0x0 , IEEE802154_ADDR_MODE_RESERVED = 0x1 , IEEE802154_ADDR_MODE_SHORT = 0x2 , IEEE802154_ADDR_MODE_EXTENDED = 0x3 }
```

相关声明：[ieee802154_addressing_mode](#a49f3241733da0a6dd0003d7bcaf55965)、[IEEE802154_ADDR_MODE_NONE](#a49f3241733da0a6dd0003d7bcaf55965a50e45c02f42ef667e1216cfc1024860f)、[IEEE802154_ADDR_MODE_RESERVED](#a49f3241733da0a6dd0003d7bcaf55965a6f5f3599146d548b541dd22fa1f6322c)、[IEEE802154_ADDR_MODE_SHORT](#a49f3241733da0a6dd0003d7bcaf55965aa51f0be0ff88addcd167b03051e2dc21)、[IEEE802154_ADDR_MODE_EXTENDED](#a49f3241733da0a6dd0003d7bcaf55965a27c38f60597d1b202cbb0e6c8cad27fd)。

目的地址与源地址寻址模式（Destination and Source Addressing Mode）子字段的值。

<a id="r_aa6a4b34e9722f5ccd06b65cf64efe053"></a>

```c
enum ieee802154_version { IEEE802154_VERSION_802154_2003 = 0x0 , IEEE802154_VERSION_802154_2006 = 0x1 , IEEE802154_VERSION_802154 = 0x2 , IEEE802154_VERSION_RESERVED = 0x3 }
```

相关声明：[ieee802154_version](#aa6a4b34e9722f5ccd06b65cf64efe053)、[IEEE802154_VERSION_802154_2003](#aa6a4b34e9722f5ccd06b65cf64efe053aad3af323ce4f598be0256ec9c19dcf36)、[IEEE802154_VERSION_802154_2006](#aa6a4b34e9722f5ccd06b65cf64efe053a3b2b709ecd3a2a1a4b997baf26c40bbc)、[IEEE802154_VERSION_802154](#aa6a4b34e9722f5ccd06b65cf64efe053aa2a088916733a4de4d009caaea734ca2)、[IEEE802154_VERSION_RESERVED](#aa6a4b34e9722f5ccd06b65cf64efe053a8112ae7940d211afe7a5a1a79071ad57)。

帧版本（Frame Version）子字段的值。

<a id="r_aaf5ffabf140bf36c9076662e4b46e4a2"></a>

```c
enum ieee802154_security_level { IEEE802154_SECURITY_LEVEL_NONE = 0x0 , IEEE802154_SECURITY_LEVEL_MIC_32 = 0x1 , IEEE802154_SECURITY_LEVEL_MIC_64 = 0x2 , IEEE802154_SECURITY_LEVEL_MIC_128 = 0x3 , IEEE802154_SECURITY_LEVEL_RESERVED = 0x4 , IEEE802154_SECURITY_LEVEL_ENC_MIC_32 = 0x5 , IEEE802154_SECURITY_LEVEL_ENC_MIC_64 = 0x6 , IEEE802154_SECURITY_LEVEL_ENC_MIC_128 = 0x7 }
```

相关声明：[ieee802154_security_level](#aaf5ffabf140bf36c9076662e4b46e4a2)、[IEEE802154_SECURITY_LEVEL_NONE](#aaf5ffabf140bf36c9076662e4b46e4a2af5bff347e35ac0af5c86b65ef231df47)、[IEEE802154_SECURITY_LEVEL_MIC_32](#aaf5ffabf140bf36c9076662e4b46e4a2a2b8b7e0d195c7fb33e3578b86bda99d7)、[IEEE802154_SECURITY_LEVEL_MIC_64](#aaf5ffabf140bf36c9076662e4b46e4a2abe9a01bb053e5809e0f110cb0709d001)、[IEEE802154_SECURITY_LEVEL_MIC_128](#aaf5ffabf140bf36c9076662e4b46e4a2a60e7720ffc14a08b0f4c90b567ce57bd)、[IEEE802154_SECURITY_LEVEL_RESERVED](#aaf5ffabf140bf36c9076662e4b46e4a2a2155c782cf4074f240bcb087aecc8f06)、[IEEE802154_SECURITY_LEVEL_ENC_MIC_32](#aaf5ffabf140bf36c9076662e4b46e4a2a95e1e7954023a5cd3c35aaf6596b0821)、[IEEE802154_SECURITY_LEVEL_ENC_MIC_64](#aaf5ffabf140bf36c9076662e4b46e4a2a649d558004918cacb4c9ec32d247c934)、[IEEE802154_SECURITY_LEVEL_ENC_MIC_128](#aaf5ffabf140bf36c9076662e4b46e4a2abaa5076f0f373c3f2e415a8f28a6e0ee)。

安全控制（Security Control）字段中安全级别（Security Level）子字段的值。

<a id="r_ac5819ed25fa7b56756e8e7962f579ec7"></a>

```c
enum ieee802154_key_id_mode { IEEE802154_KEY_ID_MODE_IMPLICIT = 0x0 , IEEE802154_KEY_ID_MODE_INDEX = 0x1 , IEEE802154_KEY_ID_MODE_SRC_4_INDEX = 0x2 , IEEE802154_KEY_ID_MODE_SRC_8_INDEX = 0x3 }
```

相关声明：[ieee802154_key_id_mode](#ac5819ed25fa7b56756e8e7962f579ec7)、[IEEE802154_KEY_ID_MODE_IMPLICIT](#ac5819ed25fa7b56756e8e7962f579ec7a2519ea53b9adf534707e7ce4401966f6)、[IEEE802154_KEY_ID_MODE_INDEX](#ac5819ed25fa7b56756e8e7962f579ec7a918058e16c48ecee20a8ce3968138c04)、[IEEE802154_KEY_ID_MODE_SRC_4_INDEX](#ac5819ed25fa7b56756e8e7962f579ec7ae351b9dc1ba1e546a706c861b4dfd841)、[IEEE802154_KEY_ID_MODE_SRC_8_INDEX](#ac5819ed25fa7b56756e8e7962f579ec7a0c363713ca56c27961d5198a5ee7078f)。

密钥标识符模式（Key Identifier Mode）子字段的值。

<a id="r_aa2c9cb8ba5b7c397c695a9a591649b91"></a>

```c
enum ieee802154_association_status_field { IEEE802154_ASF_SUCCESSFUL = 0x00 , IEEE802154_ASF_PAN_AT_CAPACITY = 0x01 , IEEE802154_ASF_PAN_ACCESS_DENIED = 0x02 , IEEE802154_ASF_RESERVED = 0x03 , IEEE802154_ASF_RESERVED_PRIMITIVES = 0x80 }
```

相关声明：[ieee802154_association_status_field](#aa2c9cb8ba5b7c397c695a9a591649b91)、[IEEE802154_ASF_SUCCESSFUL](#aa2c9cb8ba5b7c397c695a9a591649b91a280571e677e992f5220f56818e52ccf4)、[IEEE802154_ASF_PAN_AT_CAPACITY](#aa2c9cb8ba5b7c397c695a9a591649b91a571c5b2f63cedf01857ce31ba1125517)、[IEEE802154_ASF_PAN_ACCESS_DENIED](#aa2c9cb8ba5b7c397c695a9a591649b91a1cedbaa8a44fdb79041e6b5ad8af6031)、[IEEE802154_ASF_RESERVED](#aa2c9cb8ba5b7c397c695a9a591649b91a3a72c63164f925e7fe6d12d9cf572d81)、[IEEE802154_ASF_RESERVED_PRIMITIVES](#aa2c9cb8ba5b7c397c695a9a591649b91a15eb8c84a04a1642e7395a872eb5db59)。

关联响应（Association Response）命令中的关联状态（Association Status）值。

<a id="r_a2ab06c343e03a4d6e28073780eb47648"></a>

```c
enum ieee802154_disassociation_reason_field { IEEE802154_DRF_RESERVED_1 = 0x00 , IEEE802154_DRF_COORDINATOR_WISH = 0x01 , IEEE802154_DRF_DEVICE_WISH = 0x02 , IEEE802154_DRF_RESERVED_2 = 0x03 , IEEE802154_DRF_RESERVED_PRIMITIVES = 0x80 }
```

相关声明：[ieee802154_disassociation_reason_field](#a2ab06c343e03a4d6e28073780eb47648)、[IEEE802154_DRF_RESERVED_1](#a2ab06c343e03a4d6e28073780eb47648aec815962bcc4fe41d8a2223bc7b7e3c7)、[IEEE802154_DRF_COORDINATOR_WISH](#a2ab06c343e03a4d6e28073780eb47648a8b04f0bae8a62282a8a7821a4db949cb)、[IEEE802154_DRF_DEVICE_WISH](#a2ab06c343e03a4d6e28073780eb47648a3feadbd533ba9b31977e2fa7537fa8c1)、[IEEE802154_DRF_RESERVED_2](#a2ab06c343e03a4d6e28073780eb47648ae09de01a9f7b2a7eba0ee0173765e1ef)、[IEEE802154_DRF_RESERVED_PRIMITIVES](#a2ab06c343e03a4d6e28073780eb47648a2d69c0e06015471da07bce9314a900c7)。

解除关联通知（Disassociation Notification）命令中的解除关联原因码（Reason Code）。

<a id="r_a7efde78911de6991098ba5d837157199"></a>

```c
enum ieee802154_cfi { IEEE802154_CFI_UNKNOWN = 0x00 , IEEE802154_CFI_ASSOCIATION_REQUEST = 0x01 , IEEE802154_CFI_ASSOCIATION_RESPONSE = 0x02 , IEEE802154_CFI_DISASSOCIATION_NOTIFICATION = 0x03 , IEEE802154_CFI_DATA_REQUEST = 0x04 , IEEE802154_CFI_PAN_ID_CONFLICT_NOTIFICATION = 0x05 , IEEE802154_CFI_ORPHAN_NOTIFICATION = 0x06 , IEEE802154_CFI_BEACON_REQUEST = 0x07 , IEEE802154_CFI_COORDINATOR_REALIGNEMENT = 0x08 , IEEE802154_CFI_GTS_REQUEST = 0x09 , IEEE802154_CFI_RESERVED = 0x0a }
```

相关声明：[ieee802154_cfi](#a7efde78911de6991098ba5d837157199)、[IEEE802154_CFI_UNKNOWN](#a7efde78911de6991098ba5d837157199a9371a4aeeab31f2f0eb52a188d8a2990)、[IEEE802154_CFI_ASSOCIATION_REQUEST](#a7efde78911de6991098ba5d837157199a867cc7c5b4c9e1b99dda26bfc1713d87)、[IEEE802154_CFI_ASSOCIATION_RESPONSE](#a7efde78911de6991098ba5d837157199a2541a973cde011d980fe2565803a30f4)、[IEEE802154_CFI_DISASSOCIATION_NOTIFICATION](#a7efde78911de6991098ba5d837157199a0ee7d320f5923af196869ac9c348ec34)、[IEEE802154_CFI_DATA_REQUEST](#a7efde78911de6991098ba5d837157199a8d85bf1bc19b90562b854db227c74211)、[IEEE802154_CFI_PAN_ID_CONFLICT_NOTIFICATION](#a7efde78911de6991098ba5d837157199a446febb8ad088218de365cd86d406c94)、[IEEE802154_CFI_ORPHAN_NOTIFICATION](#a7efde78911de6991098ba5d837157199a0a15cf36690a5224f8239f24687ca09f)、[IEEE802154_CFI_BEACON_REQUEST](#a7efde78911de6991098ba5d837157199a89935d04845589a5a8d4c4d6abeb4ef5)、[IEEE802154_CFI_COORDINATOR_REALIGNEMENT](#a7efde78911de6991098ba5d837157199a234e0cdb8bebaa8e9da8da2052babd71)、[IEEE802154_CFI_GTS_REQUEST](#a7efde78911de6991098ba5d837157199a256265e47b2e4cdc50596153ee2a9018)、[IEEE802154_CFI_RESERVED](#a7efde78911de6991098ba5d837157199a9ebdc4dfb6ca44098e9bdc2635dc7b18)。

MAC 命令的命令帧标识符（Command Frame Identifier，CFI）值。

## 5.4\_详细说明（Detailed Documentation）

<a id="a3f791448bce9ad9297401f7725835eb4"></a>

### `IEEE802154_ACK_PKT_LENGTH`

```c
#define IEEE802154_ACK_PKT_LENGTH 3
```

立即确认（Immediate Acknowledgment，Imm-Ack）帧的 MAC 协议数据单元（MPDU）长度，单位为八位组（Octet）。

立即确认（Imm-Ack）仅由帧控制（Frame Control）字段和序列号（Sequence Number）字段组成；参见第 7.3.3 节和图 7-17。

<a id="a041a677ab85038ad00ce3ff00132aaa7"></a>

### `IEEE802154_AUTH_TAG_LENGTH_128`

```c
#define IEEE802154_AUTH_TAG_LENGTH_128 16
```

MIC-128 模式的认证标签（Authentication Tag）长度，单位为八位组（Octet）。

对应 `IEEE802154_SECURITY_LEVEL_MIC_128` 和 `IEEE802154_SECURITY_LEVEL_ENC_MIC_128`。

<a id="a3b252760d00618bf006c4939327a3cc2"></a>

### `IEEE802154_AUTH_TAG_LENGTH_32`

```c
#define IEEE802154_AUTH_TAG_LENGTH_32 4
```

MIC-32 模式的认证标签（Authentication Tag）长度，单位为八位组（Octet）。

对应 `IEEE802154_SECURITY_LEVEL_MIC_32` 和 `IEEE802154_SECURITY_LEVEL_ENC_MIC_32`。

<a id="a5ce2b6b1b0aa9f166aac68fbf5d522e4"></a>

### `IEEE802154_AUTH_TAG_LENGTH_64`

```c
#define IEEE802154_AUTH_TAG_LENGTH_64 8
```

MIC-64 模式的认证标签（Authentication Tag）长度，单位为八位组（Octet）。

对应 `IEEE802154_SECURITY_LEVEL_MIC_64` 和 `IEEE802154_SECURITY_LEVEL_ENC_MIC_64`。

<a id="a5f7adf99bac9e2a46f3b013d960ff4b8"></a>

### `IEEE802154_BEACON_GTS_DIR_SIZE`

```c
#define IEEE802154_BEACON_GTS_DIR_SIZE 1
```

GTS 方向（GTS Direction）字段的长度，单位为八位组（Octet）。

当 GTS 描述符计数（GTS Descriptor Count）子字段不为零时存在；参见第 7.3.1.5 节和图 7-10。

<a id="a04623eec2e0971b164b145ae365e7a8d"></a>

### `IEEE802154_BEACON_GTS_IF_MIN_SIZE`

```c
#define IEEE802154_BEACON_GTS_IF_MIN_SIZE IEEE802154_BEACON_GTS_SPEC_SIZE
```

仅存在 GTS 规范（GTS Specification）时，保障时隙（GTS）字段的最小长度，单位为八位组（Octet）。

不存在 GTS 描述符（Descriptor）时，与 `IEEE802154_BEACON_GTS_SPEC_SIZE` 相同。

<a id="a3d3ff94ce6204f4b7abd972a53f27f26"></a>

### `IEEE802154_BEACON_GTS_RX`

```c
#define IEEE802154_BEACON_GTS_RX 1
```

仅接收保障时隙（Receive-only GTS）的描述符方向值。

参见图 7-11 中的设备类型（Device Type）子字段。

<a id="acd065b4e0ce7a30a950d7a1ce1841d02"></a>

### `IEEE802154_BEACON_GTS_SIZE`

```c
#define IEEE802154_BEACON_GTS_SIZE 3
```

GTS 列表（GTS List）字段中一个 GTS 描述符（Descriptor）的长度，单位为八位组（Octet）。

每个描述符（Descriptor）占三个八位组（Octet）；参见第 7.3.1.5 节和图 7-11。

<a id="a3745048f0cf83f38e060978d6ffd1ccc"></a>

### `IEEE802154_BEACON_GTS_SPEC_SIZE`

```c
#define IEEE802154_BEACON_GTS_SPEC_SIZE 1
```

保障时隙规范（GTS Specification）字段的长度，单位为八位组（Octet）。

参见第 7.3.1.5 节及图 7-9。

<a id="a77527e2b10568aefd0152d6b08aa33a9"></a>

### `IEEE802154_BEACON_GTS_TX`

```c
#define IEEE802154_BEACON_GTS_TX 0
```

仅发送保障时隙（Transmit-only GTS）的描述符方向值。

参见图 7-11 中的设备类型（Device Type）子字段。

<a id="a953435b3c17981ebe7e3c8d27eb41f3e"></a>

### `IEEE802154_BEACON_MIN_SIZE`

```c
#define IEEE802154_BEACON_MIN_SIZE 4
```

信标载荷（Beacon Payload）字段的最小长度，单位为八位组（Octet）。

至少包含超帧规范（Superframe Specification）、GTS 规范（GTS Specification）和待处理地址规范（Pending Address Specification）字段；参见第 7.3.1 节和图 7-6。

<a id="a60daa438820182fe4f9d8ad22e93c935"></a>

### `IEEE802154_BEACON_PAS_IF_MIN_SIZE`

```c
#define IEEE802154_BEACON_PAS_IF_MIN_SIZE IEEE802154_BEACON_PAS_SPEC_SIZE
```

仅存在规范字段时，待处理地址（Pending Address）字段的最小长度，单位为八位组（Octet）。

未列出任何待处理地址（Pending Address）时，与 `IEEE802154_BEACON_PAS_SPEC_SIZE` 相同。

<a id="a83d3c27393203aba941af700eb82c739"></a>

### `IEEE802154_BEACON_PAS_SPEC_SIZE`

```c
#define IEEE802154_BEACON_PAS_SPEC_SIZE 1
```

待处理地址规范（Pending Address Specification）字段的长度，单位为八位组（Octet）。

参见第 7.3.1.6 节及图 7-12。

<a id="a30b5cca2bcf74cce616ae8e901fc1c5b"></a>

### `IEEE802154_BEACON_SF_SIZE`

```c
#define IEEE802154_BEACON_SF_SIZE 2
```

超帧规范（Superframe Specification）字段的长度，单位为八位组（Octet）。

参见第 7.3.1.4 节及图 7-7。

<a id="a848b45622662cb7d0f2653ebaab09bd9"></a>

### `IEEE802154_CMD_ASSOC_REQ_LENGTH`

```c
#define IEEE802154_CMD_ASSOC_REQ_LENGTH 1
```

关联请求（Association Request）命令载荷（能力信息（Capability Information））的长度，单位为八位组（Octet）。

1 个八位字节（Octets）；参见第 7.5.2 节。

<a id="a950a98517a7c0068bcdc6d099d5e2997"></a>

### `IEEE802154_CMD_ASSOC_RES_LENGTH`

```c
#define IEEE802154_CMD_ASSOC_RES_LENGTH 3
```

关联响应（Association Response）命令载荷的长度，单位为八位组（Octet）。

3 个八位字节（Octets）；参见第 7.5.3 节。

<a id="a9d7451a2c78857e0d9650c51e4f0a06a"></a>

### `IEEE802154_CMD_CFI_LENGTH`

```c
#define IEEE802154_CMD_CFI_LENGTH 1
```

命令帧标识符（Command Frame Identifier）字段的长度，单位为八位组（Octet）。

1 个八位字节（Octets）；参见第 7.5.1 节。

<a id="a3486e79bb2efb3dec6124ff4fa092b21"></a>

### `IEEE802154_CMD_COORD_REALIGN_LENGTH`

```c
#define IEEE802154_CMD_COORD_REALIGN_LENGTH 3
```

此处涵盖的协调器重对齐（Coordinator Realignment）命令载荷的最小长度，单位为八位组（Octet）。

载荷（Payload）的前三个八位组（Octet）；参见第 7.5.10 节。

<a id="af141f1fa16d118eb2c2f786813745e6f"></a>

### `IEEE802154_CMD_DISASSOC_NOTE_LENGTH`

```c
#define IEEE802154_CMD_DISASSOC_NOTE_LENGTH 1
```

解除关联通知（Disassociation Notification）命令载荷的长度，单位为八位组（Octet）。

1 个八位字节（Octets）；参见第 7.5.4 节。

<a id="a6ef8827cf387edee15d3252dd8af9a41"></a>

### `IEEE802154_FCF_SEQ_LENGTH`

```c
#define IEEE802154_FCF_SEQ_LENGTH 3
```

帧控制（Frame Control）字段与序列号（Sequence Number）字段的总长度，单位为八位组（Octet）。

这些是通用 MAC 帧格式的前三个八位组（Octet）；参见图 7-2 和第 7.2.2 节。

<a id="a5fd880c4112671a1d17c31c84d41eb28"></a>

### `IEEE802154_GTS_REQUEST_LENGTH`

```c
#define IEEE802154_GTS_REQUEST_LENGTH 1
```

GTS 请求（GTS Request）命令载荷的长度，单位为八位组（Octet）。

1 个八位字节（Octets）；参见第 7.5.11 节。

<a id="a4b7a12e735b0c3f7896480ec62818dc4"></a>

### `IEEE802154_KEY_ID_FIELD_INDEX_LENGTH`

```c
#define IEEE802154_KEY_ID_FIELD_INDEX_LENGTH 1
```

密钥标识符模式 1（Key Identifier Mode 1）中密钥标识符字段的长度，单位为八位组（Octet）。

仅包含密钥索引（Key Index）；参见表 9-7。

<a id="a59da421480bdd7a4e0e00fd091d8a9ec"></a>

### `IEEE802154_KEY_ID_FIELD_SRC_4_INDEX_LENGTH`

```c
#define IEEE802154_KEY_ID_FIELD_SRC_4_INDEX_LENGTH 5
```

密钥标识符模式 2（Key Identifier Mode 2）中密钥标识符字段的长度，单位为八位组（Octet）。

四个八位组（Octet）的密钥来源（Key Source）加上密钥索引（Key Index）；参见表 9-7。

<a id="a30b9143792a736afc9a1e051cb07eeb5"></a>

### `IEEE802154_KEY_ID_FIELD_SRC_8_INDEX_LENGTH`

```c
#define IEEE802154_KEY_ID_FIELD_SRC_8_INDEX_LENGTH 9
```

密钥标识符模式 3（Key Identifier Mode 3）中密钥标识符字段的长度，单位为八位组（Octet）。

八个八位组（Octet）的密钥来源（Key Source）加上密钥索引（Key Index）；参见表 9-7。

<a id="a181095776e2bbe690d8b8d694d00cb5b"></a>

### `IEEE802154_KEY_MAX_LEN`

```c
#define IEEE802154_KEY_MAX_LEN 16
```

本 API 中 MAC 安全操作的最大密钥（Key）长度，单位为八位组（Octet）。

与典型的 AES-128 密钥（Key）大小一致；参见第 9.4 节。

<a id="aa446d872aea406d4946c9c0e2f286c2e"></a>

### `IEEE802154_MIN_LENGTH`

```c
#define IEEE802154_MIN_LENGTH IEEE802154_ACK_PKT_LENGTH
```

此处支持的最小 MAC 帧 NMPDU 长度（与 `IEEE802154_ACK_PKT_LENGTH` 相同）。

标准定义的最短 MAC 帧为立即确认（Imm-Ack）；参见第 7.3.3 节。

<a id="a78fb36a5e46dfa669d199eb630a3adda"></a>

### `IEEE802154_PAN_ID_LENGTH`

```c
#define IEEE802154_PAN_ID_LENGTH 2
```

MAC 寻址字段中个域网标识符（PAN Identifier）的长度，单位为八位组（Octet）。

个域网标识符（PAN ID）占两个八位组（Octet）；参见第 7.2.2.8 节。

<a id="ac05f9f47c969440174e2fb801fc08976"></a>

### `IEEE802154_SECURITY_CF_LENGTH`

```c
#define IEEE802154_SECURITY_CF_LENGTH 1
```

安全控制（Security Control）字段的长度，单位为八位组（Octet）。

1 个八位字节（Octets）；参见第 9.4.2 节。

<a id="a065430381b20783ed8ef9a04708b3e54"></a>

### `IEEE802154_SECURITY_FRAME_COUNTER_LENGTH`

```c
#define IEEE802154_SECURITY_FRAME_COUNTER_LENGTH 4
```

辅助安全头部（Auxiliary Security Header）中帧计数器（Frame Counter）字段的长度，单位为八位组（Octet）。

4 个八位字节（Octets）；参见第 9.4.3 节。

<a id="a9fe069f17d6dc89ad8085056bd7f0956"></a>

### `IEEE802154_SECURITY_LEVEL_ENC`

```c
#define IEEE802154_SECURITY_LEVEL_ENC IEEE802154_SECURITY_LEVEL_RESERVED
```

将安全级别（Security Level）与此值比较，以识别加密模式（Encryption Mode）。

严格大于此常量的安全级别（Security Level）值使用加密（ENC MIC）；参见表 9-6。此常量定义为保留码点（Reserved Codepoint）`IEEE802154_SECURITY_LEVEL_RESERVED`。

<a id="a49f3241733da0a6dd0003d7bcaf55965"></a>

### `ieee802154_addressing_mode`

```c
enum ieee802154_addressing_mode
```

目的地址与源地址寻址模式（Destination and Source Addressing Mode）子字段的值。

参见第 7.2.2.9 节及表 7-3。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `IEEE802154_ADDR_MODE_NONE` | 省略寻址字段（Addressing Fields），即字段不存在。 |
| `IEEE802154_ADDR_MODE_RESERVED` | 保留（Reserved）；不得使用。 |
| `IEEE802154_ADDR_MODE_SHORT` | 短地址（Short Address），16 位。 |
| `IEEE802154_ADDR_MODE_EXTENDED` | 扩展地址（Extended Address），64 位。 |

<a id="aa2c9cb8ba5b7c397c695a9a591649b91"></a>

### `ieee802154_association_status_field`

```c
enum ieee802154_association_status_field
```

关联响应（Association Response）命令中的关联状态（Association Status）值。

参见第 7.5.3 节。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `IEEE802154_ASF_SUCCESSFUL` | 关联成功（Association Successful）。 |
| `IEEE802154_ASF_PAN_AT_CAPACITY` | 个域网（PAN）容量已满。 |
| `IEEE802154_ASF_PAN_ACCESS_DENIED` | 个域网（PAN）访问被拒绝。 |
| `IEEE802154_ASF_RESERVED` | 保留（Reserved）。 |
| `IEEE802154_ASF_RESERVED_PRIMITIVES` | 为 MAC 原语（Primitive）保留的范围。 |

<a id="a7efde78911de6991098ba5d837157199"></a>

### `ieee802154_cfi`

```c
enum ieee802154_cfi
```

MAC 命令的命令帧标识符（Command Frame Identifier，CFI）值。

参见第 7.5.1 节。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `IEEE802154_CFI_UNKNOWN` | 未知或未指定的命令（Command）。 |
| `IEEE802154_CFI_ASSOCIATION_REQUEST` | 关联请求（Association Request）。 |
| `IEEE802154_CFI_ASSOCIATION_RESPONSE` | 关联响应（Association Response）。 |
| `IEEE802154_CFI_DISASSOCIATION_NOTIFICATION` | 解除关联通知（Disassociation Notification）。 |
| `IEEE802154_CFI_DATA_REQUEST` | 数据请求（Data Request）。 |
| `IEEE802154_CFI_PAN_ID_CONFLICT_NOTIFICATION` | 个域网标识符冲突通知（PAN ID Conflict Notification）。 |
| `IEEE802154_CFI_ORPHAN_NOTIFICATION` | 孤立设备通知（Orphan Notification）。 |
| `IEEE802154_CFI_BEACON_REQUEST` | 信标请求（Beacon Request）。 |
| `IEEE802154_CFI_COORDINATOR_REALIGNEMENT` | 协调器重对齐（Coordinator Realignment）。 |
| `IEEE802154_CFI_GTS_REQUEST` | 保障时隙请求（GTS Request）。 |
| `IEEE802154_CFI_RESERVED` | 保留（Reserved）。 |

<a id="a2ab06c343e03a4d6e28073780eb47648"></a>

### `ieee802154_disassociation_reason_field`

```c
enum ieee802154_disassociation_reason_field
```

解除关联通知（Disassociation Notification）命令中的解除关联原因码（Reason Code）。

参见第 7.5.4 节。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `IEEE802154_DRF_RESERVED_1` | 保留（Reserved）。 |
| `IEEE802154_DRF_COORDINATOR_WISH` | 协调器（Coordinator）希望设备离开。 |
| `IEEE802154_DRF_DEVICE_WISH` | 设备（Device）希望离开。 |
| `IEEE802154_DRF_RESERVED_2` | 保留（Reserved）。 |
| `IEEE802154_DRF_RESERVED_PRIMITIVES` | 为 MAC 原语（Primitive）保留的范围。 |

<a id="a16702b800d3e4a51df6cb6f909ff79fd"></a>

### `ieee802154_frame_type`

```c
enum ieee802154_frame_type
```

帧控制（Frame Control）字段中帧类型（Frame Type）子字段的值。

参见第 7.2.2.2 节及表 7-1。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `IEEE802154_FRAME_TYPE_BEACON` | 信标帧（Beacon Frame）。 |
| `IEEE802154_FRAME_TYPE_DATA` | 数据帧（Data Frame）。 |
| `IEEE802154_FRAME_TYPE_ACK` | 确认帧（Acknowledgment Frame）。 |
| `IEEE802154_FRAME_TYPE_MAC_COMMAND` | MAC 命令帧（MAC Command Frame）。 |
| `IEEE802154_FRAME_TYPE_RESERVED` | 保留的帧类型（Reserved Frame Type）。 |
| `IEEE802154_FRAME_TYPE_MULTIPURPOSE` | 多用途帧（Multipurpose Frame）。 |
| `IEEE802154_FRAME_TYPE_FRAK` | FRak 帧，即分片确认（Fragment Acknowledgment）帧。 |
| `IEEE802154_FRAME_TYPE_EXTENDED` | 扩展帧类型（Extended Frame Type）；使用扩展帧类型字段。 |

<a id="ac5819ed25fa7b56756e8e7962f579ec7"></a>

### `ieee802154_key_id_mode`

```c
enum ieee802154_key_id_mode
```

密钥标识符模式（Key Identifier Mode）子字段的值。

参见第 9.4.2.3 节及表 9-7。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `IEEE802154_KEY_ID_MODE_IMPLICIT` | 以隐式方式确定密钥（Key）。 |
| `IEEE802154_KEY_ID_MODE_INDEX` | 仅包含密钥索引（Key Index）。 |
| `IEEE802154_KEY_ID_MODE_SRC_4_INDEX` | 4 个八位组（Octet）的密钥来源（Key Source）和密钥索引（Key Index）。 |
| `IEEE802154_KEY_ID_MODE_SRC_8_INDEX` | 8 个八位组（Octet）的密钥来源（Key Source）和密钥索引（Key Index）。 |

<a id="aaf5ffabf140bf36c9076662e4b46e4a2"></a>

### `ieee802154_security_level`

```c
enum ieee802154_security_level
```

安全控制（Security Control）字段中安全级别（Security Level）子字段的值。

参见第 9.4.2.2 节及表 9-6。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `IEEE802154_SECURITY_LEVEL_NONE` | 不提供安全保护（No Security）：不加密，也不认证。 |
| `IEEE802154_SECURITY_LEVEL_MIC_32` | 仅进行 MIC-32 认证（Authentication）。 |
| `IEEE802154_SECURITY_LEVEL_MIC_64` | 仅进行 MIC-64 认证（Authentication）。 |
| `IEEE802154_SECURITY_LEVEL_MIC_128` | 仅进行 MIC-128 认证（Authentication）。 |
| `IEEE802154_SECURITY_LEVEL_RESERVED` | 保留（Reserved）。 |
| `IEEE802154_SECURITY_LEVEL_ENC_MIC_32` | 加密并使用 MIC-32（Encryption with MIC-32）。 |
| `IEEE802154_SECURITY_LEVEL_ENC_MIC_64` | 加密并使用 MIC-64（Encryption with MIC-64）。 |
| `IEEE802154_SECURITY_LEVEL_ENC_MIC_128` | 加密并使用 MIC-128（Encryption with MIC-128）。 |

<a id="aa6a4b34e9722f5ccd06b65cf64efe053"></a>

### `ieee802154_version`

```c
enum ieee802154_version
```

帧版本（Frame Version）子字段的值。

参见第 7.2.2.10 节。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `IEEE802154_VERSION_802154_2003` | IEEE 802.15.4-2003 标准（IEEE Std 802.15.4-2003）。 |
| `IEEE802154_VERSION_802154_2006` | IEEE 802.15.4-2006 标准（IEEE Std 802.15.4-2006）。 |
| `IEEE802154_VERSION_802154` | IEEE 802.15.4 标准（IEEE Std 802.15.4），不含 2003 和 2006 版本。 |
| `IEEE802154_VERSION_RESERVED` | 保留供将来使用。 |


## 5.5\_原页交叉引用（Cross References）

- [zephyr/kernel.h](../api_source_workqueue_pin_control_reference/P002_kernel.h_源码浏览.md)
- [zephyr/net/ieee802154.h](../api_source_configuration_reference/P031_ieee802154.h_源码浏览.md)
- [zephyr/net/net_pkt.h](../api_source_packet_gnss_reference/P006_net_pkt.h_源码浏览.md)
- [zephyr/toolchain.h](../api_source_compiler_device_reference/P023_toolchain.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P338_ieee802154_frame.h_源码浏览.md)
- [ieee802154_fcf_seq](../network_core_model_reference/P016_ieee802154_fcf_seq_结构体.md)
- [ieee802154_address](../network_core_model_reference/P001_ieee802154_address_结构体.md)
- [ieee802154_address_field_comp](../network_core_model_reference/P003_ieee802154_address_field_comp_结构体.md)
- [ieee802154_address_field_plain](../network_core_model_reference/P004_ieee802154_address_field_plain_结构体.md)
- [ieee802154_address_field](../network_core_model_reference/P002_ieee802154_address_field_结构体.md)
- [ieee802154_security_control_field](../network_core_model_reference/P043_ieee802154_security_control_field_结构体.md)
- [ieee802154_key_identifier_field](../network_core_model_reference/P033_ieee802154_key_identifier_field_结构体.md)
- [ieee802154_aux_security_hdr](../network_core_model_reference/P006_ieee802154_aux_security_hdr_结构体.md)
- [ieee802154_mhr](../network_core_model_reference/P034_ieee802154_mhr_结构体.md)
- [ieee802154_gts_dir](../network_core_model_reference/P020_ieee802154_gts_dir_结构体.md)
- [ieee802154_gts](../network_core_model_reference/P019_ieee802154_gts_结构体.md)
- [ieee802154_gts_spec](../network_core_model_reference/P022_ieee802154_gts_spec_结构体.md)
- [ieee802154_pas_spec](../network_core_model_reference/P038_ieee802154_pas_spec_结构体.md)
- [ieee802154_beacon_sf](../network_core_model_reference/P008_ieee802154_beacon_sf_结构体.md)
- [ieee802154_beacon](../network_core_model_reference/P007_ieee802154_beacon_结构体.md)
- [ieee802154_cmd_assoc_req](../network_core_model_reference/P009_ieee802154_cmd_assoc_req_结构体.md)
- [ieee802154_cmd_assoc_res](../network_core_model_reference/P010_ieee802154_cmd_assoc_res_结构体.md)
- [ieee802154_cmd_disassoc_note](../network_core_model_reference/P012_ieee802154_cmd_disassoc_note_结构体.md)
- [ieee802154_cmd_coord_realign](../network_core_model_reference/P011_ieee802154_cmd_coord_realign_结构体.md)
- [ieee802154_gts_request](../network_core_model_reference/P021_ieee802154_gts_request_结构体.md)
- [ieee802154_command](../network_core_model_reference/P013_ieee802154_command_结构体.md)
- [ieee802154_mpdu](../network_core_model_reference/P035_ieee802154_mpdu_结构体.md)
- [ieee802154_frame_params](../network_core_model_reference/P018_ieee802154_frame_params_结构体.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="a49f3241733da0a6dd0003d7bcaf55965a50e45c02f42ef667e1216cfc1024860f"></a>
<a id="a49f3241733da0a6dd0003d7bcaf55965a6f5f3599146d548b541dd22fa1f6322c"></a>
<a id="a49f3241733da0a6dd0003d7bcaf55965aa51f0be0ff88addcd167b03051e2dc21"></a>
<a id="a49f3241733da0a6dd0003d7bcaf55965a27c38f60597d1b202cbb0e6c8cad27fd"></a>
<a id="aa2c9cb8ba5b7c397c695a9a591649b91a280571e677e992f5220f56818e52ccf4"></a>
<a id="aa2c9cb8ba5b7c397c695a9a591649b91a571c5b2f63cedf01857ce31ba1125517"></a>
<a id="aa2c9cb8ba5b7c397c695a9a591649b91a1cedbaa8a44fdb79041e6b5ad8af6031"></a>
<a id="aa2c9cb8ba5b7c397c695a9a591649b91a3a72c63164f925e7fe6d12d9cf572d81"></a>
<a id="aa2c9cb8ba5b7c397c695a9a591649b91a15eb8c84a04a1642e7395a872eb5db59"></a>
<a id="a7efde78911de6991098ba5d837157199a9371a4aeeab31f2f0eb52a188d8a2990"></a>
<a id="a7efde78911de6991098ba5d837157199a867cc7c5b4c9e1b99dda26bfc1713d87"></a>
<a id="a7efde78911de6991098ba5d837157199a2541a973cde011d980fe2565803a30f4"></a>
<a id="a7efde78911de6991098ba5d837157199a0ee7d320f5923af196869ac9c348ec34"></a>
<a id="a7efde78911de6991098ba5d837157199a8d85bf1bc19b90562b854db227c74211"></a>
<a id="a7efde78911de6991098ba5d837157199a446febb8ad088218de365cd86d406c94"></a>
<a id="a7efde78911de6991098ba5d837157199a0a15cf36690a5224f8239f24687ca09f"></a>
<a id="a7efde78911de6991098ba5d837157199a89935d04845589a5a8d4c4d6abeb4ef5"></a>
<a id="a7efde78911de6991098ba5d837157199a234e0cdb8bebaa8e9da8da2052babd71"></a>
<a id="a7efde78911de6991098ba5d837157199a256265e47b2e4cdc50596153ee2a9018"></a>
<a id="a7efde78911de6991098ba5d837157199a9ebdc4dfb6ca44098e9bdc2635dc7b18"></a>
<a id="a2ab06c343e03a4d6e28073780eb47648aec815962bcc4fe41d8a2223bc7b7e3c7"></a>
<a id="a2ab06c343e03a4d6e28073780eb47648a8b04f0bae8a62282a8a7821a4db949cb"></a>
<a id="a2ab06c343e03a4d6e28073780eb47648a3feadbd533ba9b31977e2fa7537fa8c1"></a>
<a id="a2ab06c343e03a4d6e28073780eb47648ae09de01a9f7b2a7eba0ee0173765e1ef"></a>
<a id="a2ab06c343e03a4d6e28073780eb47648a2d69c0e06015471da07bce9314a900c7"></a>
<a id="a16702b800d3e4a51df6cb6f909ff79fda6253c6948e0ecbc79878bd1fd73473ec"></a>
<a id="a16702b800d3e4a51df6cb6f909ff79fda59490f8a40d1c65c365b3370ccabd3d8"></a>
<a id="a16702b800d3e4a51df6cb6f909ff79fdacd5ec548c6199b61912ed8a15df3b486"></a>
<a id="a16702b800d3e4a51df6cb6f909ff79fda69235bb8211a5a4a3c4fde6379d28644"></a>
<a id="a16702b800d3e4a51df6cb6f909ff79fdaf14e1c3c75c77dcfaf54d2d637b9b4ae"></a>
<a id="a16702b800d3e4a51df6cb6f909ff79fda953e79789829eb3e220bccb94f21316f"></a>
<a id="a16702b800d3e4a51df6cb6f909ff79fdaaabec4197346f0d36903217c1f68b90f"></a>
<a id="a16702b800d3e4a51df6cb6f909ff79fdacb7f98a3d76846d411bc698572a5eeb5"></a>
<a id="ac5819ed25fa7b56756e8e7962f579ec7a2519ea53b9adf534707e7ce4401966f6"></a>
<a id="ac5819ed25fa7b56756e8e7962f579ec7a918058e16c48ecee20a8ce3968138c04"></a>
<a id="ac5819ed25fa7b56756e8e7962f579ec7ae351b9dc1ba1e546a706c861b4dfd841"></a>
<a id="ac5819ed25fa7b56756e8e7962f579ec7a0c363713ca56c27961d5198a5ee7078f"></a>
<a id="aaf5ffabf140bf36c9076662e4b46e4a2af5bff347e35ac0af5c86b65ef231df47"></a>
<a id="aaf5ffabf140bf36c9076662e4b46e4a2a2b8b7e0d195c7fb33e3578b86bda99d7"></a>
<a id="aaf5ffabf140bf36c9076662e4b46e4a2abe9a01bb053e5809e0f110cb0709d001"></a>
<a id="aaf5ffabf140bf36c9076662e4b46e4a2a60e7720ffc14a08b0f4c90b567ce57bd"></a>
<a id="aaf5ffabf140bf36c9076662e4b46e4a2a2155c782cf4074f240bcb087aecc8f06"></a>
<a id="aaf5ffabf140bf36c9076662e4b46e4a2a95e1e7954023a5cd3c35aaf6596b0821"></a>
<a id="aaf5ffabf140bf36c9076662e4b46e4a2a649d558004918cacb4c9ec32d247c934"></a>
<a id="aaf5ffabf140bf36c9076662e4b46e4a2abaa5076f0f373c3f2e415a8f28a6e0ee"></a>
<a id="aa6a4b34e9722f5ccd06b65cf64efe053aad3af323ce4f598be0256ec9c19dcf36"></a>
<a id="aa6a4b34e9722f5ccd06b65cf64efe053a3b2b709ecd3a2a1a4b997baf26c40bbc"></a>
<a id="aa6a4b34e9722f5ccd06b65cf64efe053aa2a088916733a4de4d009caaea734ca2"></a>
<a id="aa6a4b34e9722f5ccd06b65cf64efe053a8112ae7940d211afe7a5a1a79071ad57"></a>

---

[上一章](P004_zephyr__drivers__i3c.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P006_zephyr__kernel.h_文件参考.md)

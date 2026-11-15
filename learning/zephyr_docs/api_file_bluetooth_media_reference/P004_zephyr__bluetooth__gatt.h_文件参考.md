---
id: learning.zephyr-docs.api-file-bluetooth-media-reference.page-4
title: zephyr__bluetooth__gatt.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/gatt_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_zephyr\_\_bluetooth\_\_gatt.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/gatt_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

通用属性配置文件（Generic Attribute Profile）的处理。

<a id="details"></a>

```c
#include <stdint.h>
#include <stddef.h>
#include <string.h>
#include <sys/types.h>
#include <zephyr/autoconf.h>
#include <zephyr/bluetooth/addr.h>
#include <zephyr/bluetooth/conn.h>
#include <zephyr/bluetooth/uuid.h>
#include <zephyr/bluetooth/att.h>
#include <zephyr/sys/atomic.h>
#include <zephyr/sys/iterable_sections.h>
#include <zephyr/sys/slist.h>
#include <zephyr/sys/util.h>
#include <zephyr/sys/util_macro.h>
#include <zephyr/toolchain.h>
```

查看此文件的源码。

通用属性配置文件（Generic Attribute Profile）的处理。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 4.1\_数据结构（Data Structures）

<a id="r_bt_5Fgatt_5Fattr"></a>

```c
struct bt_gatt_attr
```

相关声明：[bt_gatt_attr](../bluetooth_connection_model_reference/P049_bt_gatt_attr_结构体.md)。

通用属性配置文件（GATT）属性（Attribute）。

<a id="r_bt_5Fgatt_5Fservice_5Fstatic"></a>

```c
struct bt_gatt_service_static
```

相关声明：[bt_gatt_service_static](../bluetooth_connection_model_reference/P066_bt_gatt_service_static_结构体.md)。

静态 GATT 服务结构体。

<a id="r_bt_5Fgatt_5Fservice"></a>

```c
struct bt_gatt_service
```

相关声明：[bt_gatt_service](../bluetooth_connection_model_reference/P065_bt_gatt_service_结构体.md)。

GATT 服务（Service）结构体。

<a id="r_bt_5Fgatt_5Fservice_5Fval"></a>

```c
struct bt_gatt_service_val
```

相关声明：[bt_gatt_service_val](../bluetooth_connection_model_reference/P067_bt_gatt_service_val_结构体.md)。

服务（Service）属性值。

<a id="r_bt_5Fgatt_5Finclude"></a>

```c
struct bt_gatt_include
```

相关声明：[bt_gatt_include](../bluetooth_connection_model_reference/P060_bt_gatt_include_结构体.md)。

包含服务（Include）属性值。

<a id="r_bt_5Fgatt_5Fcb"></a>

```c
struct bt_gatt_cb
```

相关声明：[bt_gatt_cb](../bluetooth_connection_model_reference/P051_bt_gatt_cb_结构体.md)。

GATT 回调结构体。

<a id="r_bt_5Fgatt_5Fauthorization_5Fcb"></a>

```c
struct bt_gatt_authorization_cb
```

相关声明：[bt_gatt_authorization_cb](../bluetooth_connection_model_reference/P050_bt_gatt_authorization_cb_结构体.md)。

GATT 授权（Authorization）回调结构体。

<a id="r_bt_5Fgatt_5Fchrc"></a>

```c
struct bt_gatt_chrc
```

相关声明：[bt_gatt_chrc](../bluetooth_connection_model_reference/P056_bt_gatt_chrc_结构体.md)。

特征声明（Characteristic Declaration）的属性值。

<a id="r_bt_5Fgatt_5Fcep"></a>

```c
struct bt_gatt_cep
```

相关声明：[bt_gatt_cep](../bluetooth_connection_model_reference/P055_bt_gatt_cep_结构体.md)。

特征扩展属性（Characteristic Extended Properties）属性值。

<a id="r_bt_5Fgatt_5Fccc"></a>

```c
struct bt_gatt_ccc
```

相关声明：[bt_gatt_ccc](../bluetooth_connection_model_reference/P052_bt_gatt_ccc_结构体.md)。

客户端特征配置（Client Characteristic Configuration，CCC）属性值。

<a id="r_bt_5Fgatt_5Fscc"></a>

```c
struct bt_gatt_scc
```

相关声明：[bt_gatt_scc](../bluetooth_connection_model_reference/P064_bt_gatt_scc_结构体.md)。

服务器特征配置（Server Characteristic Configuration）属性值。

<a id="r_bt_5Fgatt_5Fcpf"></a>

```c
struct bt_gatt_cpf
```

相关声明：[bt_gatt_cpf](../bluetooth_connection_model_reference/P057_bt_gatt_cpf_结构体.md)。

GATT 特征呈现格式（Characteristic Presentation Format）属性值。

<a id="r_bt_5Fgatt_5Fccc_5Fcfg"></a>

```c
struct bt_gatt_ccc_cfg
```

相关声明：[bt_gatt_ccc_cfg](../bluetooth_connection_model_reference/P053_bt_gatt_ccc_cfg_结构体.md)。

GATT CCC 配置条目。

<a id="r_bt_5Fgatt_5Fccc_5Fmanaged_5Fuser_5Fdata"></a>

```c
struct bt_gatt_ccc_managed_user_data
```

相关声明：[bt_gatt_ccc_managed_user_data](../bluetooth_connection_model_reference/P054_bt_gatt_ccc_managed_user_data_结构体.md)。

CCC 值的内部表示（Internal Representation）。

<a id="r_bt_5Fgatt_5Fnotify_5Fparams"></a>

```c
struct bt_gatt_notify_params
```

相关声明：[bt_gatt_notify_params](../bluetooth_connection_model_reference/P062_bt_gatt_notify_params_结构体.md)。

GATT 通知（Notification）参数。

<a id="r_bt_5Fgatt_5Findicate_5Fparams"></a>

```c
struct bt_gatt_indicate_params
```

相关声明：[bt_gatt_indicate_params](../bluetooth_connection_model_reference/P061_bt_gatt_indicate_params_结构体.md)。

GATT 值指示（Indicate Value）参数。

<a id="r_bt_5Fgatt_5Fexchange_5Fparams"></a>

```c
struct bt_gatt_exchange_params
```

相关声明：[bt_gatt_exchange_params](../bluetooth_connection_model_reference/P059_bt_gatt_exchange_params_结构体.md)。

GATT 最大传输单元交换（Exchange MTU）参数。

<a id="r_bt_5Fgatt_5Fdiscover_5Fparams"></a>

```c
struct bt_gatt_discover_params
```

相关声明：[bt_gatt_discover_params](../bluetooth_connection_model_reference/P058_bt_gatt_discover_params_结构体.md)。

GATT 属性发现（Discover Attributes）参数。

<a id="r_bt_5Fgatt_5Fread_5Fparams"></a>

```c
struct bt_gatt_read_params
```

相关声明：[bt_gatt_read_params](../bluetooth_connection_model_reference/P063_bt_gatt_read_params_结构体.md)。

GATT 读取（Read）参数。

<a id="r_bt_5Fgatt_5Fwrite_5Fparams"></a>

```c
struct bt_gatt_write_params
```

相关声明：[bt_gatt_write_params](../bluetooth_connection_model_reference/P069_bt_gatt_write_params_结构体.md)。

GATT 写入（Write）参数。

<a id="r_bt_5Fgatt_5Fsubscribe_5Fparams"></a>

```c
struct bt_gatt_subscribe_params
```

相关声明：[bt_gatt_subscribe_params](../bluetooth_connection_model_reference/P068_bt_gatt_subscribe_params_结构体.md)。

GATT 订阅（Subscribe）参数。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 4.2\_宏定义（Macros）

<a id="r_gaff31756c1bf8ee755e65b1e0fb689bb7"></a>

```c
#define BT_GATT_ERR(_att_err)
```

相关声明：[BT_GATT_ERR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#gaff31756c1bf8ee755e65b1e0fb689bb7)。

构造属性读写回调（Attribute Read/Write Callbacks）的错误返回值。

<a id="r_ga86bddd8211e7466b0457173a0dd412f0"></a>

```c
#define BT_GATT_CHRC_BROADCAST 0x01
```

相关声明：[BT_GATT_CHRC_BROADCAST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#ga86bddd8211e7466b0457173a0dd412f0)。

特征属性（Characteristic Properties）位域值。

<a id="r_gaa243a11d6d8b3e3be815c0893e0220f3"></a>

```c
#define BT_GATT_CHRC_READ 0x02
```

相关声明：[BT_GATT_CHRC_READ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#gaa243a11d6d8b3e3be815c0893e0220f3)。

特征读取属性（Characteristic Read Property）。

<a id="r_ga9c029ca574eb3c5992685b279388ac85"></a>

```c
#define BT_GATT_CHRC_WRITE_WITHOUT_RESP 0x04
```

相关声明：[BT_GATT_CHRC_WRITE_WITHOUT_RESP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#ga9c029ca574eb3c5992685b279388ac85)。

特征无响应写入属性（Characteristic Write Without Response Property）。

<a id="r_gad482d8db34707e1f9da1d8e2ddd5507e"></a>

```c
#define BT_GATT_CHRC_WRITE 0x08
```

相关声明：[BT_GATT_CHRC_WRITE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#gad482d8db34707e1f9da1d8e2ddd5507e)。

特征有响应写入属性（Characteristic Write With Response Property）。

<a id="r_gab8cd9649bdfd125a26065a8ced762a98"></a>

```c
#define BT_GATT_CHRC_NOTIFY 0x10
```

相关声明：[BT_GATT_CHRC_NOTIFY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#gab8cd9649bdfd125a26065a8ced762a98)。

特征通知属性（Characteristic Notify Property）。

<a id="r_gaa9639b9d655ea41767584b638add1f2b"></a>

```c
#define BT_GATT_CHRC_INDICATE 0x20
```

相关声明：[BT_GATT_CHRC_INDICATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#gaa9639b9d655ea41767584b638add1f2b)。

特征指示属性（Characteristic Indicate Property）。

<a id="r_gaab3a26a00f88a6eacd36f2841004204c"></a>

```c
#define BT_GATT_CHRC_AUTH 0x40 __DEPRECATED_MACRO
```

相关声明：[BT_GATT_CHRC_AUTH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#gaab3a26a00f88a6eacd36f2841004204c)。

特征认证签名写入属性（Characteristic Authenticated Signed Writes Property）。

<a id="r_gac84d73a0ad50bfd149ad83181315de1a"></a>

```c
#define BT_GATT_CHRC_EXT_PROP 0x80
```

相关声明：[BT_GATT_CHRC_EXT_PROP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#gac84d73a0ad50bfd149ad83181315de1a)。

特征扩展属性（Characteristic Extended Properties Property）。

<a id="r_gad1825f8deafc36d7e8f09c2835884fc6"></a>

```c
#define BT_GATT_CEP_RELIABLE_WRITE 0x0001
```

相关声明：[BT_GATT_CEP_RELIABLE_WRITE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#gad1825f8deafc36d7e8f09c2835884fc6)。

特征扩展属性（Characteristic Extended Properties）位域值。

<a id="r_ga64898ec8390c89c1fc5bdf0364220a43"></a>

```c
#define BT_GATT_CEP_WRITABLE_AUX 0x0002
```

相关声明：[BT_GATT_CEP_WRITABLE_AUX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#ga64898ec8390c89c1fc5bdf0364220a43)。

特征扩展属性：可写辅助项（Writable Auxiliaries）。

<a id="r_ga240a10df32aa7a256a103ceee7211f8d"></a>

```c
#define BT_GATT_CCC_NOTIFY 0x0001
```

相关声明：[BT_GATT_CCC_NOTIFY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#ga240a10df32aa7a256a103ceee7211f8d)。

客户端特征配置值（Client Characteristic Configuration Values）。

<a id="r_ga60ff2ddcc2e3148881a2f15745ba06e8"></a>

```c
#define BT_GATT_CCC_INDICATE 0x0002
```

相关声明：[BT_GATT_CCC_INDICATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#ga60ff2ddcc2e3148881a2f15745ba06e8)。

客户端特征配置：指示（Client Characteristic Configuration Indication）。

<a id="r_ga7a7d3cfa6eec4baa0b57ec9c4bc41f7a"></a>

```c
#define BT_GATT_SCC_BROADCAST 0x0001
```

相关声明：[BT_GATT_SCC_BROADCAST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#ga7a7d3cfa6eec4baa0b57ec9c4bc41f7a)。

服务器特征配置值（Server Characteristic Configuration Values）。

<a id="r_ga04c7887fb67107bd060dd023fd3186d5"></a>

```c
#define BT_GATT_SERVICE_DEFINE(_name, ...)
```

相关声明：[BT_GATT_SERVICE_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga04c7887fb67107bd060dd023fd3186d5)。

静态定义并注册服务（Service）。

<a id="r_ga8bb3aeef20465d7f6e38f6bbddef74e5"></a>

```c
#define BT_GATT_SERVICE_INSTANCE_DEFINE( _name, _instances, _instance_num, _attrs_def)
```

相关声明：[BT_GATT_SERVICE_INSTANCE_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga8bb3aeef20465d7f6e38f6bbddef74e5)。

静态定义服务结构体数组（Service Structure Array）。

<a id="r_ga7d413ec013b91a633ec24d80d2814e2b"></a>

```c
#define BT_GATT_SERVICE(_attrs)
```

相关声明：[BT_GATT_SERVICE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga7d413ec013b91a633ec24d80d2814e2b)。

服务结构体声明宏（Service Structure Declaration Macro）。

<a id="r_gaacada0ff1029af959b6fcd6703d4a0bf"></a>

```c
#define BT_GATT_PRIMARY_SERVICE(_service)
```

相关声明：[BT_GATT_PRIMARY_SERVICE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#gaacada0ff1029af959b6fcd6703d4a0bf)。

主服务声明宏（Primary Service Declaration Macro）。

<a id="r_gaecb4d30282677d3450ad79c5f83f3445"></a>

```c
#define BT_GATT_SECONDARY_SERVICE(_service)
```

相关声明：[BT_GATT_SECONDARY_SERVICE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#gaecb4d30282677d3450ad79c5f83f3445)。

次级服务声明宏（Secondary Service Declaration Macro）。

<a id="r_ga08ffee706d271b75a54b1b99249dba24"></a>

```c
#define BT_GATT_INCLUDE_SERVICE(_service_incl)
```

相关声明：[BT_GATT_INCLUDE_SERVICE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga08ffee706d271b75a54b1b99249dba24)。

包含服务声明宏（Include Service Declaration Macro）。

<a id="r_ga7f19592a722c41d6c1d2421d166dd78a"></a>

```c
#define BT_GATT_CHRC_INIT(_uuid, _handle, _props)
```

相关声明：[BT_GATT_CHRC_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga7f19592a722c41d6c1d2421d166dd78a)。

GATT 特征初始化宏（Characteristic Initialization Macro）。

<a id="r_ga9e739546dbd906d3b3c4f1ed5ad9f41e"></a>

```c
#define BT_GATT_CHARACTERISTIC(_uuid, _props, _perm, _read, _write, _user_data)
```

相关声明：[BT_GATT_CHARACTERISTIC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga9e739546dbd906d3b3c4f1ed5ad9f41e)。

特征及其值声明宏（Characteristic and Value Declaration Macro）。

<a id="r_gac1c0a195c1ec1ff2cdd5bf6d0ba6ad00"></a>

```c
#define BT_GATT_CCC_MAX 0
```

相关声明：[BT_GATT_CCC_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#gac1c0a195c1ec1ff2cdd5bf6d0ba6ad00)。

BT_GATT_CCC_MAX 的定义取决于是否设置 CONFIG_BT_SETTINGS_CCC_LAZY_LOADING 或 CONFIG_BT_CONN。

<a id="r_gae3a23386bfe38e0127b74e0f4b5e5667"></a>

```c
#define BT_GATT_CCC_MANAGED_USER_DATA_INIT(_changed, _write, _match)
```

相关声明：[BT_GATT_CCC_MANAGED_USER_DATA_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#gae3a23386bfe38e0127b74e0f4b5e5667)。

初始化客户端特征配置声明的宏（Initialize Client Characteristic Configuration Declaration Macro）。

<a id="r_gad8b296ecfd1139680f21da7904b9f585"></a>

```c
#define BT_GATT_CCC_MANAGED(_ccc, _perm)
```

相关声明：[BT_GATT_CCC_MANAGED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#gad8b296ecfd1139680f21da7904b9f585)。

托管客户端特征配置声明宏（Managed Client Characteristic Configuration Declaration Macro）。

<a id="r_ga140b9c25d10244bebd9c891f881fdc94"></a>

```c
#define BT_GATT_CCC(_changed, _perm)
```

相关声明：[BT_GATT_CCC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga140b9c25d10244bebd9c891f881fdc94)。

客户端特征配置声明宏（Client Characteristic Configuration Declaration Macro）。

<a id="r_ga9a6fa72eb2b6e9438ad677365c998428"></a>

```c
#define BT_GATT_CCC_WITH_WRITE_CB(_changed, _write, _perm)
```

相关声明：[BT_GATT_CCC_WITH_WRITE_CB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga9a6fa72eb2b6e9438ad677365c998428)。

带写回调的客户端特征配置声明宏（Client Characteristic Configuration Declaration Macro with Write Callback）。

<a id="r_ga55a82cada1093c4ff75fe5504ac504b1"></a>

```c
#define BT_GATT_CEP(_value)
```

相关声明：[BT_GATT_CEP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga55a82cada1093c4ff75fe5504ac504b1)。

特征扩展属性声明宏（Characteristic Extended Properties Declaration Macro）。

<a id="r_ga1e1cd9d0853e2dcbefcb85fda44dc9c7"></a>

```c
#define BT_GATT_CUD(_value, _perm)
```

相关声明：[BT_GATT_CUD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga1e1cd9d0853e2dcbefcb85fda44dc9c7)。

特征用户格式描述符声明宏（Characteristic User Format Descriptor Declaration Macro）。

<a id="r_ga3835fcfdf7a5f917e21c9d17e75162be"></a>

```c
#define BT_GATT_CPF(_value)
```

相关声明：[BT_GATT_CPF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga3835fcfdf7a5f917e21c9d17e75162be)。

特征呈现格式描述符声明宏（Characteristic Presentation Format Descriptor Declaration Macro）。

<a id="r_ga83207fc083454327004f7d3c3e5b3840"></a>

```c
#define BT_GATT_DESCRIPTOR(_uuid, _perm, _read, _write, _user_data)
```

相关声明：[BT_GATT_DESCRIPTOR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga83207fc083454327004f7d3c3e5b3840)。

描述符声明宏（Descriptor Declaration Macro）。

<a id="r_gac4abfeb068d16dcdaceee812c12bf406"></a>

```c
#define BT_GATT_ATTRIBUTE(_uuid, _perm, _read, _write, _user_data)
```

相关声明：[BT_GATT_ATTRIBUTE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#gac4abfeb068d16dcdaceee812c12bf406)。

属性声明宏（Attribute Declaration Macro）。

<a id="r_ga7ca44e95989a143ae0b21e4a5316561d"></a>

```c
#define BT_GATT_AUTO_DISCOVER_CCC_HANDLE 0x0000U
```

相关声明：[BT_GATT_AUTO_DISCOVER_CCC_HANDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ga7ca44e95989a143ae0b21e4a5316561d)。

用于表示自动发现客户端特征配置（CCC）的句柄值（Handle Value）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 4.3\_类型定义（Typedefs）

<a id="r_ga57e36bf94652531964fd4237c203fe7b"></a>

```c
typedef ssize_t(* bt_gatt_attr_read_func_t) (struct bt_conn *conn, const struct bt_gatt_attr *attr, void *buf, uint16_t len, uint16_t offset)
```

相关声明：[ssize_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)、[bt_gatt_attr_read_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#ga57e36bf94652531964fd4237c203fe7b)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_gatt_attr](../bluetooth_connection_model_reference/P049_bt_gatt_attr_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

属性读取回调（Attribute Read Callback）。

<a id="r_ga3fd8527a0f3e8f3699dc0d3b0339eba1"></a>

```c
typedef ssize_t(* bt_gatt_attr_write_func_t) (struct bt_conn *conn, const struct bt_gatt_attr *attr, const void *buf, uint16_t len, uint16_t offset, uint8_t flags)
```

相关声明：[ssize_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)、[bt_gatt_attr_write_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#ga3fd8527a0f3e8f3699dc0d3b0339eba1)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_gatt_attr](../bluetooth_connection_model_reference/P049_bt_gatt_attr_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

属性值写入实现（Attribute Value Write Implementation）。

<a id="r_ga60284611c90729b289fe806524ba9209"></a>

```c
typedef uint8_t(* bt_gatt_attr_func_t) (const struct bt_gatt_attr *attr, uint16_t handle, void *user_data)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_gatt_attr_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga60284611c90729b289fe806524ba9209)、[bt_gatt_attr](../bluetooth_connection_model_reference/P049_bt_gatt_attr_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

属性迭代器回调（Attribute Iterator Callback）。

<a id="r_gac55832607b95f394d26a64ed1cfe5bba"></a>

```c
typedef void(* bt_gatt_complete_func_t) (struct bt_conn *conn, void *user_data)
```

相关声明：[bt_gatt_complete_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#gac55832607b95f394d26a64ed1cfe5bba)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

通知完成结果回调（Notification Complete Result Callback）。

<a id="r_ga1294850e6bdcbe7a8f42f2956fd837a8"></a>

```c
typedef void(* bt_gatt_indicate_func_t) (struct bt_conn *conn, struct bt_gatt_indicate_params *params, uint8_t err)
```

相关声明：[bt_gatt_indicate_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga1294850e6bdcbe7a8f42f2956fd837a8)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_gatt_indicate_params](../bluetooth_connection_model_reference/P061_bt_gatt_indicate_params_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

指示完成结果回调（Indication Complete Result Callback）。

<a id="r_ga5d47ed9eaea22c8f00db14329daee8fe"></a>

```c
typedef void(* bt_gatt_indicate_params_destroy_t) (struct bt_gatt_indicate_params *params)
```

相关声明：[bt_gatt_indicate_params_destroy_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga5d47ed9eaea22c8f00db14329daee8fe)、[bt_gatt_indicate_params](../bluetooth_connection_model_reference/P061_bt_gatt_indicate_params_结构体.md)。

用于销毁或清理 GATT 指示值参数（Indicate Value Parameters）的回调。

<a id="r_gabd3bcd3c1560956726574faed332fb13"></a>

```c
typedef uint8_t(* bt_gatt_discover_func_t) (struct bt_conn *conn, const struct bt_gatt_attr *attr, struct bt_gatt_discover_params *params)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_gatt_discover_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#gabd3bcd3c1560956726574faed332fb13)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_gatt_attr](../bluetooth_connection_model_reference/P049_bt_gatt_attr_结构体.md)、[bt_gatt_discover_params](../bluetooth_connection_model_reference/P058_bt_gatt_discover_params_结构体.md)。

发现属性回调函数（Discover Attribute Callback Function）。

<a id="r_ga1ca94b4f2b6c456b6134e05127993569"></a>

```c
typedef uint8_t(* bt_gatt_read_func_t) (struct bt_conn *conn, uint8_t err, struct bt_gatt_read_params *params, const void *data, uint16_t length)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_gatt_read_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ga1ca94b4f2b6c456b6134e05127993569)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_gatt_read_params](../bluetooth_connection_model_reference/P063_bt_gatt_read_params_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

读取回调函数（Read Callback Function）。

<a id="r_ga2bca8c4a45f41e0400a9e0147f4baf50"></a>

```c
typedef void(* bt_gatt_write_func_t) (struct bt_conn *conn, uint8_t err, struct bt_gatt_write_params *params)
```

相关声明：[bt_gatt_write_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ga2bca8c4a45f41e0400a9e0147f4baf50)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_gatt_write_params](../bluetooth_connection_model_reference/P069_bt_gatt_write_params_结构体.md)。

写入回调函数（Write Callback Function）。

<a id="r_gab3e53eb5f9bb1eda7bf612ef95755b4d"></a>

```c
typedef uint8_t(* bt_gatt_notify_func_t) (struct bt_conn *conn, struct bt_gatt_subscribe_params *params, const void *data, uint16_t length)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_gatt_notify_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#gab3e53eb5f9bb1eda7bf612ef95755b4d)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_gatt_subscribe_params](../bluetooth_connection_model_reference/P068_bt_gatt_subscribe_params_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

通知回调函数（Notification Callback Function）。

<a id="r_ga2e914e63b4b91fa56bc3295283c43714"></a>

```c
typedef void(* bt_gatt_subscribe_func_t) (struct bt_conn *conn, uint8_t err, struct bt_gatt_subscribe_params *params)
```

相关声明：[bt_gatt_subscribe_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ga2e914e63b4b91fa56bc3295283c43714)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_gatt_subscribe_params](../bluetooth_connection_model_reference/P068_bt_gatt_subscribe_params_结构体.md)。

订阅回调函数（Subscription Callback Function）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 4.4\_枚举（Enumerations）

<a id="r_ga96e57500d2340a45badb23701cc43833"></a>

```c
enum bt_gatt_perm { BT_GATT_PERM_NONE = 0 , BT_GATT_PERM_READ = (1UL << (0)) , BT_GATT_PERM_WRITE = (1UL << (1)) , BT_GATT_PERM_READ_ENCRYPT = (1UL << (2)) , BT_GATT_PERM_WRITE_ENCRYPT = (1UL << (3)) , BT_GATT_PERM_READ_AUTHEN = (1UL << (4)) , BT_GATT_PERM_WRITE_AUTHEN = (1UL << (5)) , BT_GATT_PERM_PREPARE_WRITE = (1UL << (6)) , BT_GATT_PERM_READ_LESC = (1UL << (7)) , BT_GATT_PERM_WRITE_LESC = (1UL << (8)) }
```

相关声明：[bt_gatt_perm](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#ga96e57500d2340a45badb23701cc43833)、[BT_GATT_PERM_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#gga96e57500d2340a45badb23701cc43833a81a1c35d981593c4c0d344dd0f7e898a)、[BT_GATT_PERM_READ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#gga96e57500d2340a45badb23701cc43833a9afb838c2cef657e9cd035ef27521f17)、[BT_GATT_PERM_WRITE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#gga96e57500d2340a45badb23701cc43833a0f611698ca511f565b247a813ea016cf)、[BT_GATT_PERM_READ_ENCRYPT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#gga96e57500d2340a45badb23701cc43833a0d0afe4a6389102f85e355468cb7984d)、[BT_GATT_PERM_WRITE_ENCRYPT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#gga96e57500d2340a45badb23701cc43833a662b9af6f435d788aa4e6829725f670f)、[BT_GATT_PERM_READ_AUTHEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#gga96e57500d2340a45badb23701cc43833ad83f4c03608f674c00ebc93e63d08583)、[BT_GATT_PERM_WRITE_AUTHEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#gga96e57500d2340a45badb23701cc43833add3893c94a788ff2e5256595a533a266)、[BT_GATT_PERM_PREPARE_WRITE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#gga96e57500d2340a45badb23701cc43833ab384b61f6ead9d140011da917c950d79)、[BT_GATT_PERM_READ_LESC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#gga96e57500d2340a45badb23701cc43833af62e397dfd87fe763b9c9fc1d5072f57)、[BT_GATT_PERM_WRITE_LESC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#gga96e57500d2340a45badb23701cc43833ac56183af896e2a58439c625420efca94)。

GATT 属性权限位域值（Attribute Permission Bit Field Values）。

<a id="r_ga830d437c8d0757f53af1de6aa3031906"></a>

```c
enum bt_gatt_attr_write_flag { BT_GATT_WRITE_FLAG_PREPARE = (1UL << (0)) , BT_GATT_WRITE_FLAG_CMD = (1UL << (1)) , BT_GATT_WRITE_FLAG_EXECUTE = (1UL << (2)) }
```

相关声明：[bt_gatt_attr_write_flag](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#ga830d437c8d0757f53af1de6aa3031906)、[BT_GATT_WRITE_FLAG_PREPARE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#gga830d437c8d0757f53af1de6aa3031906a019cf6118a0cfacbfad20c1cc5838383)、[BT_GATT_WRITE_FLAG_CMD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#gga830d437c8d0757f53af1de6aa3031906a770df41b7d433e8ce349b19e4657ba78)、[BT_GATT_WRITE_FLAG_EXECUTE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#gga830d437c8d0757f53af1de6aa3031906ad4e8f43c03da10c15685bd1a0109708b)。

GATT 属性写入标志（Attribute Write Flags）。

<a id="r_gab38994257f53473e62e01eff8f236ee1"></a>

```c
enum bt_gatt_iter { BT_GATT_ITER_STOP = 0 , BT_GATT_ITER_CONTINUE }
```

相关声明：[bt_gatt_iter](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#gab38994257f53473e62e01eff8f236ee1)、[BT_GATT_ITER_STOP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ggab38994257f53473e62e01eff8f236ee1aa3f2a25e27c7065a2c7bb2a9ff09542e)、[BT_GATT_ITER_CONTINUE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ggab38994257f53473e62e01eff8f236ee1aea569feffa4815d3443e12be78c684f5)。

用作 bt_gatt_attr_func_t 和 bt_gatt_read_func_t 类型回调的返回值（Return Values）。

<a id="r_gaea89c65f17050820d54568f636b6554a"></a>

```c
enum bt_gatt_discover_type { BT_GATT_DISCOVER_PRIMARY , BT_GATT_DISCOVER_SECONDARY , BT_GATT_DISCOVER_INCLUDE , BT_GATT_DISCOVER_CHARACTERISTIC , BT_GATT_DISCOVER_DESCRIPTOR , BT_GATT_DISCOVER_ATTRIBUTE , BT_GATT_DISCOVER_STD_CHAR_DESC }
```

相关声明：[bt_gatt_discover_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#gaea89c65f17050820d54568f636b6554a)、[BT_GATT_DISCOVER_PRIMARY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ggaea89c65f17050820d54568f636b6554aada9ac33aa77f6043da8133dcf269478f)、[BT_GATT_DISCOVER_SECONDARY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ggaea89c65f17050820d54568f636b6554aa21be62548b816c7960a54dd6e3b37a97)、[BT_GATT_DISCOVER_INCLUDE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ggaea89c65f17050820d54568f636b6554aa80afff1c83bb5ebb5603af699f2c26da)、[BT_GATT_DISCOVER_CHARACTERISTIC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ggaea89c65f17050820d54568f636b6554aa71355dfe0bf30c88f9fe2f7da1ba10ae)、[BT_GATT_DISCOVER_DESCRIPTOR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ggaea89c65f17050820d54568f636b6554aa0ccb2587aa8f21361c5d73847a33ecbe)、[BT_GATT_DISCOVER_ATTRIBUTE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ggaea89c65f17050820d54568f636b6554aafe2167b873b848935d56f6ee7f2c444c)、[BT_GATT_DISCOVER_STD_CHAR_DESC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ggaea89c65f17050820d54568f636b6554aa81a1f8737c415544a0f793f4e626bb61)。

GATT 发现类型（Discover Types）。

<a id="r_gaa43f45658809908baa72bf4e0ea745ac"></a>

```c
enum bt_gatt_sub_flag { BT_GATT_SUBSCRIBE_FLAG_VOLATILE , BT_GATT_SUBSCRIBE_FLAG_NO_RESUB , BT_GATT_SUBSCRIBE_FLAG_WRITE_PENDING , BT_GATT_SUBSCRIBE_FLAG_SENT , BT_GATT_SUBSCRIBE_NUM_FLAGS }
```

相关声明：[bt_gatt_sub_flag](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#gaa43f45658809908baa72bf4e0ea745ac)、[BT_GATT_SUBSCRIBE_FLAG_VOLATILE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ggaa43f45658809908baa72bf4e0ea745acaecdcb3baa850505f459523091c92a1cb)、[BT_GATT_SUBSCRIBE_FLAG_NO_RESUB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ggaa43f45658809908baa72bf4e0ea745aca30bfd3fb4bf4f17653ba00942ba2b2e6)、[BT_GATT_SUBSCRIBE_FLAG_WRITE_PENDING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ggaa43f45658809908baa72bf4e0ea745acafe1c3dc9380c33debd32a275d5bce8ad)、[BT_GATT_SUBSCRIBE_FLAG_SENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ggaa43f45658809908baa72bf4e0ea745aca56aa5f332d4098e3942d7a902198f7ab)、[BT_GATT_SUBSCRIBE_NUM_FLAGS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ggaa43f45658809908baa72bf4e0ea745aca5640a1e06740a89859c5f4b183d58e79)。

订阅标志（Subscription Flags）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 4.5\_函数（Functions）

<a id="r_gaf6d3f1e904f1a847afeb30236bad98a2"></a>

```c
static const char * bt_gatt_err_to_str (int gatt_err)
```

相关声明：[bt_gatt_err_to_str](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#gaf6d3f1e904f1a847afeb30236bad98a2)。

将 GATT 错误转换为字符串（String）。

<a id="r_ga270c8a52bf3d512defc373f8c29b59f2"></a>

```c
void bt_gatt_cb_register (struct bt_gatt_cb *cb)
```

相关声明：[bt_gatt_cb_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga270c8a52bf3d512defc373f8c29b59f2)、[bt_gatt_cb](../bluetooth_connection_model_reference/P051_bt_gatt_cb_结构体.md)。

注册 GATT 回调（Callbacks）。

<a id="r_ga5fb25c5eec91045dc4c7fd61ef7e528e"></a>

```c
int bt_gatt_cb_unregister (struct bt_gatt_cb *cb)
```

相关声明：[bt_gatt_cb_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga5fb25c5eec91045dc4c7fd61ef7e528e)、[bt_gatt_cb](../bluetooth_connection_model_reference/P051_bt_gatt_cb_结构体.md)。

注销 GATT 回调（Callbacks）。

<a id="r_ga5eee6afc6db391ffeda295d298bf6a56"></a>

```c
int bt_gatt_authorization_cb_register (const struct bt_gatt_authorization_cb *cb)
```

相关声明：[bt_gatt_authorization_cb_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga5eee6afc6db391ffeda295d298bf6a56)、[bt_gatt_authorization_cb](../bluetooth_connection_model_reference/P050_bt_gatt_authorization_cb_结构体.md)。

注册 GATT 授权回调（Authorization Callbacks）。

<a id="r_gab4d9cfea04e44445d5dc30ad52842b64"></a>

```c
int bt_gatt_service_register (struct bt_gatt_service *svc)
```

相关声明：[bt_gatt_service_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#gab4d9cfea04e44445d5dc30ad52842b64)、[bt_gatt_service](../bluetooth_connection_model_reference/P065_bt_gatt_service_结构体.md)。

注册 GATT 服务（Service）。

<a id="r_gaf5bf0205fad5f7ad187b764d23deba6b"></a>

```c
int bt_gatt_service_unregister (struct bt_gatt_service *svc)
```

相关声明：[bt_gatt_service_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#gaf5bf0205fad5f7ad187b764d23deba6b)、[bt_gatt_service](../bluetooth_connection_model_reference/P065_bt_gatt_service_结构体.md)。

注销 GATT 服务（Service）。

<a id="r_gae5c1e8b7bb1e673e228f03d1d084be9a"></a>

```c
bool bt_gatt_service_is_registered (const struct bt_gatt_service *svc)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_gatt_service_is_registered](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#gae5c1e8b7bb1e673e228f03d1d084be9a)、[bt_gatt_service](../bluetooth_connection_model_reference/P065_bt_gatt_service_结构体.md)。

检查 GATT 服务（Service）是否已注册。

<a id="r_gad8d8f513004f391167212d7bf9f7ff10"></a>

```c
void bt_gatt_foreach_attr_type (uint16_t start_handle, uint16_t end_handle, const struct bt_uuid *uuid, const void *attr_data, uint16_t num_matches, bt_gatt_attr_func_t func, void *user_data)
```

相关声明：[bt_gatt_foreach_attr_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#gad8d8f513004f391167212d7bf9f7ff10)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_uuid](../bluetooth_connection_model_reference/P131_bt_uuid_结构体.md)、[uuid](../data_utilities/P026_UUID二进制结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_gatt_attr_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga60284611c90729b289fe806524ba9209)。

按类型遍历的属性迭代器（Attribute Iterator by Type）。

<a id="r_gaa93b5e0f2870ed135447bead903c175a"></a>

```c
static void bt_gatt_foreach_attr (uint16_t start_handle, uint16_t end_handle, bt_gatt_attr_func_t func, void *user_data)
```

相关声明：[bt_gatt_foreach_attr](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#gaa93b5e0f2870ed135447bead903c175a)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_gatt_attr_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga60284611c90729b289fe806524ba9209)。

属性迭代器（Attribute Iterator）。

<a id="r_ga35cecaa43b00b374062d29cca1479d85"></a>

```c
struct bt_gatt_attr * bt_gatt_attr_next (const struct bt_gatt_attr *attr)
```

相关声明：[bt_gatt_attr](../bluetooth_connection_model_reference/P049_bt_gatt_attr_结构体.md)、[bt_gatt_attr_next](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga35cecaa43b00b374062d29cca1479d85)、[bt_gatt_attr](../bluetooth_connection_model_reference/P049_bt_gatt_attr_结构体.md)。

迭代到下一个属性（Attribute）。

<a id="r_gad2f3272b1dc42378104b492ec7caf6b0"></a>

```c
struct bt_gatt_attr * bt_gatt_find_by_uuid (const struct bt_gatt_attr *attr, uint16_t attr_count, const struct bt_uuid *uuid)
```

相关声明：[bt_gatt_attr](../bluetooth_connection_model_reference/P049_bt_gatt_attr_结构体.md)、[bt_gatt_find_by_uuid](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#gad2f3272b1dc42378104b492ec7caf6b0)、[bt_gatt_attr](../bluetooth_connection_model_reference/P049_bt_gatt_attr_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_uuid](../bluetooth_connection_model_reference/P131_bt_uuid_结构体.md)、[uuid](../data_utilities/P026_UUID二进制结构.md)。

按 UUID 查找属性（Attribute）。

<a id="r_ga2d51136ea1bd6cdb50900639506fd9f7"></a>

```c
uint16_t bt_gatt_attr_get_handle (const struct bt_gatt_attr *attr)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_gatt_attr_get_handle](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga2d51136ea1bd6cdb50900639506fd9f7)、[bt_gatt_attr](../bluetooth_connection_model_reference/P049_bt_gatt_attr_结构体.md)。

获取属性句柄（Attribute Handle）。

<a id="r_ga99738cf4f05eae4c6da17cc3420827d8"></a>

```c
uint16_t bt_gatt_attr_value_handle (const struct bt_gatt_attr *attr)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_gatt_attr_value_handle](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga99738cf4f05eae4c6da17cc3420827d8)、[bt_gatt_attr](../bluetooth_connection_model_reference/P049_bt_gatt_attr_结构体.md)。

获取特征值描述符（Characteristic Value Descriptor）的句柄。

<a id="r_gaf6d253849932b706ec7f303568980dfa"></a>

```c
ssize_t bt_gatt_attr_read (struct bt_conn *conn, const struct bt_gatt_attr *attr, void *buf, uint16_t buf_len, uint16_t offset, const void *value, uint16_t value_len)
```

相关声明：[ssize_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)、[bt_gatt_attr_read](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#gaf6d253849932b706ec7f303568980dfa)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_gatt_attr](../bluetooth_connection_model_reference/P049_bt_gatt_attr_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

通用属性值读取辅助函数（Generic Read Attribute Value Helper）。

<a id="r_gacae81c0f272bad7e6ac93c0d13b678c6"></a>

```c
ssize_t bt_gatt_attr_read_service (struct bt_conn *conn, const struct bt_gatt_attr *attr, void *buf, uint16_t len, uint16_t offset)
```

相关声明：[ssize_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)、[bt_gatt_attr_read_service](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#gacae81c0f272bad7e6ac93c0d13b678c6)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_gatt_attr](../bluetooth_connection_model_reference/P049_bt_gatt_attr_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

服务属性读取辅助函数（Read Service Attribute Helper）。

<a id="r_ga4313a63decac2c8b7c4a1764df3d53ea"></a>

```c
ssize_t bt_gatt_attr_read_included (struct bt_conn *conn, const struct bt_gatt_attr *attr, void *buf, uint16_t len, uint16_t offset)
```

相关声明：[ssize_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)、[bt_gatt_attr_read_included](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga4313a63decac2c8b7c4a1764df3d53ea)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_gatt_attr](../bluetooth_connection_model_reference/P049_bt_gatt_attr_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

包含属性读取辅助函数（Read Include Attribute Helper）。

<a id="r_gad58b526a06334530c13292d14a11257c"></a>

```c
ssize_t bt_gatt_attr_read_chrc (struct bt_conn *conn, const struct bt_gatt_attr *attr, void *buf, uint16_t len, uint16_t offset)
```

相关声明：[ssize_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)、[bt_gatt_attr_read_chrc](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#gad58b526a06334530c13292d14a11257c)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_gatt_attr](../bluetooth_connection_model_reference/P049_bt_gatt_attr_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

特征属性读取辅助函数（Read Characteristic Attribute Helper）。

<a id="r_ga2e85b42136e2c6a4cb5b7ad8a2532573"></a>

```c
ssize_t bt_gatt_attr_read_ccc (struct bt_conn *conn, const struct bt_gatt_attr *attr, void *buf, uint16_t len, uint16_t offset)
```

相关声明：[ssize_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)、[bt_gatt_attr_read_ccc](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga2e85b42136e2c6a4cb5b7ad8a2532573)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_gatt_attr](../bluetooth_connection_model_reference/P049_bt_gatt_attr_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

客户端特征配置属性读取辅助函数（Read Client Characteristic Configuration Attribute Helper）。

<a id="r_gabba965b676650a55cb9934072b34c75e"></a>

```c
ssize_t bt_gatt_attr_write_ccc (struct bt_conn *conn, const struct bt_gatt_attr *attr, const void *buf, uint16_t len, uint16_t offset, uint8_t flags)
```

相关声明：[ssize_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)、[bt_gatt_attr_write_ccc](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#gabba965b676650a55cb9934072b34c75e)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_gatt_attr](../bluetooth_connection_model_reference/P049_bt_gatt_attr_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

客户端特征配置属性写入辅助函数（Write Client Characteristic Configuration Attribute Helper）。

<a id="r_ga5893166f1b24f437a94ccf1fc57c7917"></a>

```c
ssize_t bt_gatt_attr_read_cep (struct bt_conn *conn, const struct bt_gatt_attr *attr, void *buf, uint16_t len, uint16_t offset)
```

相关声明：[ssize_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)、[bt_gatt_attr_read_cep](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga5893166f1b24f437a94ccf1fc57c7917)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_gatt_attr](../bluetooth_connection_model_reference/P049_bt_gatt_attr_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

特征扩展属性读取辅助函数（Read Characteristic Extended Properties Attribute Helper）。

<a id="r_ga29421c8788b47b6a648704d27d5f0d28"></a>

```c
ssize_t bt_gatt_attr_read_cud (struct bt_conn *conn, const struct bt_gatt_attr *attr, void *buf, uint16_t len, uint16_t offset)
```

相关声明：[ssize_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)、[bt_gatt_attr_read_cud](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga29421c8788b47b6a648704d27d5f0d28)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_gatt_attr](../bluetooth_connection_model_reference/P049_bt_gatt_attr_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

特征用户描述描述符属性读取辅助函数（Read Characteristic User Description Descriptor Attribute Helper）。

<a id="r_ga5ae96590a0aaa5c4c3863a4a14d80fdd"></a>

```c
ssize_t bt_gatt_attr_read_cpf (struct bt_conn *conn, const struct bt_gatt_attr *attr, void *buf, uint16_t len, uint16_t offset)
```

相关声明：[ssize_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)、[bt_gatt_attr_read_cpf](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga5ae96590a0aaa5c4c3863a4a14d80fdd)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_gatt_attr](../bluetooth_connection_model_reference/P049_bt_gatt_attr_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

特征呈现格式描述符属性读取辅助函数（Read Characteristic Presentation Format Descriptor Attribute Helper）。

<a id="r_ga55e3ef7cb43b8acb0a27643c78390146"></a>

```c
int bt_gatt_notify_cb (struct bt_conn *conn, struct bt_gatt_notify_params *params)
```

相关声明：[bt_gatt_notify_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga55e3ef7cb43b8acb0a27643c78390146)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_gatt_notify_params](../bluetooth_connection_model_reference/P062_bt_gatt_notify_params_结构体.md)。

发送属性值变化通知（Notify Attribute Value Change）。

<a id="r_ga8071d6063f85c0a78155f6b2ac2da635"></a>

```c
int bt_gatt_notify_multiple (struct bt_conn *conn, uint16_t num_params, struct bt_gatt_notify_params params[])
```

相关声明：[bt_gatt_notify_multiple](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga8071d6063f85c0a78155f6b2ac2da635)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_gatt_notify_params](../bluetooth_connection_model_reference/P062_bt_gatt_notify_params_结构体.md)。

在一个协议数据单元（PDU）中发送多个通知（Notifications）。

<a id="r_ga74ee552864c563aa5bc939f37395c14a"></a>

```c
static int bt_gatt_notify (struct bt_conn *conn, const struct bt_gatt_attr *attr, const void *data, uint16_t len)
```

相关声明：[bt_gatt_notify](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga74ee552864c563aa5bc939f37395c14a)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_gatt_attr](../bluetooth_connection_model_reference/P049_bt_gatt_attr_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

发送属性值变化通知（Notify Attribute Value Change）。

<a id="r_ga24bae284dbc71cd4075649c4bc348b7c"></a>

```c
static int bt_gatt_notify_uuid (struct bt_conn *conn, const struct bt_uuid *uuid, const struct bt_gatt_attr *attr, const void *data, uint16_t len)
```

相关声明：[bt_gatt_notify_uuid](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga24bae284dbc71cd4075649c4bc348b7c)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_uuid](../bluetooth_connection_model_reference/P131_bt_uuid_结构体.md)、[uuid](../data_utilities/P026_UUID二进制结构.md)、[bt_gatt_attr](../bluetooth_connection_model_reference/P049_bt_gatt_attr_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

按 UUID 发送属性值变化通知（Notify Attribute Value Change）。

<a id="r_ga4f2272692cc0f1d44638828012296c80"></a>

```c
int bt_gatt_indicate (struct bt_conn *conn, struct bt_gatt_indicate_params *params)
```

相关声明：[bt_gatt_indicate](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga4f2272692cc0f1d44638828012296c80)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_gatt_indicate_params](../bluetooth_connection_model_reference/P061_bt_gatt_indicate_params_结构体.md)。

发送属性值变化指示（Indicate Attribute Value Change）。

<a id="r_gabd4df0a264dae10e43797992a567be7d"></a>

```c
bool bt_gatt_is_subscribed (struct bt_conn *conn, const struct bt_gatt_attr *attr, uint16_t ccc_type)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_gatt_is_subscribed](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#gabd4df0a264dae10e43797992a567be7d)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_gatt_attr](../bluetooth_connection_model_reference/P049_bt_gatt_attr_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

检查连接是否已订阅（Subscribed）该属性。

<a id="r_ga351fd7658eaecbbfa60f1769119ef733"></a>

```c
uint16_t bt_gatt_get_mtu (struct bt_conn *conn)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_gatt_get_mtu](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga351fd7658eaecbbfa60f1769119ef733)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

获取连接的 ATT 最大传输单元（MTU）。

<a id="r_ga6653de5e245cae6dc12cd0b45acbe028"></a>

```c
uint16_t bt_gatt_get_uatt_mtu (struct bt_conn *conn)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_gatt_get_uatt_mtu](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga6653de5e245cae6dc12cd0b45acbe028)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

获取连接的非增强属性协议（Unenhanced ATT，UATT）的 MTU。

<a id="r_ga0f41da23c6559a8254b04295aff8198d"></a>

```c
int bt_gatt_exchange_mtu (struct bt_conn *conn, struct bt_gatt_exchange_params *params)
```

相关声明：[bt_gatt_exchange_mtu](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ga0f41da23c6559a8254b04295aff8198d)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_gatt_exchange_params](../bluetooth_connection_model_reference/P059_bt_gatt_exchange_params_结构体.md)。

交换最大传输单元（MTU）。

<a id="r_gac06a945e5f7939b6716bc4f2cea781bd"></a>

```c
int bt_gatt_discover (struct bt_conn *conn, struct bt_gatt_discover_params *params)
```

相关声明：[bt_gatt_discover](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#gac06a945e5f7939b6716bc4f2cea781bd)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_gatt_discover_params](../bluetooth_connection_model_reference/P058_bt_gatt_discover_params_结构体.md)。

GATT 发现函数（Discover Function）。

<a id="r_ga1a18dd726ab960a88d7f85f2a014141a"></a>

```c
int bt_gatt_read (struct bt_conn *conn, struct bt_gatt_read_params *params)
```

相关声明：[bt_gatt_read](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ga1a18dd726ab960a88d7f85f2a014141a)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_gatt_read_params](../bluetooth_connection_model_reference/P063_bt_gatt_read_params_结构体.md)。

按句柄读取属性值（Attribute Value）。

<a id="r_ga843a42e68e0497d88d3f655f8ffd58d4"></a>

```c
int bt_gatt_write (struct bt_conn *conn, struct bt_gatt_write_params *params)
```

相关声明：[bt_gatt_write](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ga843a42e68e0497d88d3f655f8ffd58d4)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_gatt_write_params](../bluetooth_connection_model_reference/P069_bt_gatt_write_params_结构体.md)。

按句柄写入属性值（Attribute Value）。

<a id="r_ga49439413d12b5a8a1c68735e961ab6fa"></a>

```c
int bt_gatt_write_without_response_cb (struct bt_conn *conn, uint16_t handle, const void *data, uint16_t length, bool sign, bt_gatt_complete_func_t func, void *user_data)
```

相关声明：[bt_gatt_write_without_response_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ga49439413d12b5a8a1c68735e961ab6fa)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_gatt_complete_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#gac55832607b95f394d26a64ed1cfe5bba)。

按句柄执行无响应属性值写入（Write Without Response），带回调。

<a id="r_ga9fc78e32230637a6f092da2400c50fe7"></a>

```c
static int bt_gatt_write_without_response (struct bt_conn *conn, uint16_t handle, const void *data, uint16_t length, bool sign)
```

相关声明：[bt_gatt_write_without_response](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ga9fc78e32230637a6f092da2400c50fe7)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

按句柄执行无响应属性值写入（Write Without Response）。

<a id="r_ga7d4a8e18f51ba6476886a15f81f48e5c"></a>

```c
int bt_gatt_subscribe (struct bt_conn *conn, struct bt_gatt_subscribe_params *params)
```

相关声明：[bt_gatt_subscribe](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ga7d4a8e18f51ba6476886a15f81f48e5c)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_gatt_subscribe_params](../bluetooth_connection_model_reference/P068_bt_gatt_subscribe_params_结构体.md)。

订阅属性值通知（Attribute Value Notification）。

<a id="r_ga791b8bb8a4c085b022fafc0535a63511"></a>

```c
int bt_gatt_resubscribe (uint8_t id, const bt_addr_le_t *peer, struct bt_gatt_subscribe_params *params)
```

相关声明：[bt_gatt_resubscribe](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ga791b8bb8a4c085b022fafc0535a63511)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[bt_gatt_subscribe_params](../bluetooth_connection_model_reference/P068_bt_gatt_subscribe_params_结构体.md)。

重新订阅属性值通知（Attribute Value Notification）。

<a id="r_ga56509c9b8f73f729cfa5e75be22d79ae"></a>

```c
int bt_gatt_unsubscribe (struct bt_conn *conn, struct bt_gatt_subscribe_params *params)
```

相关声明：[bt_gatt_unsubscribe](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ga56509c9b8f73f729cfa5e75be22d79ae)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_gatt_subscribe_params](../bluetooth_connection_model_reference/P068_bt_gatt_subscribe_params_结构体.md)。

取消订阅属性值通知（Attribute Value Notification）。

<a id="r_ga5193dea59a016692f94cf950d6b4f4f7"></a>

```c
void bt_gatt_cancel (struct bt_conn *conn, void *params)
```

相关声明：[bt_gatt_cancel](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ga5193dea59a016692f94cf950d6b4f4f7)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

尝试取消 params 标识的第一个待处理请求（Pending Request）。


## 4.6\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [string.h](../api_source_supplement_reference/P216_string.h_源码浏览.md)
- [sys/types.h](../api_source_runtime_reference/P038_types.h_源码浏览.md)
- [zephyr/bluetooth/addr.h](../api_source_visible_fragment_reference/P001_addr.h_源码浏览.md)
- [zephyr/bluetooth/conn.h](../api_source_register_time_reference/P002_conn.h_源码浏览.md)
- [zephyr/bluetooth/uuid.h](../api_source_supplement_reference/P020_uuid.h_源码浏览.md)
- [zephyr/bluetooth/att.h](../api_source_system_reference/P001_att.h_源码浏览.md)
- [zephyr/sys/atomic.h](../atomic_reference/P003_原子操作公共头文件源码.md)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P003_可遍历段辅助头文件源码.md)
- [zephyr/sys/slist.h](../slist_reference/P003_单向链表头文件源码.md)
- [zephyr/sys/util.h](../util_reference/P003_通用工具头文件源码.md)
- [zephyr/sys/util_macro.h](../util_reference/P005_宏工具头文件源码.md)
- [zephyr/toolchain.h](../api_source_compiler_device_reference/P023_toolchain.h_源码浏览.md)
- [查看此文件的源码。](../api_source_runtime_reference/P021_gatt.h_源码浏览.md)
- [bt_gatt_attr](../bluetooth_connection_model_reference/P049_bt_gatt_attr_结构体.md)
- [bt_gatt_service_static](../bluetooth_connection_model_reference/P066_bt_gatt_service_static_结构体.md)
- [bt_gatt_service](../bluetooth_connection_model_reference/P065_bt_gatt_service_结构体.md)
- [bt_gatt_service_val](../bluetooth_connection_model_reference/P067_bt_gatt_service_val_结构体.md)
- [bt_gatt_include](../bluetooth_connection_model_reference/P060_bt_gatt_include_结构体.md)
- [bt_gatt_cb](../bluetooth_connection_model_reference/P051_bt_gatt_cb_结构体.md)
- [bt_gatt_authorization_cb](../bluetooth_connection_model_reference/P050_bt_gatt_authorization_cb_结构体.md)
- [bt_gatt_chrc](../bluetooth_connection_model_reference/P056_bt_gatt_chrc_结构体.md)
- [bt_gatt_cep](../bluetooth_connection_model_reference/P055_bt_gatt_cep_结构体.md)
- [bt_gatt_ccc](../bluetooth_connection_model_reference/P052_bt_gatt_ccc_结构体.md)
- [bt_gatt_scc](../bluetooth_connection_model_reference/P064_bt_gatt_scc_结构体.md)
- [bt_gatt_cpf](../bluetooth_connection_model_reference/P057_bt_gatt_cpf_结构体.md)
- [bt_gatt_ccc_cfg](../bluetooth_connection_model_reference/P053_bt_gatt_ccc_cfg_结构体.md)
- [bt_gatt_ccc_managed_user_data](../bluetooth_connection_model_reference/P054_bt_gatt_ccc_managed_user_data_结构体.md)
- [bt_gatt_notify_params](../bluetooth_connection_model_reference/P062_bt_gatt_notify_params_结构体.md)
- [bt_gatt_indicate_params](../bluetooth_connection_model_reference/P061_bt_gatt_indicate_params_结构体.md)
- [bt_gatt_exchange_params](../bluetooth_connection_model_reference/P059_bt_gatt_exchange_params_结构体.md)
- [bt_gatt_discover_params](../bluetooth_connection_model_reference/P058_bt_gatt_discover_params_结构体.md)
- [bt_gatt_read_params](../bluetooth_connection_model_reference/P063_bt_gatt_read_params_结构体.md)
- [bt_gatt_write_params](../bluetooth_connection_model_reference/P069_bt_gatt_write_params_结构体.md)
- [bt_gatt_subscribe_params](../bluetooth_connection_model_reference/P068_bt_gatt_subscribe_params_结构体.md)
- [BT_GATT_ERR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#gaff31756c1bf8ee755e65b1e0fb689bb7)
- [BT_GATT_CHRC_BROADCAST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#ga86bddd8211e7466b0457173a0dd412f0)
- [BT_GATT_CHRC_READ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#gaa243a11d6d8b3e3be815c0893e0220f3)
- [BT_GATT_CHRC_WRITE_WITHOUT_RESP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#ga9c029ca574eb3c5992685b279388ac85)
- [BT_GATT_CHRC_WRITE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#gad482d8db34707e1f9da1d8e2ddd5507e)
- [BT_GATT_CHRC_NOTIFY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#gab8cd9649bdfd125a26065a8ced762a98)
- [BT_GATT_CHRC_INDICATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#gaa9639b9d655ea41767584b638add1f2b)
- [BT_GATT_CHRC_AUTH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#gaab3a26a00f88a6eacd36f2841004204c)
- [BT_GATT_CHRC_EXT_PROP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#gac84d73a0ad50bfd149ad83181315de1a)
- [BT_GATT_CEP_RELIABLE_WRITE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#gad1825f8deafc36d7e8f09c2835884fc6)
- [BT_GATT_CEP_WRITABLE_AUX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#ga64898ec8390c89c1fc5bdf0364220a43)
- [BT_GATT_CCC_NOTIFY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#ga240a10df32aa7a256a103ceee7211f8d)
- [BT_GATT_CCC_INDICATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#ga60ff2ddcc2e3148881a2f15745ba06e8)
- [BT_GATT_SCC_BROADCAST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#ga7a7d3cfa6eec4baa0b57ec9c4bc41f7a)
- [BT_GATT_SERVICE_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga04c7887fb67107bd060dd023fd3186d5)
- [BT_GATT_SERVICE_INSTANCE_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga8bb3aeef20465d7f6e38f6bbddef74e5)
- [BT_GATT_SERVICE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga7d413ec013b91a633ec24d80d2814e2b)
- [BT_GATT_PRIMARY_SERVICE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#gaacada0ff1029af959b6fcd6703d4a0bf)
- [BT_GATT_SECONDARY_SERVICE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#gaecb4d30282677d3450ad79c5f83f3445)
- [BT_GATT_INCLUDE_SERVICE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga08ffee706d271b75a54b1b99249dba24)
- [BT_GATT_CHRC_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga7f19592a722c41d6c1d2421d166dd78a)
- [BT_GATT_CHARACTERISTIC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga9e739546dbd906d3b3c4f1ed5ad9f41e)
- [BT_GATT_CCC_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#gac1c0a195c1ec1ff2cdd5bf6d0ba6ad00)
- [CONFIG_BT_SETTINGS_CCC_LAZY_LOADING](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SETTINGS_CCC_LAZY_LOADING)
- [CONFIG_BT_CONN](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CONN)
- [BT_GATT_CCC_MANAGED_USER_DATA_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#gae3a23386bfe38e0127b74e0f4b5e5667)
- [BT_GATT_CCC_MANAGED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#gad8b296ecfd1139680f21da7904b9f585)
- [BT_GATT_CCC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga140b9c25d10244bebd9c891f881fdc94)
- [BT_GATT_CCC_WITH_WRITE_CB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga9a6fa72eb2b6e9438ad677365c998428)
- [BT_GATT_CEP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga55a82cada1093c4ff75fe5504ac504b1)
- [BT_GATT_CUD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga1e1cd9d0853e2dcbefcb85fda44dc9c7)
- [BT_GATT_CPF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga3835fcfdf7a5f917e21c9d17e75162be)
- [BT_GATT_DESCRIPTOR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga83207fc083454327004f7d3c3e5b3840)
- [BT_GATT_ATTRIBUTE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#gac4abfeb068d16dcdaceee812c12bf406)
- [BT_GATT_AUTO_DISCOVER_CCC_HANDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ga7ca44e95989a143ae0b21e4a5316561d)
- [ssize_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)
- [bt_gatt_attr_read_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#ga57e36bf94652531964fd4237c203fe7b)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_gatt_attr_write_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#ga3fd8527a0f3e8f3699dc0d3b0339eba1)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [bt_gatt_attr_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga60284611c90729b289fe806524ba9209)
- [bt_gatt_complete_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#gac55832607b95f394d26a64ed1cfe5bba)
- [bt_gatt_indicate_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga1294850e6bdcbe7a8f42f2956fd837a8)
- [bt_gatt_indicate_params_destroy_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga5d47ed9eaea22c8f00db14329daee8fe)
- [bt_gatt_discover_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#gabd3bcd3c1560956726574faed332fb13)
- [bt_gatt_read_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ga1ca94b4f2b6c456b6134e05127993569)
- [bt_gatt_write_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ga2bca8c4a45f41e0400a9e0147f4baf50)
- [bt_gatt_notify_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#gab3e53eb5f9bb1eda7bf612ef95755b4d)
- [bt_gatt_subscribe_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ga2e914e63b4b91fa56bc3295283c43714)
- [bt_gatt_perm](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#ga96e57500d2340a45badb23701cc43833)
- [BT_GATT_PERM_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#gga96e57500d2340a45badb23701cc43833a81a1c35d981593c4c0d344dd0f7e898a)
- [BT_GATT_PERM_READ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#gga96e57500d2340a45badb23701cc43833a9afb838c2cef657e9cd035ef27521f17)
- [BT_GATT_PERM_WRITE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#gga96e57500d2340a45badb23701cc43833a0f611698ca511f565b247a813ea016cf)
- [BT_GATT_PERM_READ_ENCRYPT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#gga96e57500d2340a45badb23701cc43833a0d0afe4a6389102f85e355468cb7984d)
- [BT_GATT_PERM_WRITE_ENCRYPT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#gga96e57500d2340a45badb23701cc43833a662b9af6f435d788aa4e6829725f670f)
- [BT_GATT_PERM_READ_AUTHEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#gga96e57500d2340a45badb23701cc43833ad83f4c03608f674c00ebc93e63d08583)
- [BT_GATT_PERM_WRITE_AUTHEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#gga96e57500d2340a45badb23701cc43833add3893c94a788ff2e5256595a533a266)
- [BT_GATT_PERM_PREPARE_WRITE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#gga96e57500d2340a45badb23701cc43833ab384b61f6ead9d140011da917c950d79)
- [BT_GATT_PERM_READ_LESC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#gga96e57500d2340a45badb23701cc43833af62e397dfd87fe763b9c9fc1d5072f57)
- [BT_GATT_PERM_WRITE_LESC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#gga96e57500d2340a45badb23701cc43833ac56183af896e2a58439c625420efca94)
- [bt_gatt_attr_write_flag](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#ga830d437c8d0757f53af1de6aa3031906)
- [BT_GATT_WRITE_FLAG_PREPARE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#gga830d437c8d0757f53af1de6aa3031906a019cf6118a0cfacbfad20c1cc5838383)
- [BT_GATT_WRITE_FLAG_CMD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#gga830d437c8d0757f53af1de6aa3031906a770df41b7d433e8ce349b19e4657ba78)
- [BT_GATT_WRITE_FLAG_EXECUTE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#gga830d437c8d0757f53af1de6aa3031906ad4e8f43c03da10c15685bd1a0109708b)
- [bt_gatt_iter](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#gab38994257f53473e62e01eff8f236ee1)
- [BT_GATT_ITER_STOP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ggab38994257f53473e62e01eff8f236ee1aa3f2a25e27c7065a2c7bb2a9ff09542e)
- [BT_GATT_ITER_CONTINUE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ggab38994257f53473e62e01eff8f236ee1aea569feffa4815d3443e12be78c684f5)
- [bt_gatt_discover_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#gaea89c65f17050820d54568f636b6554a)
- [BT_GATT_DISCOVER_PRIMARY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ggaea89c65f17050820d54568f636b6554aada9ac33aa77f6043da8133dcf269478f)
- [BT_GATT_DISCOVER_SECONDARY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ggaea89c65f17050820d54568f636b6554aa21be62548b816c7960a54dd6e3b37a97)
- [BT_GATT_DISCOVER_INCLUDE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ggaea89c65f17050820d54568f636b6554aa80afff1c83bb5ebb5603af699f2c26da)
- [BT_GATT_DISCOVER_CHARACTERISTIC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ggaea89c65f17050820d54568f636b6554aa71355dfe0bf30c88f9fe2f7da1ba10ae)
- [BT_GATT_DISCOVER_DESCRIPTOR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ggaea89c65f17050820d54568f636b6554aa0ccb2587aa8f21361c5d73847a33ecbe)
- [BT_GATT_DISCOVER_ATTRIBUTE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ggaea89c65f17050820d54568f636b6554aafe2167b873b848935d56f6ee7f2c444c)
- [BT_GATT_DISCOVER_STD_CHAR_DESC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ggaea89c65f17050820d54568f636b6554aa81a1f8737c415544a0f793f4e626bb61)
- [bt_gatt_sub_flag](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#gaa43f45658809908baa72bf4e0ea745ac)
- [BT_GATT_SUBSCRIBE_FLAG_VOLATILE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ggaa43f45658809908baa72bf4e0ea745acaecdcb3baa850505f459523091c92a1cb)
- [BT_GATT_SUBSCRIBE_FLAG_NO_RESUB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ggaa43f45658809908baa72bf4e0ea745aca30bfd3fb4bf4f17653ba00942ba2b2e6)
- [BT_GATT_SUBSCRIBE_FLAG_WRITE_PENDING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ggaa43f45658809908baa72bf4e0ea745acafe1c3dc9380c33debd32a275d5bce8ad)
- [BT_GATT_SUBSCRIBE_FLAG_SENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ggaa43f45658809908baa72bf4e0ea745aca56aa5f332d4098e3942d7a902198f7ab)
- [BT_GATT_SUBSCRIBE_NUM_FLAGS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ggaa43f45658809908baa72bf4e0ea745aca5640a1e06740a89859c5f4b183d58e79)
- [bt_gatt_err_to_str](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#gaf6d3f1e904f1a847afeb30236bad98a2)
- [bt_gatt_cb_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga270c8a52bf3d512defc373f8c29b59f2)
- [bt_gatt_cb_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga5fb25c5eec91045dc4c7fd61ef7e528e)
- [bt_gatt_authorization_cb_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga5eee6afc6db391ffeda295d298bf6a56)
- [bt_gatt_service_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#gab4d9cfea04e44445d5dc30ad52842b64)
- [bt_gatt_service_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#gaf5bf0205fad5f7ad187b764d23deba6b)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [bt_gatt_service_is_registered](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#gae5c1e8b7bb1e673e228f03d1d084be9a)
- [bt_gatt_foreach_attr_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#gad8d8f513004f391167212d7bf9f7ff10)
- [bt_uuid](../bluetooth_connection_model_reference/P131_bt_uuid_结构体.md)
- [uuid](../data_utilities/P026_UUID二进制结构.md)
- [bt_gatt_foreach_attr](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#gaa93b5e0f2870ed135447bead903c175a)
- [bt_gatt_attr_next](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga35cecaa43b00b374062d29cca1479d85)
- [bt_gatt_find_by_uuid](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#gad2f3272b1dc42378104b492ec7caf6b0)
- [bt_gatt_attr_get_handle](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga2d51136ea1bd6cdb50900639506fd9f7)
- [bt_gatt_attr_value_handle](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga99738cf4f05eae4c6da17cc3420827d8)
- [bt_gatt_attr_read](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#gaf6d253849932b706ec7f303568980dfa)
- [bt_gatt_attr_read_service](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#gacae81c0f272bad7e6ac93c0d13b678c6)
- [bt_gatt_attr_read_included](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga4313a63decac2c8b7c4a1764df3d53ea)
- [bt_gatt_attr_read_chrc](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#gad58b526a06334530c13292d14a11257c)
- [bt_gatt_attr_read_ccc](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga2e85b42136e2c6a4cb5b7ad8a2532573)
- [bt_gatt_attr_write_ccc](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#gabba965b676650a55cb9934072b34c75e)
- [bt_gatt_attr_read_cep](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga5893166f1b24f437a94ccf1fc57c7917)
- [bt_gatt_attr_read_cud](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga29421c8788b47b6a648704d27d5f0d28)
- [bt_gatt_attr_read_cpf](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga5ae96590a0aaa5c4c3863a4a14d80fdd)
- [bt_gatt_notify_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga55e3ef7cb43b8acb0a27643c78390146)
- [bt_gatt_notify_multiple](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga8071d6063f85c0a78155f6b2ac2da635)
- [bt_gatt_notify](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga74ee552864c563aa5bc939f37395c14a)
- [bt_gatt_notify_uuid](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga24bae284dbc71cd4075649c4bc348b7c)
- [bt_gatt_indicate](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga4f2272692cc0f1d44638828012296c80)
- [bt_gatt_is_subscribed](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#gabd4df0a264dae10e43797992a567be7d)
- [bt_gatt_get_mtu](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga351fd7658eaecbbfa60f1769119ef733)
- [bt_gatt_get_uatt_mtu](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga6653de5e245cae6dc12cd0b45acbe028)
- [bt_gatt_exchange_mtu](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ga0f41da23c6559a8254b04295aff8198d)
- [bt_gatt_discover](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#gac06a945e5f7939b6716bc4f2cea781bd)
- [bt_gatt_read](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ga1a18dd726ab960a88d7f85f2a014141a)
- [bt_gatt_write](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ga843a42e68e0497d88d3f655f8ffd58d4)
- [bt_gatt_write_without_response_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ga49439413d12b5a8a1c68735e961ab6fa)
- [bt_gatt_write_without_response](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ga9fc78e32230637a6f092da2400c50fe7)
- [bt_gatt_subscribe](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ga7d4a8e18f51ba6476886a15f81f48e5c)
- [bt_gatt_resubscribe](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ga791b8bb8a4c085b022fafc0535a63511)
- [bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)
- [bt_gatt_unsubscribe](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ga56509c9b8f73f729cfa5e75be22d79ae)
- [bt_gatt_cancel](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ga5193dea59a016692f94cf950d6b4f4f7)

<a id="header-details"></a>

---

[上一章](P003_zephyr__dt-bindings__sensor__max30009.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P005_zephyr__dt-bindings__clock__ifx_clock_source_common.h_文件参考.md)

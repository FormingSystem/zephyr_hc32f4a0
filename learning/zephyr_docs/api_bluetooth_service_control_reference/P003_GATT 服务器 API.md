---
id: learning.zephyr-docs.api-bluetooth-service-control-reference.page-3
title: GATT 服务器 API
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_GATT 服务器 API

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 3.1\_数据结构（Data Structures）

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

<a id="header-define-members"></a>
<a id="define-members"></a>

## 3.2\_宏定义（Macros）

<a id="r_ga04c7887fb67107bd060dd023fd3186d5"></a>

```c
#define BT_GATT_SERVICE_DEFINE(_name, ...)
```

相关声明：[BT_GATT_SERVICE_DEFINE](#ga04c7887fb67107bd060dd023fd3186d5)。

静态定义并注册服务（Service）。

<a id="r_ga8bb3aeef20465d7f6e38f6bbddef74e5"></a>

```c
#define BT_GATT_SERVICE_INSTANCE_DEFINE( _name, _instances, _instance_num, _attrs_def)
```

相关声明：[BT_GATT_SERVICE_INSTANCE_DEFINE](#ga8bb3aeef20465d7f6e38f6bbddef74e5)。

静态定义服务结构体数组（Service Structure Array）。

<a id="r_ga7d413ec013b91a633ec24d80d2814e2b"></a>

```c
#define BT_GATT_SERVICE(_attrs)
```

相关声明：[BT_GATT_SERVICE](#ga7d413ec013b91a633ec24d80d2814e2b)。

服务结构体声明宏（Service Structure Declaration Macro）。

<a id="r_gaacada0ff1029af959b6fcd6703d4a0bf"></a>

```c
#define BT_GATT_PRIMARY_SERVICE(_service)
```

相关声明：[BT_GATT_PRIMARY_SERVICE](#gaacada0ff1029af959b6fcd6703d4a0bf)。

主服务声明宏（Primary Service Declaration Macro）。

<a id="r_gaecb4d30282677d3450ad79c5f83f3445"></a>

```c
#define BT_GATT_SECONDARY_SERVICE(_service)
```

相关声明：[BT_GATT_SECONDARY_SERVICE](#gaecb4d30282677d3450ad79c5f83f3445)。

次级服务声明宏（Secondary Service Declaration Macro）。

<a id="r_ga08ffee706d271b75a54b1b99249dba24"></a>

```c
#define BT_GATT_INCLUDE_SERVICE(_service_incl)
```

相关声明：[BT_GATT_INCLUDE_SERVICE](#ga08ffee706d271b75a54b1b99249dba24)。

包含服务声明宏（Include Service Declaration Macro）。

<a id="r_ga7f19592a722c41d6c1d2421d166dd78a"></a>

```c
#define BT_GATT_CHRC_INIT(_uuid, _handle, _props)
```

相关声明：[BT_GATT_CHRC_INIT](#ga7f19592a722c41d6c1d2421d166dd78a)。

GATT 特征初始化宏（Characteristic Initialization Macro）。

<a id="r_ga9e739546dbd906d3b3c4f1ed5ad9f41e"></a>

```c
#define BT_GATT_CHARACTERISTIC(_uuid, _props, _perm, _read, _write, _user_data)
```

相关声明：[BT_GATT_CHARACTERISTIC](#ga9e739546dbd906d3b3c4f1ed5ad9f41e)。

特征及其值声明宏（Characteristic and Value Declaration Macro）。

<a id="r_gac1c0a195c1ec1ff2cdd5bf6d0ba6ad00"></a>

```c
#define BT_GATT_CCC_MAX 0
```

相关声明：[BT_GATT_CCC_MAX](#gac1c0a195c1ec1ff2cdd5bf6d0ba6ad00)。

BT_GATT_CCC_MAX 的定义取决于是否设置 CONFIG_BT_SETTINGS_CCC_LAZY_LOADING 或 CONFIG_BT_CONN。

<a id="r_gae3a23386bfe38e0127b74e0f4b5e5667"></a>

```c
#define BT_GATT_CCC_MANAGED_USER_DATA_INIT(_changed, _write, _match)
```

相关声明：[BT_GATT_CCC_MANAGED_USER_DATA_INIT](#gae3a23386bfe38e0127b74e0f4b5e5667)。

初始化客户端特征配置声明的宏（Initialize Client Characteristic Configuration Declaration Macro）。

<a id="r_gad8b296ecfd1139680f21da7904b9f585"></a>

```c
#define BT_GATT_CCC_MANAGED(_ccc, _perm)
```

相关声明：[BT_GATT_CCC_MANAGED](#gad8b296ecfd1139680f21da7904b9f585)。

托管客户端特征配置声明宏（Managed Client Characteristic Configuration Declaration Macro）。

<a id="r_ga140b9c25d10244bebd9c891f881fdc94"></a>

```c
#define BT_GATT_CCC(_changed, _perm)
```

相关声明：[BT_GATT_CCC](#ga140b9c25d10244bebd9c891f881fdc94)。

客户端特征配置声明宏（Client Characteristic Configuration Declaration Macro）。

<a id="r_ga9a6fa72eb2b6e9438ad677365c998428"></a>

```c
#define BT_GATT_CCC_WITH_WRITE_CB(_changed, _write, _perm)
```

相关声明：[BT_GATT_CCC_WITH_WRITE_CB](#ga9a6fa72eb2b6e9438ad677365c998428)。

带写回调的客户端特征配置声明宏（Client Characteristic Configuration Declaration Macro with Write Callback）。

<a id="r_ga55a82cada1093c4ff75fe5504ac504b1"></a>

```c
#define BT_GATT_CEP(_value)
```

相关声明：[BT_GATT_CEP](#ga55a82cada1093c4ff75fe5504ac504b1)。

特征扩展属性声明宏（Characteristic Extended Properties Declaration Macro）。

<a id="r_ga1e1cd9d0853e2dcbefcb85fda44dc9c7"></a>

```c
#define BT_GATT_CUD(_value, _perm)
```

相关声明：[BT_GATT_CUD](#ga1e1cd9d0853e2dcbefcb85fda44dc9c7)。

特征用户格式描述符声明宏（Characteristic User Format Descriptor Declaration Macro）。

<a id="r_ga3835fcfdf7a5f917e21c9d17e75162be"></a>

```c
#define BT_GATT_CPF(_value)
```

相关声明：[BT_GATT_CPF](#ga3835fcfdf7a5f917e21c9d17e75162be)。

特征呈现格式描述符声明宏（Characteristic Presentation Format Descriptor Declaration Macro）。

<a id="r_ga83207fc083454327004f7d3c3e5b3840"></a>

```c
#define BT_GATT_DESCRIPTOR(_uuid, _perm, _read, _write, _user_data)
```

相关声明：[BT_GATT_DESCRIPTOR](#ga83207fc083454327004f7d3c3e5b3840)。

描述符声明宏（Descriptor Declaration Macro）。

<a id="r_gac4abfeb068d16dcdaceee812c12bf406"></a>

```c
#define BT_GATT_ATTRIBUTE(_uuid, _perm, _read, _write, _user_data)
```

相关声明：[BT_GATT_ATTRIBUTE](#gac4abfeb068d16dcdaceee812c12bf406)。

属性声明宏（Attribute Declaration Macro）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 3.3\_类型定义（Typedefs）

<a id="r_ga60284611c90729b289fe806524ba9209"></a>

```c
typedef uint8_t(* bt_gatt_attr_func_t) (const struct bt_gatt_attr *attr, uint16_t handle, void *user_data)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_gatt_attr_func_t](#ga60284611c90729b289fe806524ba9209)、[bt_gatt_attr](../bluetooth_connection_model_reference/P049_bt_gatt_attr_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

属性迭代器回调（Attribute Iterator Callback）。

<a id="r_gac55832607b95f394d26a64ed1cfe5bba"></a>

```c
typedef void(* bt_gatt_complete_func_t) (struct bt_conn *conn, void *user_data)
```

相关声明：[bt_gatt_complete_func_t](#gac55832607b95f394d26a64ed1cfe5bba)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

通知完成结果回调（Notification Complete Result Callback）。

<a id="r_ga1294850e6bdcbe7a8f42f2956fd837a8"></a>

```c
typedef void(* bt_gatt_indicate_func_t) (struct bt_conn *conn, struct bt_gatt_indicate_params *params, uint8_t err)
```

相关声明：[bt_gatt_indicate_func_t](#ga1294850e6bdcbe7a8f42f2956fd837a8)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_gatt_indicate_params](../bluetooth_connection_model_reference/P061_bt_gatt_indicate_params_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

指示完成结果回调（Indication Complete Result Callback）。

<a id="r_ga5d47ed9eaea22c8f00db14329daee8fe"></a>

```c
typedef void(* bt_gatt_indicate_params_destroy_t) (struct bt_gatt_indicate_params *params)
```

相关声明：[bt_gatt_indicate_params_destroy_t](#ga5d47ed9eaea22c8f00db14329daee8fe)、[bt_gatt_indicate_params](../bluetooth_connection_model_reference/P061_bt_gatt_indicate_params_结构体.md)。

用于销毁或清理 GATT 指示值参数（Indicate Value Parameters）的回调。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 3.4\_枚举（Enumerations）

<a id="r_gab38994257f53473e62e01eff8f236ee1"></a>

```c
enum bt_gatt_iter { BT_GATT_ITER_STOP = 0 , BT_GATT_ITER_CONTINUE }
```

相关声明：[bt_gatt_iter](#gab38994257f53473e62e01eff8f236ee1)、[BT_GATT_ITER_STOP](#ggab38994257f53473e62e01eff8f236ee1aa3f2a25e27c7065a2c7bb2a9ff09542e)、[BT_GATT_ITER_CONTINUE](#ggab38994257f53473e62e01eff8f236ee1aea569feffa4815d3443e12be78c684f5)。

用作 bt_gatt_attr_func_t 和 bt_gatt_read_func_t 类型回调的返回值（Return Values）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 3.5\_函数（Functions）

<a id="r_gaf6d3f1e904f1a847afeb30236bad98a2"></a>

```c
static const char * bt_gatt_err_to_str (int gatt_err)
```

相关声明：[bt_gatt_err_to_str](#gaf6d3f1e904f1a847afeb30236bad98a2)。

将 GATT 错误转换为字符串（String）。

<a id="r_ga270c8a52bf3d512defc373f8c29b59f2"></a>

```c
void bt_gatt_cb_register (struct bt_gatt_cb *cb)
```

相关声明：[bt_gatt_cb_register](#ga270c8a52bf3d512defc373f8c29b59f2)、[bt_gatt_cb](../bluetooth_connection_model_reference/P051_bt_gatt_cb_结构体.md)。

注册 GATT 回调（Callbacks）。

<a id="r_ga5fb25c5eec91045dc4c7fd61ef7e528e"></a>

```c
int bt_gatt_cb_unregister (struct bt_gatt_cb *cb)
```

相关声明：[bt_gatt_cb_unregister](#ga5fb25c5eec91045dc4c7fd61ef7e528e)、[bt_gatt_cb](../bluetooth_connection_model_reference/P051_bt_gatt_cb_结构体.md)。

注销 GATT 回调（Callbacks）。

<a id="r_ga5eee6afc6db391ffeda295d298bf6a56"></a>

```c
int bt_gatt_authorization_cb_register (const struct bt_gatt_authorization_cb *cb)
```

相关声明：[bt_gatt_authorization_cb_register](#ga5eee6afc6db391ffeda295d298bf6a56)、[bt_gatt_authorization_cb](../bluetooth_connection_model_reference/P050_bt_gatt_authorization_cb_结构体.md)。

注册 GATT 授权回调（Authorization Callbacks）。

<a id="r_gab4d9cfea04e44445d5dc30ad52842b64"></a>

```c
int bt_gatt_service_register (struct bt_gatt_service *svc)
```

相关声明：[bt_gatt_service_register](#gab4d9cfea04e44445d5dc30ad52842b64)、[bt_gatt_service](../bluetooth_connection_model_reference/P065_bt_gatt_service_结构体.md)。

注册 GATT 服务（Service）。

<a id="r_gaf5bf0205fad5f7ad187b764d23deba6b"></a>

```c
int bt_gatt_service_unregister (struct bt_gatt_service *svc)
```

相关声明：[bt_gatt_service_unregister](#gaf5bf0205fad5f7ad187b764d23deba6b)、[bt_gatt_service](../bluetooth_connection_model_reference/P065_bt_gatt_service_结构体.md)。

注销 GATT 服务（Service）。

<a id="r_gae5c1e8b7bb1e673e228f03d1d084be9a"></a>

```c
bool bt_gatt_service_is_registered (const struct bt_gatt_service *svc)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_gatt_service_is_registered](#gae5c1e8b7bb1e673e228f03d1d084be9a)、[bt_gatt_service](../bluetooth_connection_model_reference/P065_bt_gatt_service_结构体.md)。

检查 GATT 服务（Service）是否已注册。

<a id="r_gad8d8f513004f391167212d7bf9f7ff10"></a>

```c
void bt_gatt_foreach_attr_type (uint16_t start_handle, uint16_t end_handle, const struct bt_uuid *uuid, const void *attr_data, uint16_t num_matches, bt_gatt_attr_func_t func, void *user_data)
```

相关声明：[bt_gatt_foreach_attr_type](#gad8d8f513004f391167212d7bf9f7ff10)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_uuid](../bluetooth_connection_model_reference/P131_bt_uuid_结构体.md)、[uuid](../data_utilities/P026_UUID二进制结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_gatt_attr_func_t](#ga60284611c90729b289fe806524ba9209)。

按类型遍历的属性迭代器（Attribute Iterator by Type）。

<a id="r_gaa93b5e0f2870ed135447bead903c175a"></a>

```c
static void bt_gatt_foreach_attr (uint16_t start_handle, uint16_t end_handle, bt_gatt_attr_func_t func, void *user_data)
```

相关声明：[bt_gatt_foreach_attr](#gaa93b5e0f2870ed135447bead903c175a)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_gatt_attr_func_t](#ga60284611c90729b289fe806524ba9209)。

属性迭代器（Attribute Iterator）。

<a id="r_ga35cecaa43b00b374062d29cca1479d85"></a>

```c
struct bt_gatt_attr * bt_gatt_attr_next (const struct bt_gatt_attr *attr)
```

相关声明：[bt_gatt_attr](../bluetooth_connection_model_reference/P049_bt_gatt_attr_结构体.md)、[bt_gatt_attr_next](#ga35cecaa43b00b374062d29cca1479d85)、[bt_gatt_attr](../bluetooth_connection_model_reference/P049_bt_gatt_attr_结构体.md)。

迭代到下一个属性（Attribute）。

<a id="r_gad2f3272b1dc42378104b492ec7caf6b0"></a>

```c
struct bt_gatt_attr * bt_gatt_find_by_uuid (const struct bt_gatt_attr *attr, uint16_t attr_count, const struct bt_uuid *uuid)
```

相关声明：[bt_gatt_attr](../bluetooth_connection_model_reference/P049_bt_gatt_attr_结构体.md)、[bt_gatt_find_by_uuid](#gad2f3272b1dc42378104b492ec7caf6b0)、[bt_gatt_attr](../bluetooth_connection_model_reference/P049_bt_gatt_attr_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_uuid](../bluetooth_connection_model_reference/P131_bt_uuid_结构体.md)、[uuid](../data_utilities/P026_UUID二进制结构.md)。

按 UUID 查找属性（Attribute）。

<a id="r_ga2d51136ea1bd6cdb50900639506fd9f7"></a>

```c
uint16_t bt_gatt_attr_get_handle (const struct bt_gatt_attr *attr)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_gatt_attr_get_handle](#ga2d51136ea1bd6cdb50900639506fd9f7)、[bt_gatt_attr](../bluetooth_connection_model_reference/P049_bt_gatt_attr_结构体.md)。

获取属性句柄（Attribute Handle）。

<a id="r_ga99738cf4f05eae4c6da17cc3420827d8"></a>

```c
uint16_t bt_gatt_attr_value_handle (const struct bt_gatt_attr *attr)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_gatt_attr_value_handle](#ga99738cf4f05eae4c6da17cc3420827d8)、[bt_gatt_attr](../bluetooth_connection_model_reference/P049_bt_gatt_attr_结构体.md)。

获取特征值描述符（Characteristic Value Descriptor）的句柄。

<a id="r_gaf6d253849932b706ec7f303568980dfa"></a>

```c
ssize_t bt_gatt_attr_read (struct bt_conn *conn, const struct bt_gatt_attr *attr, void *buf, uint16_t buf_len, uint16_t offset, const void *value, uint16_t value_len)
```

相关声明：[ssize_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)、[bt_gatt_attr_read](#gaf6d253849932b706ec7f303568980dfa)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_gatt_attr](../bluetooth_connection_model_reference/P049_bt_gatt_attr_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

通用属性值读取辅助函数（Generic Read Attribute Value Helper）。

<a id="r_gacae81c0f272bad7e6ac93c0d13b678c6"></a>

```c
ssize_t bt_gatt_attr_read_service (struct bt_conn *conn, const struct bt_gatt_attr *attr, void *buf, uint16_t len, uint16_t offset)
```

相关声明：[ssize_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)、[bt_gatt_attr_read_service](#gacae81c0f272bad7e6ac93c0d13b678c6)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_gatt_attr](../bluetooth_connection_model_reference/P049_bt_gatt_attr_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

服务属性读取辅助函数（Read Service Attribute Helper）。

<a id="r_ga4313a63decac2c8b7c4a1764df3d53ea"></a>

```c
ssize_t bt_gatt_attr_read_included (struct bt_conn *conn, const struct bt_gatt_attr *attr, void *buf, uint16_t len, uint16_t offset)
```

相关声明：[ssize_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)、[bt_gatt_attr_read_included](#ga4313a63decac2c8b7c4a1764df3d53ea)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_gatt_attr](../bluetooth_connection_model_reference/P049_bt_gatt_attr_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

包含属性读取辅助函数（Read Include Attribute Helper）。

<a id="r_gad58b526a06334530c13292d14a11257c"></a>

```c
ssize_t bt_gatt_attr_read_chrc (struct bt_conn *conn, const struct bt_gatt_attr *attr, void *buf, uint16_t len, uint16_t offset)
```

相关声明：[ssize_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)、[bt_gatt_attr_read_chrc](#gad58b526a06334530c13292d14a11257c)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_gatt_attr](../bluetooth_connection_model_reference/P049_bt_gatt_attr_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

特征属性读取辅助函数（Read Characteristic Attribute Helper）。

<a id="r_ga2e85b42136e2c6a4cb5b7ad8a2532573"></a>

```c
ssize_t bt_gatt_attr_read_ccc (struct bt_conn *conn, const struct bt_gatt_attr *attr, void *buf, uint16_t len, uint16_t offset)
```

相关声明：[ssize_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)、[bt_gatt_attr_read_ccc](#ga2e85b42136e2c6a4cb5b7ad8a2532573)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_gatt_attr](../bluetooth_connection_model_reference/P049_bt_gatt_attr_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

客户端特征配置属性读取辅助函数（Read Client Characteristic Configuration Attribute Helper）。

<a id="r_gabba965b676650a55cb9934072b34c75e"></a>

```c
ssize_t bt_gatt_attr_write_ccc (struct bt_conn *conn, const struct bt_gatt_attr *attr, const void *buf, uint16_t len, uint16_t offset, uint8_t flags)
```

相关声明：[ssize_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)、[bt_gatt_attr_write_ccc](#gabba965b676650a55cb9934072b34c75e)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_gatt_attr](../bluetooth_connection_model_reference/P049_bt_gatt_attr_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

客户端特征配置属性写入辅助函数（Write Client Characteristic Configuration Attribute Helper）。

<a id="r_ga5893166f1b24f437a94ccf1fc57c7917"></a>

```c
ssize_t bt_gatt_attr_read_cep (struct bt_conn *conn, const struct bt_gatt_attr *attr, void *buf, uint16_t len, uint16_t offset)
```

相关声明：[ssize_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)、[bt_gatt_attr_read_cep](#ga5893166f1b24f437a94ccf1fc57c7917)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_gatt_attr](../bluetooth_connection_model_reference/P049_bt_gatt_attr_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

特征扩展属性读取辅助函数（Read Characteristic Extended Properties Attribute Helper）。

<a id="r_ga29421c8788b47b6a648704d27d5f0d28"></a>

```c
ssize_t bt_gatt_attr_read_cud (struct bt_conn *conn, const struct bt_gatt_attr *attr, void *buf, uint16_t len, uint16_t offset)
```

相关声明：[ssize_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)、[bt_gatt_attr_read_cud](#ga29421c8788b47b6a648704d27d5f0d28)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_gatt_attr](../bluetooth_connection_model_reference/P049_bt_gatt_attr_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

特征用户描述描述符属性读取辅助函数（Read Characteristic User Description Descriptor Attribute Helper）。

<a id="r_ga5ae96590a0aaa5c4c3863a4a14d80fdd"></a>

```c
ssize_t bt_gatt_attr_read_cpf (struct bt_conn *conn, const struct bt_gatt_attr *attr, void *buf, uint16_t len, uint16_t offset)
```

相关声明：[ssize_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)、[bt_gatt_attr_read_cpf](#ga5ae96590a0aaa5c4c3863a4a14d80fdd)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_gatt_attr](../bluetooth_connection_model_reference/P049_bt_gatt_attr_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

特征呈现格式描述符属性读取辅助函数（Read Characteristic Presentation Format Descriptor Attribute Helper）。

<a id="r_ga55e3ef7cb43b8acb0a27643c78390146"></a>

```c
int bt_gatt_notify_cb (struct bt_conn *conn, struct bt_gatt_notify_params *params)
```

相关声明：[bt_gatt_notify_cb](#ga55e3ef7cb43b8acb0a27643c78390146)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_gatt_notify_params](../bluetooth_connection_model_reference/P062_bt_gatt_notify_params_结构体.md)。

发送属性值变化通知（Notify Attribute Value Change）。

<a id="r_ga8071d6063f85c0a78155f6b2ac2da635"></a>

```c
int bt_gatt_notify_multiple (struct bt_conn *conn, uint16_t num_params, struct bt_gatt_notify_params params[])
```

相关声明：[bt_gatt_notify_multiple](#ga8071d6063f85c0a78155f6b2ac2da635)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_gatt_notify_params](../bluetooth_connection_model_reference/P062_bt_gatt_notify_params_结构体.md)。

在一个协议数据单元（PDU）中发送多个通知（Notifications）。

<a id="r_ga74ee552864c563aa5bc939f37395c14a"></a>

```c
static int bt_gatt_notify (struct bt_conn *conn, const struct bt_gatt_attr *attr, const void *data, uint16_t len)
```

相关声明：[bt_gatt_notify](#ga74ee552864c563aa5bc939f37395c14a)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_gatt_attr](../bluetooth_connection_model_reference/P049_bt_gatt_attr_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

发送属性值变化通知（Notify Attribute Value Change）。

<a id="r_ga24bae284dbc71cd4075649c4bc348b7c"></a>

```c
static int bt_gatt_notify_uuid (struct bt_conn *conn, const struct bt_uuid *uuid, const struct bt_gatt_attr *attr, const void *data, uint16_t len)
```

相关声明：[bt_gatt_notify_uuid](#ga24bae284dbc71cd4075649c4bc348b7c)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_uuid](../bluetooth_connection_model_reference/P131_bt_uuid_结构体.md)、[uuid](../data_utilities/P026_UUID二进制结构.md)、[bt_gatt_attr](../bluetooth_connection_model_reference/P049_bt_gatt_attr_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

按 UUID 发送属性值变化通知（Notify Attribute Value Change）。

<a id="r_ga4f2272692cc0f1d44638828012296c80"></a>

```c
int bt_gatt_indicate (struct bt_conn *conn, struct bt_gatt_indicate_params *params)
```

相关声明：[bt_gatt_indicate](#ga4f2272692cc0f1d44638828012296c80)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_gatt_indicate_params](../bluetooth_connection_model_reference/P061_bt_gatt_indicate_params_结构体.md)。

发送属性值变化指示（Indicate Attribute Value Change）。

<a id="r_gabd4df0a264dae10e43797992a567be7d"></a>

```c
bool bt_gatt_is_subscribed (struct bt_conn *conn, const struct bt_gatt_attr *attr, uint16_t ccc_type)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_gatt_is_subscribed](#gabd4df0a264dae10e43797992a567be7d)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_gatt_attr](../bluetooth_connection_model_reference/P049_bt_gatt_attr_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

检查连接是否已订阅（Subscribed）该属性。

<a id="r_ga351fd7658eaecbbfa60f1769119ef733"></a>

```c
uint16_t bt_gatt_get_mtu (struct bt_conn *conn)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_gatt_get_mtu](#ga351fd7658eaecbbfa60f1769119ef733)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

获取连接的 ATT 最大传输单元（MTU）。

<a id="r_ga6653de5e245cae6dc12cd0b45acbe028"></a>

```c
uint16_t bt_gatt_get_uatt_mtu (struct bt_conn *conn)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_gatt_get_uatt_mtu](#ga6653de5e245cae6dc12cd0b45acbe028)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

获取连接的非增强属性协议（Unenhanced ATT，UATT）的 MTU。

## 3.6\_详细说明（Detailed Documentation）

<a id="gac4abfeb068d16dcdaceee812c12bf406"></a>

### `BT_GATT_ATTRIBUTE`

```c
#define BT_GATT_ATTRIBUTE ( _uuid, _perm, _read, _write, _user_data )
```

```c
#include <zephyr/bluetooth/gatt.h>
```

展开值（Value）：

```c
{                                                                       \
        .uuid = _uuid,                                                  \
        .read = _read,                                                  \
        .write = _write,                                                \
        .user_data = _user_data,                                        \
        .handle = 0,                                                    \
        .perm = _perm,                                                  \
}
```

属性声明宏（Attribute Declaration Macro）。

用于声明属性（Attribute）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_uuid` | 属性的通用唯一标识符（UUID）。 |
| `_perm` | 属性访问权限（Access Permissions），由 `bt_gatt_perm` 值组成的位图。 |
| `_read` | 属性读取回调（Read Callback），类型为 `bt_gatt_attr_read_func_t`。 |
| `_write` | 属性写入回调（Write Callback），类型为 `bt_gatt_attr_write_func_t`。 |
| `_user_data` | 属性用户数据（User Data）。 |

<a id="ga140b9c25d10244bebd9c891f881fdc94"></a>

### `BT_GATT_CCC`

```c
#define BT_GATT_CCC ( _changed, _perm )
```

```c
#include <zephyr/bluetooth/gatt.h>
```

展开值（Value）：

```c
BT_GATT_CCC_MANAGED(((struct bt_gatt_ccc_managed_user_data[]){                             \
                            BT_GATT_CCC_MANAGED_USER_DATA_INIT(_changed, NULL, NULL)}),    \
                    _perm)
```

客户端特征配置声明宏（Client Characteristic Configuration Declaration Macro）。

用于声明客户端特征配置（Client Characteristic Configuration，CCC）属性的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_changed` | 配置变化回调（Configuration Changed Callback）。 |
| `_perm` | CCC 访问权限（Access Permissions），由 `bt_gatt_perm` 值组成的位图。 |

<a id="gad8b296ecfd1139680f21da7904b9f585"></a>

### `BT_GATT_CCC_MANAGED`

```c
#define BT_GATT_CCC_MANAGED ( _ccc, _perm )
```

```c
#include <zephyr/bluetooth/gatt.h>
```

展开值（Value）：

```c
BT_GATT_ATTRIBUTE(BT_UUID_GATT_CCC, _perm,                      \
                bt_gatt_attr_read_ccc, bt_gatt_attr_write_ccc,  \
                _ccc)
```

托管客户端特征配置声明宏（Managed Client Characteristic Configuration Declaration Macro）。

用于声明托管客户端特征配置（Managed CCC）属性的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_ccc` | 一个新的 `bt_gatt_ccc_managed_user_data` 对象，其生命周期（Lifetime）与调用 `BT_GATT_CCC_MANAGED` 得到的结果相同。初始化方法参见 `bt_gatt_ccc_managed_user_data` 文档。 |
| `_perm` | CCC 访问权限（Access Permissions），由 `bt_gatt_perm` 值组成的位图。 |

<a id="gae3a23386bfe38e0127b74e0f4b5e5667"></a>

### `BT_GATT_CCC_MANAGED_USER_DATA_INIT`

```c
#define BT_GATT_CCC_MANAGED_USER_DATA_INIT ( _changed, _write, _match )
```

```c
#include <zephyr/bluetooth/gatt.h>
```

展开值（Value）：

```c
{                                                                                          \
        .cfg = {},                                                                         \
        .cfg_changed = _changed,                                                           \
        .cfg_write = _write,                                                               \
        .cfg_match = _match,                                                               \
}
```

初始化客户端特征配置声明的宏（Initialize Client Characteristic Configuration Declaration Macro）。

用于初始化托管客户端特征配置（Managed CCC）属性值的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_changed` | 配置变化回调（Configuration Changed Callback）。 |
| `_write` | 配置写入回调（Configuration Write Callback）。 |
| `_match` | 配置匹配回调（Configuration Match Callback）。 |

<a id="gac1c0a195c1ec1ff2cdd5bf6d0ba6ad00"></a>

### `BT_GATT_CCC_MAX`

```c
#define BT_GATT_CCC_MAX 0
```

```c
#include <zephyr/bluetooth/gatt.h>
```

BT_GATT_CCC_MAX 的定义取决于是否设置 CONFIG_BT_SETTINGS_CCC_LAZY_LOADING 或 CONFIG_BT_CONN。

`CONFIG_BT_SETTINGS_CCC_LAZY_LOADING` 会将 `BT_GATT_CCC_MAX` 设为 `CONFIG_BT_MAX_CONN`；`CONFIG_BT_CONN` 会将 `BT_GATT_CCC_MAX` 设为 `CONFIG_BT_MAX_PAIRED + CONFIG_BT_MAX_CONN`。两者均未设置时，`BT_GATT_CCC_MAX` 为 0。

<a id="ga9a6fa72eb2b6e9438ad677365c998428"></a>

### `BT_GATT_CCC_WITH_WRITE_CB`

```c
#define BT_GATT_CCC_WITH_WRITE_CB ( _changed, _write, _perm )
```

```c
#include <zephyr/bluetooth/gatt.h>
```

展开值（Value）：

```c
BT_GATT_CCC_MANAGED(((struct bt_gatt_ccc_managed_user_data[]){                             \
                            BT_GATT_CCC_MANAGED_USER_DATA_INIT(_changed, _write, NULL)}),  \
                    _perm)
```

带写回调的客户端特征配置声明宏（Client Characteristic Configuration Declaration Macro with Write Callback）。

用于声明带写入回调（Write Callback）的 CCC 属性的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_changed` | 配置变化回调（Configuration Changed Callback）。 |
| `_write` | 配置写入回调（Configuration Write Callback）。 |
| `_perm` | CCC 访问权限（Access Permissions），由 `bt_gatt_perm` 值组成的位图。 |

<a id="ga55a82cada1093c4ff75fe5504ac504b1"></a>

### `BT_GATT_CEP`

```c
#define BT_GATT_CEP ( _value)
```

```c
#include <zephyr/bluetooth/gatt.h>
```

展开值（Value）：

```c
BT_GATT_DESCRIPTOR(BT_UUID_GATT_CEP, BT_GATT_PERM_READ,         \
                  bt_gatt_attr_read_cep, NULL, (void *)_value)
```

特征扩展属性声明宏（Characteristic Extended Properties Declaration Macro）。

用于声明特征扩展属性（Characteristic Extended Properties，CEP）属性的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_value` | 指向 `struct bt_gatt_cep` 的指针。 |

<a id="ga9e739546dbd906d3b3c4f1ed5ad9f41e"></a>

### `BT_GATT_CHARACTERISTIC`

```c
#define BT_GATT_CHARACTERISTIC ( _uuid, _props, _perm, _read, _write, _user_data )
```

```c
#include <zephyr/bluetooth/gatt.h>
```

展开值（Value）：

```c
BT_GATT_ATTRIBUTE(BT_UUID_GATT_CHRC, BT_GATT_PERM_READ,                 \
                  bt_gatt_attr_read_chrc, NULL,                         \
                  ((struct bt_gatt_chrc[]) {                            \
                        BT_GATT_CHRC_INIT(_uuid, 0U, _props),           \
                                           })),                         \
BT_GATT_ATTRIBUTE(_uuid, _perm, _read, _write, _user_data)
```

特征及其值声明宏（Characteristic and Value Declaration Macro）。

用于同时声明特征属性（Characteristic Attribute）及其属性值（Attribute Value）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_uuid` | 特征属性（Characteristic Attribute）的 UUID。 |
| `_props` | 特征属性的性质（Properties），由 `BT_GATT_CHRC_*` 宏组成的位图。 |
| `_perm` | 特征属性的访问权限（Access Permissions），由 `bt_gatt_perm` 值组成的位图。 |
| `_read` | 特征属性的读取回调（Read Callback），类型为 `bt_gatt_attr_read_func_t`。 |
| `_write` | 特征属性的写入回调（Write Callback），类型为 `bt_gatt_attr_write_func_t`。 |
| `_user_data` | 特征属性的用户数据（User Data）。 |

<a id="ga7f19592a722c41d6c1d2421d166dd78a"></a>

### `BT_GATT_CHRC_INIT`

```c
#define BT_GATT_CHRC_INIT ( _uuid, _handle, _props )
```

```c
#include <zephyr/bluetooth/gatt.h>
```

展开值（Value）：

```c
{                                                 \
        .uuid = _uuid,                            \
        .value_handle = _handle,                  \
        .properties = _props,                     \
}
```

GATT 特征初始化宏（Characteristic Initialization Macro）。

用于 GATT 属性声明中 `BT_GATT_CHARACTERISTIC` 宏内部的辅助宏，用于设置属性用户数据（User Data）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_uuid` | 特征属性（Characteristic Attribute）的 UUID。 |
| `_handle` | 初始化时的特征属性句柄（Characteristic Attribute Handle）。 |
| `_props` | 特征属性的性质（Properties），由 `BT_GATT_CHRC_*` 宏组成的位图。 |

<a id="ga3835fcfdf7a5f917e21c9d17e75162be"></a>

### `BT_GATT_CPF`

```c
#define BT_GATT_CPF ( _value)
```

```c
#include <zephyr/bluetooth/gatt.h>
```

展开值（Value）：

```c
BT_GATT_DESCRIPTOR(BT_UUID_GATT_CPF, BT_GATT_PERM_READ,         \
                  bt_gatt_attr_read_cpf, NULL, (void *)_value)
```

特征呈现格式描述符声明宏（Characteristic Presentation Format Descriptor Declaration Macro）。

用于声明特征呈现格式（Characteristic Presentation Format，CPF）属性的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_value` | 指向 `struct bt_gatt_cpf` 的指针。 |

<a id="ga1e1cd9d0853e2dcbefcb85fda44dc9c7"></a>

### `BT_GATT_CUD`

```c
#define BT_GATT_CUD ( _value, _perm )
```

```c
#include <zephyr/bluetooth/gatt.h>
```

展开值（Value）：

```c
BT_GATT_DESCRIPTOR(BT_UUID_GATT_CUD, _perm, bt_gatt_attr_read_cud, \
                   NULL, (void *)_value)
```

特征用户格式描述符声明宏（Characteristic User Format Descriptor Declaration Macro）。

用于声明特征用户描述（Characteristic User Description，CUD）属性的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_value` | 用户描述（User Description），采用以空字符结尾的 C 字符串。 |
| `_perm` | 描述符属性的访问权限（Access Permissions），由 `bt_gatt_perm` 值组成的位图。 |

<a id="ga83207fc083454327004f7d3c3e5b3840"></a>

### `BT_GATT_DESCRIPTOR`

```c
#define BT_GATT_DESCRIPTOR ( _uuid, _perm, _read, _write, _user_data )
```

```c
#include <zephyr/bluetooth/gatt.h>
```

展开值（Value）：

```c
BT_GATT_ATTRIBUTE(_uuid, _perm, _read, _write, _user_data)
```

描述符声明宏（Descriptor Declaration Macro）。

用于声明描述符属性（Descriptor Attribute）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_uuid` | 描述符属性的 UUID。 |
| `_perm` | 描述符属性的访问权限（Access Permissions），由 `bt_gatt_perm` 值组成的位图。 |
| `_read` | 描述符属性的读取回调（Read Callback），类型为 `bt_gatt_attr_read_func_t`。 |
| `_write` | 描述符属性的写入回调（Write Callback），类型为 `bt_gatt_attr_write_func_t`。 |
| `_user_data` | 描述符属性的用户数据（User Data）。 |

<a id="ga08ffee706d271b75a54b1b99249dba24"></a>

### `BT_GATT_INCLUDE_SERVICE`

```c
#define BT_GATT_INCLUDE_SERVICE ( _service_incl)
```

```c
#include <zephyr/bluetooth/gatt.h>
```

展开值（Value）：

```c
BT_GATT_ATTRIBUTE(BT_UUID_GATT_INCLUDE, BT_GATT_PERM_READ,      \
                  bt_gatt_attr_read_included, NULL, _service_incl)
```

包含服务声明宏（Include Service Declaration Macro）。

用于声明数据库内部包含服务属性（Include Service Attribute）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_service_incl` | 要包含的服务的第一个服务属性（Service Attribute）。 |

<a id="gaacada0ff1029af959b6fcd6703d4a0bf"></a>

### `BT_GATT_PRIMARY_SERVICE`

```c
#define BT_GATT_PRIMARY_SERVICE ( _service)
```

```c
#include <zephyr/bluetooth/gatt.h>
```

展开值（Value）：

```c
BT_GATT_ATTRIBUTE(BT_UUID_GATT_PRIMARY, BT_GATT_PERM_READ,      \
                 bt_gatt_attr_read_service, NULL, (void *)_service)
```

主服务声明宏（Primary Service Declaration Macro）。

用于声明主服务属性（Primary Service Attribute）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_service` | 服务属性值（Service Attribute Value）。 |

<a id="gaecb4d30282677d3450ad79c5f83f3445"></a>

### `BT_GATT_SECONDARY_SERVICE`

```c
#define BT_GATT_SECONDARY_SERVICE ( _service)
```

```c
#include <zephyr/bluetooth/gatt.h>
```

展开值（Value）：

```c
BT_GATT_ATTRIBUTE(BT_UUID_GATT_SECONDARY, BT_GATT_PERM_READ,    \
                 bt_gatt_attr_read_service, NULL, (void *)_service)
```

次级服务声明宏（Secondary Service Declaration Macro）。

用于声明次级服务属性（Secondary Service Attribute）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_service` | 服务属性值（Service Attribute Value）。 |

**说明（Note）**：注意：次级服务（Secondary Service）仅供主服务（Primary Service）、其他次级服务或其他更高层规范包含使用。

<a id="ga7d413ec013b91a633ec24d80d2814e2b"></a>

### `BT_GATT_SERVICE`

```c
#define BT_GATT_SERVICE ( _attrs)
```

```c
#include <zephyr/bluetooth/gatt.h>
```

展开值（Value）：

```c
{                                                                       \
        .attrs = _attrs,                                                \
        .attr_count = ARRAY_SIZE(_attrs),                               \
}
```

服务结构体声明宏（Service Structure Declaration Macro）。

用于声明服务结构（Service Structure）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_attrs` | 服务属性（Service Attributes）。 |

<a id="ga04c7887fb67107bd060dd023fd3186d5"></a>

### `BT_GATT_SERVICE_DEFINE`

```c
#define BT_GATT_SERVICE_DEFINE ( _name, ... )
```

```c
#include <zephyr/bluetooth/gatt.h>
```

展开值（Value）：

```c
const struct bt_gatt_attr attr_##_name[] = { __VA_ARGS__ };     \
const STRUCT_SECTION_ITERABLE(bt_gatt_service_static, _name) =  \
                                BT_GATT_SERVICE(attr_##_name)
```

静态定义并注册服务（Service）。

用于静态定义并注册服务（Service）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | 服务名称（Service Name）。 |

<a id="ga8bb3aeef20465d7f6e38f6bbddef74e5"></a>

### `BT_GATT_SERVICE_INSTANCE_DEFINE`

```c
#define BT_GATT_SERVICE_INSTANCE_DEFINE ( _name, _instances, _instance_num, _attrs_def )
```

```c
#include <zephyr/bluetooth/gatt.h>
```

展开值（Value）：

```c
BUILD_ASSERT(ARRAY_SIZE(_instances) == _instance_num,            \
        "The number of array elements does not match its size"); \
LISTIFY(_instance_num, _BT_GATT_ATTRS_ARRAY_DEFINE, (;),         \
        _instances, _attrs_def);                                 \
static struct bt_gatt_service _name[] = {                        \
        LISTIFY(_instance_num, _BT_GATT_SERVICE_ARRAY_ITEM, (,)) \
}
```

静态定义服务结构体数组（Service Structure Array）。

用于静态定义服务结构数组（Service Structure Array）的辅助宏。数组中的每个元素都关联到一个服务属性数组；该属性数组也在此作用域中使用 `_attrs_def` 宏定义。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | 服务结构数组（Service Structure Array）的名称。 |
| `_instances` | 实例数组（Instance Array），其中的实例作为用户上下文（User Context）传递给属性回调。 |
| `_instance_num` | 实例数组（Instance Array）的元素数量。 |
| `_attrs_def` | 由用户提供、用于定义服务属性数组（Attribute Array）的宏。此宏应接受一个参数，即实例上下文（Instance Context）。 |

<a id="ga60284611c90729b289fe806524ba9209"></a>

### `bt_gatt_attr_func_t`

```c
typedef uint8_t(* bt_gatt_attr_func_t) (const struct bt_gatt_attr *attr, uint16_t handle, void *user_data)
```

```c
#include <zephyr/bluetooth/gatt.h>
```

属性迭代器回调（Attribute Iterator Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `attr` | 找到的属性（Attribute）。 |
| `handle` | 找到的属性句柄（Attribute Handle）。 |
| `user_data` | 所给数据（Data）。 |

**返回（Returns）**：返回值（Returns）：需要继续读取下一个属性（Attribute）时返回 `BT_GATT_ITER_CONTINUE`；停止时返回 `BT_GATT_ITER_STOP`。

<a id="gac55832607b95f394d26a64ed1cfe5bba"></a>

### `bt_gatt_complete_func_t`

```c
typedef void(* bt_gatt_complete_func_t) (struct bt_conn *conn, void *user_data)
```

```c
#include <zephyr/bluetooth/gatt.h>
```

通知完成结果回调（Notification Complete Result Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `user_data` | 用户传入的数据（Data）。 |

<a id="ga1294850e6bdcbe7a8f42f2956fd837a8"></a>

### `bt_gatt_indicate_func_t`

```c
typedef void(* bt_gatt_indicate_func_t) (struct bt_conn *conn, struct bt_gatt_indicate_params *params, uint8_t err)
```

```c
#include <zephyr/bluetooth/gatt.h>
```

指示完成结果回调（Indication Complete Result Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `params` | 指示参数对象（Indication Parameters Object）。 |
| `err` | ATT 错误码（Error Code）。 |

<a id="ga5d47ed9eaea22c8f00db14329daee8fe"></a>

### `bt_gatt_indicate_params_destroy_t`

```c
typedef void(* bt_gatt_indicate_params_destroy_t) (struct bt_gatt_indicate_params *params)
```

```c
#include <zephyr/bluetooth/gatt.h>
```

用于销毁或清理 GATT 指示值参数（Indicate Value Parameters）的回调。

GATT 指示（Indication）操作完成后，将调用此回调函数清理与 `bt_gatt_indicate_params` 结构关联的全部资源。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `params` | 指向待清理的 GATT 指示参数（Indicate Parameters）结构的指针。 |

<a id="gab38994257f53473e62e01eff8f236ee1"></a>

### `bt_gatt_iter`

```c
enum bt_gatt_iter
```

```c
#include <zephyr/bluetooth/gatt.h>
```

用作 bt_gatt_attr_func_t 和 bt_gatt_read_func_t 类型回调的返回值（Return Values）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_GATT_ITER_STOP` |  |
| `BT_GATT_ITER_CONTINUE` |  |

<a id="ga2d51136ea1bd6cdb50900639506fd9f7"></a>

### `bt_gatt_attr_get_handle()`

```c
uint16_t bt_gatt_attr_get_handle ( const struct bt_gatt_attr * attr)
```

```c
#include <zephyr/bluetooth/gatt.h>
```

获取属性句柄（Attribute Handle）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `attr` | 当前已在本地属性协议（ATT）服务器注册的属性对象（Attribute Object）。 |

**返回（Returns）**：返回值：相应属性的句柄（Handle）；找不到该属性时为 0。

<a id="ga35cecaa43b00b374062d29cca1479d85"></a>

### `bt_gatt_attr_next()`

```c
struct bt_gatt_attr * bt_gatt_attr_next ( const struct bt_gatt_attr * attr)
```

```c
#include <zephyr/bluetooth/gatt.h>
```

迭代到下一个属性（Attribute）。

迭代到给定属性之后的下一个属性（Attribute）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `attr` | 当前属性（Current Attribute）。 |

**返回（Returns）**：返回值：下一个属性（Attribute）；找不到时为 `NULL`。

<a id="gaf6d253849932b706ec7f303568980dfa"></a>

### `bt_gatt_attr_read()`

```c
ssize_t bt_gatt_attr_read ( struct bt_conn * conn, const struct bt_gatt_attr * attr, void * buf, uint16_t buf_len, uint16_t offset, const void * value, uint16_t value_len )
```

```c
#include <zephyr/bluetooth/gatt.h>
```

通用属性值读取辅助函数（Generic Read Attribute Value Helper）。

从本地数据库（Local Database）读取属性值，并将结果存入缓冲区（Buffer）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `attr` | 要读取的属性（Attribute）。 |
| `buf` | 用于存储值的缓冲区（Buffer）。 |
| `buf_len` | 缓冲区长度。 |
| `offset` | 起始偏移量（Start Offset）。 |
| `value` | 属性值（Attribute Value）。 |
| `value_len` | 属性值（Attribute Value）的长度。 |

**返回（Returns）**：返回值：成功时为读取的字节数，出错时为负值。

<a id="ga2e85b42136e2c6a4cb5b7ad8a2532573"></a>

### `bt_gatt_attr_read_ccc()`

```c
ssize_t bt_gatt_attr_read_ccc ( struct bt_conn * conn, const struct bt_gatt_attr * attr, void * buf, uint16_t len, uint16_t offset )
```

```c
#include <zephyr/bluetooth/gatt.h>
```

客户端特征配置属性读取辅助函数（Read Client Characteristic Configuration Attribute Helper）。

从本地数据库读取 CCC 属性值，编码后将结果存入缓冲区（Buffer）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `attr` | 要读取的属性（Attribute）。 |
| `buf` | 用于存储读取值的缓冲区（Buffer）。 |
| `len` | 缓冲区长度。 |
| `offset` | 起始偏移量（Start Offset）。 |

**返回（Returns）**：返回值：成功时为读取的字节数，出错时为负值。

<a id="ga5893166f1b24f437a94ccf1fc57c7917"></a>

### `bt_gatt_attr_read_cep()`

```c
ssize_t bt_gatt_attr_read_cep ( struct bt_conn * conn, const struct bt_gatt_attr * attr, void * buf, uint16_t len, uint16_t offset )
```

```c
#include <zephyr/bluetooth/gatt.h>
```

特征扩展属性读取辅助函数（Read Characteristic Extended Properties Attribute Helper）。

从本地数据库读取 CEP 属性值，编码后将结果存入缓冲区（Buffer）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `attr` | 要读取的属性（Attribute）。 |
| `buf` | 用于存储读取值的缓冲区（Buffer）。 |
| `len` | 缓冲区长度。 |
| `offset` | 起始偏移量（Start Offset）。 |

**说明（Note）**：注意：仅用于 `user_data` 类型为 `bt_gatt_cep` 的属性（Attribute）。

**返回（Returns）**：返回值：成功时为读取的字节数，出错时为负值。

<a id="gad58b526a06334530c13292d14a11257c"></a>

### `bt_gatt_attr_read_chrc()`

```c
ssize_t bt_gatt_attr_read_chrc ( struct bt_conn * conn, const struct bt_gatt_attr * attr, void * buf, uint16_t len, uint16_t offset )
```

```c
#include <zephyr/bluetooth/gatt.h>
```

特征属性读取辅助函数（Read Characteristic Attribute Helper）。

从本地数据库读取特征属性（Characteristic Attribute）值，编码后将结果存入缓冲区。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `attr` | 要读取的属性（Attribute）。 |
| `buf` | 用于存储读取值的缓冲区（Buffer）。 |
| `len` | 缓冲区长度。 |
| `offset` | 起始偏移量（Start Offset）。 |

**说明（Note）**：注意：仅用于 `user_data` 类型为 `bt_gatt_chrc` 的属性（Attribute）。

**返回（Returns）**：返回值：成功时为读取的字节数，出错时为负值。

<a id="ga5ae96590a0aaa5c4c3863a4a14d80fdd"></a>

### `bt_gatt_attr_read_cpf()`

```c
ssize_t bt_gatt_attr_read_cpf ( struct bt_conn * conn, const struct bt_gatt_attr * attr, void * buf, uint16_t len, uint16_t offset )
```

```c
#include <zephyr/bluetooth/gatt.h>
```

特征呈现格式描述符属性读取辅助函数（Read Characteristic Presentation Format Descriptor Attribute Helper）。

从本地数据库读取 CPF 属性值，编码后将结果存入缓冲区（Buffer）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `attr` | 要读取的属性（Attribute）。 |
| `buf` | 用于存储读取值的缓冲区（Buffer）。 |
| `len` | 缓冲区长度。 |
| `offset` | 起始偏移量（Start Offset）。 |

**说明（Note）**：注意：仅用于 `user_data` 类型为 `bt_gatt_cpf` 的属性（Attribute）。

**返回（Returns）**：返回值：成功时为读取的字节数，出错时为负值。

<a id="ga29421c8788b47b6a648704d27d5f0d28"></a>

### `bt_gatt_attr_read_cud()`

```c
ssize_t bt_gatt_attr_read_cud ( struct bt_conn * conn, const struct bt_gatt_attr * attr, void * buf, uint16_t len, uint16_t offset )
```

```c
#include <zephyr/bluetooth/gatt.h>
```

特征用户描述描述符属性读取辅助函数（Read Characteristic User Description Descriptor Attribute Helper）。

从本地数据库读取 CUD 属性值，编码后将结果存入缓冲区（Buffer）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `attr` | 要读取的属性（Attribute）。 |
| `buf` | 用于存储读取值的缓冲区（Buffer）。 |
| `len` | 缓冲区长度。 |
| `offset` | 起始偏移量（Start Offset）。 |

**说明（Note）**：注意：仅用于 `user_data` 为以空字符结尾的 C 字符串的属性（Attribute）。

**返回（Returns）**：返回值：成功时为读取的字节数，出错时为负值。

<a id="ga4313a63decac2c8b7c4a1764df3d53ea"></a>

### `bt_gatt_attr_read_included()`

```c
ssize_t bt_gatt_attr_read_included ( struct bt_conn * conn, const struct bt_gatt_attr * attr, void * buf, uint16_t len, uint16_t offset )
```

```c
#include <zephyr/bluetooth/gatt.h>
```

包含属性读取辅助函数（Read Include Attribute Helper）。

从本地数据库读取包含服务属性（Include Service Attribute）值，编码后将结果存入缓冲区。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `attr` | 要读取的属性（Attribute）。 |
| `buf` | 用于存储读取值的缓冲区（Buffer）。 |
| `len` | 缓冲区长度。 |
| `offset` | 起始偏移量（Start Offset）。 |

**说明（Note）**：注意：仅用于 `user_data` 类型为 `bt_gatt_include` 的属性。若 `attr` 或 `attr->user_data` 为 `NULL`，函数返回 `EINVAL`。

**返回（Returns）**：返回值：成功时为读取的字节数，出错时为负值。

<a id="gacae81c0f272bad7e6ac93c0d13b678c6"></a>

### `bt_gatt_attr_read_service()`

```c
ssize_t bt_gatt_attr_read_service ( struct bt_conn * conn, const struct bt_gatt_attr * attr, void * buf, uint16_t len, uint16_t offset )
```

```c
#include <zephyr/bluetooth/gatt.h>
```

服务属性读取辅助函数（Read Service Attribute Helper）。

从本地数据库读取服务属性（Service Attribute）值，编码后将结果存入缓冲区。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `attr` | 要读取的属性（Attribute）。 |
| `buf` | 用于存储读取值的缓冲区（Buffer）。 |
| `len` | 缓冲区长度。 |
| `offset` | 起始偏移量（Start Offset）。 |

**说明（Note）**：注意：仅用于 `user_data` 类型为 `bt_uuid` 的属性（Attribute）。

**返回（Returns）**：返回值：成功时为读取的字节数，出错时为负值。

<a id="ga99738cf4f05eae4c6da17cc3420827d8"></a>

### `bt_gatt_attr_value_handle()`

```c
uint16_t bt_gatt_attr_value_handle ( const struct bt_gatt_attr * attr)
```

```c
#include <zephyr/bluetooth/gatt.h>
```

获取特征值描述符（Characteristic Value Descriptor）的句柄。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `attr` | 一个特征属性（Characteristic Attribute）。 |

**说明（Note）**：注意：此属性的 `user_data` 必须为 `bt_gatt_chrc` 类型，`uuid` 应为 `BT_UUID_GATT_CHRC`。

**返回（Returns）**：返回值：相应特征值（Characteristic Value）的句柄。如果 `attr` 不是特征属性，则返回 0，即无效句柄。

<a id="gabba965b676650a55cb9934072b34c75e"></a>

### `bt_gatt_attr_write_ccc()`

```c
ssize_t bt_gatt_attr_write_ccc ( struct bt_conn * conn, const struct bt_gatt_attr * attr, const void * buf, uint16_t len, uint16_t offset, uint8_t flags )
```

```c
#include <zephyr/bluetooth/gatt.h>
```

客户端特征配置属性写入辅助函数（Write Client Characteristic Configuration Attribute Helper）。

将缓冲区中的值写入 CCC 属性。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `attr` | 要读取的属性（Attribute）。 |
| `buf` | 用于存储读取值的缓冲区（Buffer）。 |
| `len` | 缓冲区长度。 |
| `offset` | 起始偏移量（Start Offset）。 |
| `flags` | 写入标志（Write Flags），参见 `bt_gatt_attr_write_flag`。 |

**返回（Returns）**：返回值：成功时为写入的字节数，出错时为负值。

<a id="ga5eee6afc6db391ffeda295d298bf6a56"></a>

### `bt_gatt_authorization_cb_register()`

```c
int bt_gatt_authorization_cb_register ( const struct bt_gatt_authorization_cb * cb)
```

```c
#include <zephyr/bluetooth/gatt.h>
```

注册 GATT 授权回调（Authorization Callbacks）。

注册回调，以便对全部已注册 GATT 属性上的 GATT 操作执行应用程序特定的授权（Authorization）。在蓝牙子系统（Bluetooth Subsystem）处于活动状态的整个期间，回调结构必须始终有效。

必须启用 Kconfig 选项 `CONFIG_BT_GATT_AUTHORIZATION_CUSTOM`，此 API 才能发挥作用。

此 API 同一时间只允许注册一个回调结构（Callback Structure）。传入 `NULL` 会注销之前的回调集合，之后即可注册新的回调集合。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 回调结构体（Callback Struct）。 |

**返回（Returns）**：返回值（Returns）：成功时为零，否则返回负错误码。

<a id="ga270c8a52bf3d512defc373f8c29b59f2"></a>

### `bt_gatt_cb_register()`

```c
void bt_gatt_cb_register ( struct bt_gatt_cb * cb)
```

```c
#include <zephyr/bluetooth/gatt.h>
```

注册 GATT 回调（Callbacks）。

注册用于监控 GATT 状态的回调（Callbacks）。回调结构必须在程序余下的运行期间始终有效。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 回调结构体（Callback Struct）。 |

<a id="ga5fb25c5eec91045dc4c7fd61ef7e528e"></a>

### `bt_gatt_cb_unregister()`

```c
int bt_gatt_cb_unregister ( struct bt_gatt_cb * cb)
```

```c
#include <zephyr/bluetooth/gatt.h>
```

注销 GATT 回调（Callbacks）。

注销用于监控 GATT 状态的回调（Callbacks）。提供的回调结构应为之前已注册的结构。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 回调结构体（Callback Struct）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="gaf6d3f1e904f1a847afeb30236bad98a2"></a>

### `bt_gatt_err_to_str()`

```c
const char * bt_gatt_err_to_str ( int gatt_err)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/bluetooth/gatt.h>
```

将 GATT 错误转换为字符串（String）。

GATT 错误使用 `BT_GATT_ERR` 创建。

错误码（Error Codes）在《蓝牙核心规范》（Bluetooth Core Specification）第 3 卷 F 部分第 3.4.1.1 节中描述。

卷 4、F 部分和 G 部分中的 ATT 与 GATT 文档说明不同错误码的使用场景。

另请参阅已定义的 BT_ATT_ERR_* 宏。

**返回（Returns）**：返回值：GATT 错误码（Error Code）的字符串表示。如果未启用 `CONFIG_BT_ATT_ERR_TO_STR`，则仅返回空字符串。

<a id="gad2f3272b1dc42378104b492ec7caf6b0"></a>

### `bt_gatt_find_by_uuid()`

```c
struct bt_gatt_attr * bt_gatt_find_by_uuid ( const struct bt_gatt_attr * attr, uint16_t attr_count, const struct bt_uuid * uuid )
```

```c
#include <zephyr/bluetooth/gatt.h>
```

按 UUID 查找属性（Attribute）。

查找 UUID 匹配的属性。要将搜索限制在某个服务内，将 `attr` 设为该服务的属性，将 `attr_count` 设为该服务的属性数量。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `attr` | 指向一个属性的指针，以此属性为起点搜索匹配的 UUID。传入 `NULL` 时搜索整个范围。 |
| `attr_count` | 从起点开始搜索 UUID 匹配项时检查的属性数量。设为 0 时搜索到末尾。 |
| `uuid` | 要匹配的 UUID。 |

<a id="gaa93b5e0f2870ed135447bead903c175a"></a>

### `bt_gatt_foreach_attr()`

```c
void bt_gatt_foreach_attr ( uint16_t start_handle, uint16_t end_handle, bt_gatt_attr_func_t func, void * user_data )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/bluetooth/gatt.h>
```

属性迭代器（Attribute Iterator）。

迭代指定范围内的属性（Attributes）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `start_handle` | 起始属性句柄（Starting Attribute Handle）。 |
| `end_handle` | 结束属性句柄（Ending Attribute Handle）。 |
| `func` | 回调函数（Callback function）。 |
| `user_data` | 传给回调（Callback）的数据。 |

<a id="gad8d8f513004f391167212d7bf9f7ff10"></a>

### `bt_gatt_foreach_attr_type()`

```c
void bt_gatt_foreach_attr_type ( uint16_t start_handle, uint16_t end_handle, const struct bt_uuid * uuid, const void * attr_data, uint16_t num_matches, bt_gatt_attr_func_t func, void * user_data )
```

```c
#include <zephyr/bluetooth/gatt.h>
```

按类型遍历的属性迭代器（Attribute Iterator by Type）。

迭代指定范围内与给定 UUID 和／或数据匹配的属性（Attributes）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `start_handle` | 起始属性句柄（Start Attribute Handle）。 |
| `end_handle` | 结束属性句柄（End Attribute Handle）。通常设为 `start_handle + attr_count` 或 `BT_ATT_LAST_ATTRIBUTE_HANDLE`。 |
| `uuid` | 要匹配的 UUID；传入 `NULL` 则跳过 UUID 匹配。 |
| `attr_data` | 要匹配的属性数据（Attribute Data）；传入 `NULL` 则跳过数据匹配。 |
| `num_matches` | 匹配数量（Number of Matches）；传入 0 则不限制数量。 |
| `func` | 回调函数（Callback function）。 |
| `user_data` | 传给回调（Callback）的数据。 |

<a id="ga351fd7658eaecbbfa60f1769119ef733"></a>

### `bt_gatt_get_mtu()`

```c
uint16_t bt_gatt_get_mtu ( struct bt_conn * conn)
```

```c
#include <zephyr/bluetooth/gatt.h>
```

获取连接的 ATT 最大传输单元（MTU）。

获取协商后的 ATT 连接最大传输单元（MTU）。注意：该值不等于单个数据包可传输的最大属性数据量。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |

**返回（Returns）**：返回值：最大传输单元（MTU），单位为字节。

<a id="ga6653de5e245cae6dc12cd0b45acbe028"></a>

### `bt_gatt_get_uatt_mtu()`

```c
uint16_t bt_gatt_get_uatt_mtu ( struct bt_conn * conn)
```

```c
#include <zephyr/bluetooth/gatt.h>
```

获取连接的非增强属性协议（Unenhanced ATT，UATT）的 MTU。

获取未增强属性协议（Unenhanced ATT，UATT）连接的最大传输单元（MTU）。

`ATT_MTU` 定义 ATT 协议数据单元（PDU）的最大大小，包括 ATT 操作码（Opcode）、附加字段和属性值载荷（Attribute Value Payload）。因此，值载荷的最大大小更小，并随 ATT PDU 类型变化。例如，在 `ATT_HANDLE_VALUE_NTF` PDU 中，属性值字段最多可包含 `ATT_MTU - 3` 个八位字节；减去的 3 个八位字节用于操作码和句柄。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |

**返回（Returns）**：返回值：当前 UATT 的 `ATT_MTU`；如果 `conn` 没有 UATT `ATT_MTU`，例如已断开连接，则返回 0。

<a id="ga4f2272692cc0f1d44638828012296c80"></a>

### `bt_gatt_indicate()`

```c
int bt_gatt_indicate ( struct bt_conn * conn, struct bt_gatt_indicate_params * params )
```

```c
#include <zephyr/bluetooth/gatt.h>
```

发送属性值变化指示（Indicate Attribute Value Change）。

发送属性值变化的指示（Indication）。如果连接为 `NULL`，向所有通过 CCC 启用通知的对端发送指示；否则，仅直接向给定连接发送指示。

参数中的属性对象可以是特征声明（Characteristic Declaration），通常通过 `BT_GATT_CHARACTERISTIC` 声明，后接 `BT_GATT_CCC`；也可以是特征值声明（Characteristic Value Declaration），使用 `BT_GATT_CHARACTERISTIC` 时会自动创建在特征声明之后。

也可在参数中设置 UUID，按 UUID 发送指示（Indication）。采用此方法时，如果同时提供属性，则以该属性作为查找可能匹配项的范围起点。

值的长度受 `bt_att_get_max_indicate_size` 报告的最大指示值大小（Maximum Indication Value Size）限制；超过限制时，调用者必须截断它。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `params` | 指示参数（Indicate Parameters）。 |

**说明（Note）**：注意：此过程为异步（Asynchronous）过程，因此在其活动期间，参数必须始终有效。过程保持活动状态，直到执行 `destroy` 回调。

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="gabd4df0a264dae10e43797992a567be7d"></a>

### `bt_gatt_is_subscribed()`

```c
bool bt_gatt_is_subscribed ( struct bt_conn * conn, const struct bt_gatt_attr * attr, uint16_t ccc_type )
```

```c
#include <zephyr/bluetooth/gatt.h>
```

检查连接是否已订阅（Subscribed）该属性。

检查连接是否订阅了属性值变化（Attribute Value Change）。

属性对象可以是特征声明（Characteristic Declaration），通常通过 `BT_GATT_CHARACTERISTIC` 声明，后接 `BT_GATT_CCC`；也可以是使用 `BT_GATT_CHARACTERISTIC` 时自动创建在特征声明之后的特征值声明（Characteristic Value Declaration）；还可以是 `BT_GATT_CCC` 创建的客户端特征配置描述符（Client Characteristic Configuration Descriptor，CCCD）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `attr` | 属性对象（Attribute Object）。 |
| `ccc_type` | 订阅类型（Subscription Type），为 `BT_GATT_CCC_NOTIFY` 和／或 `BT_GATT_CCC_INDICATE`。 |

**返回（Returns）**：返回值：该属性对象已被订阅时为 `true`。

<a id="ga74ee552864c563aa5bc939f37395c14a"></a>

### `bt_gatt_notify()`

```c
int bt_gatt_notify ( struct bt_conn * conn, const struct bt_gatt_attr * attr, const void * data, uint16_t len )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/bluetooth/gatt.h>
```

发送属性值变化通知（Notify Attribute Value Change）。

发送属性值变化的通知（Notification）。如果连接为 `NULL`，通知所有通过 CCC 启用通知的对端；否则，仅直接通知给定连接。

参数中的属性对象可以是特征声明（Characteristic Declaration），通常通过 `BT_GATT_CHARACTERISTIC` 声明，后接 `BT_GATT_CCC`；也可以是特征值声明（Characteristic Value Declaration），使用 `BT_GATT_CHARACTERISTIC` 时会自动创建在特征声明之后。

值的长度受 `bt_att_get_max_notify_size` 报告的最大通知值大小（Maximum Notification Value Size）限制；超过限制时，调用者必须截断它。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `attr` | 特征（Characteristic）或特征值（Characteristic Value）属性。 |
| `data` | 指向属性数据（Attribute Data）的指针。 |
| `len` | 属性值长度（Attribute Value Length）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga55e3ef7cb43b8acb0a27643c78390146"></a>

### `bt_gatt_notify_cb()`

```c
int bt_gatt_notify_cb ( struct bt_conn * conn, struct bt_gatt_notify_params * params )
```

```c
#include <zephyr/bluetooth/gatt.h>
```

发送属性值变化通知（Notify Attribute Value Change）。

此函数的工作方式与 `bt_gatt_notify` 相同，另外还会在发送通知（Notification）后调用回调函数。

回调在线程上下文（Thread Context）运行，绝不在中断服务程序（ISR）中运行；参见回调执行上下文（Callback Execution Contexts）。从系统工作队列上下文（System Workqueue Context）调用时，此 API 不会等待供回调使用的资源，而会返回错误。

也可在参数中设置 UUID，按 UUID 发送通知（Notification）。采用此方法时，如果同时提供属性，则以该属性作为查找可能匹配项的范围起点。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `params` | 通知参数（Notification Parameters）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga8071d6063f85c0a78155f6b2ac2da635"></a>

### `bt_gatt_notify_multiple()`

```c
int bt_gatt_notify_multiple ( struct bt_conn * conn, uint16_t num_params, struct bt_gatt_notify_params params[] )
```

```c
#include <zephyr/bluetooth/gatt.h>
```

在一个协议数据单元（PDU）中发送多个通知（Notifications）。

GATT 服务器将发送一个 `ATT_MULTIPLE_HANDLE_VALUE_NTF` 协议数据单元（PDU），其中包含传递给此 API 的所有通知。

受实现限制，所有 `params` 必须具有相同的 `func` 和 `user_data`；但每个参数都会分别触发一次 `func(user_data)` 调用。

此 API 可能阻塞以等待蓝牙主机（Bluetooth Host）资源，因此不建议从协作式线程（Cooperative Thread）或蓝牙回调中调用它。

使用此 API 之前，对端的 GATT 客户端必须写入本设备的客户端支持特性（Client Supported Features）属性，并设置多句柄值通知（Multiple Handle Value Notifications）对应的位。

仅在需要强制使用 `ATT_MULTIPLE_HANDLE_VALUE_NTF` PDU 时才使用此 API。普通应用程序优先使用 `bt_gatt_notify_cb`：它会在对端支持时使用此 PDU，在对端不支持时自动回退为 `ATT_HANDLE_VALUE_NTF`。

此 API 还有一个限制：它仅接受有效属性引用（Attribute References），不像 `bt_gatt_notify` 和 `bt_gatt_notify_cb` 那样接受 UUID。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 目标客户端（Target Client）。目前尚不支持通过传入 `NULL` 通知全部已连接客户端；请改用 `bt_gatt_notify`。 |
| `num_params` | `params` 数组的元素数量，必须大于 1。 |
| `params` | 通知参数数组（Notification Parameters Array）。调用此函数后即可释放该数组。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。协议数据单元（PDU）已进入发送队列。 |
| `-EINVAL` | 某个属性句柄（Attribute Handle）无效；仅传入了一个参数，而此 API 要求至少两个；并非所有 `func` 相同，或并非所有 `user_data` 相同；某个特征不支持通知；或某个参数传入了 UUID。 |
| `-ERANGE` | 所有通知无法装入单个 `ATT_MULTIPLE_HANDLE_VALUE_NTF`；其总长度超过所有已打开 ATT 承载（Bearers）的最大传输单元（MTU）。 |
| `-EPERM` | 连接的安全级别（Security Level）低于某个属性的要求。 |
| `-EOPNOTSUPP` | 对端尚未告知其支持此协议数据单元（PDU）类型。 |

<a id="ga24bae284dbc71cd4075649c4bc348b7c"></a>

### `bt_gatt_notify_uuid()`

```c
int bt_gatt_notify_uuid ( struct bt_conn * conn, const struct bt_uuid * uuid, const struct bt_gatt_attr * attr, const void * data, uint16_t len )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/bluetooth/gatt.h>
```

按 UUID 发送属性值变化通知（Notify Attribute Value Change）。

发送属性值变化的通知（Notification）。如果连接为 `NULL`，通知所有通过 CCC 启用通知的对端；否则，仅直接通知给定连接。

此属性对象（Attribute Object）是搜索 UUID 的起点。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `uuid` | UUID。如果服务器中存在多个具有相同 UUID 的服务，则采用从给定 `attr` 开始找到的第一个匹配项。 |
| `attr` | 指向一个属性的指针，以此属性为起点搜索匹配的 UUID。 |
| `data` | 指向属性数据（Attribute Data）的指针。 |
| `len` | 属性值长度（Attribute Value Length）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="gae5c1e8b7bb1e673e228f03d1d084be9a"></a>

### `bt_gatt_service_is_registered()`

```c
bool bt_gatt_service_is_registered ( const struct bt_gatt_service * svc)
```

```c
#include <zephyr/bluetooth/gatt.h>
```

检查 GATT 服务（Service）是否已注册。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `svc` | 要检查的服务（Service）。 |

**返回（Returns）**：返回值：已注册时为 `true`，未注册时为 `false`。

<a id="gab4d9cfea04e44445d5dc30ad52842b64"></a>

### `bt_gatt_service_register()`

```c
int bt_gatt_service_register ( struct bt_gatt_service * svc)
```

```c
#include <zephyr/bluetooth/gatt.h>
```

注册 GATT 服务（Service）。

应用程序可以使用 `BT_GATT_PRIMARY_SERVICE`、`BT_GATT_CHARACTERISTIC`、`BT_GATT_DESCRIPTOR` 等宏注册 GATT 服务（Service）。

使用 `CONFIG_BT_SETTINGS` 时，凡是需要加载绑定配置（Bond Configuration），即 CCC 值的服务，都必须在调用 `settings_load` 之前注册。

同时使用 `CONFIG_BT_GATT_CACHING` 和 `CONFIG_BT_SETTINGS` 时，凡是应纳入 GATT 数据库哈希（Database Hash）计算的服务，都应在调用 `settings_load` 之前添加。在 `settings_load` 之后注册的所有服务都会触发新的数据库哈希计算，并存储新的哈希。

此函数可以在两种情况下调用：调用 `bt_init()` 之前，或调用 `settings_load()` 之后。不支持在两者之间注册服务（Service），否则会返回错误。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `svc` | 包含可用属性（Attributes）的服务。 |

**返回（Returns）**：返回值：成功时为 0，出错时为负值。如果已调用 `bt_init()` 但尚未调用 `settings_load()`，则返回 `-EAGAIN`。

<a id="gaf5bf0205fad5f7ad187b764d23deba6b"></a>

### `bt_gatt_service_unregister()`

```c
int bt_gatt_service_unregister ( struct bt_gatt_service * svc)
```

```c
#include <zephyr/bluetooth/gatt.h>
```

注销 GATT 服务（Service）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `svc` | 要注销的服务（Service）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。


## 3.7\_原页交叉引用（Cross References）

- [bt_gatt_ccc_cfg](../bluetooth_connection_model_reference/P053_bt_gatt_ccc_cfg_结构体.md)
- [bt_gatt_ccc_managed_user_data](../bluetooth_connection_model_reference/P054_bt_gatt_ccc_managed_user_data_结构体.md)
- [bt_gatt_notify_params](../bluetooth_connection_model_reference/P062_bt_gatt_notify_params_结构体.md)
- [bt_gatt_indicate_params](../bluetooth_connection_model_reference/P061_bt_gatt_indicate_params_结构体.md)
- [CONFIG_BT_SETTINGS_CCC_LAZY_LOADING](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SETTINGS_CCC_LAZY_LOADING)
- [CONFIG_BT_CONN](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CONN)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_gatt_attr](../bluetooth_connection_model_reference/P049_bt_gatt_attr_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_gatt_read_func_t](../api_socket_lora_topic_reference/P005_GATT 客户端 API.md#ga1ca94b4f2b6c456b6134e05127993569)
- [bt_gatt_cb](../bluetooth_connection_model_reference/P051_bt_gatt_cb_结构体.md)
- [bt_gatt_authorization_cb](../bluetooth_connection_model_reference/P050_bt_gatt_authorization_cb_结构体.md)
- [bt_gatt_service](../bluetooth_connection_model_reference/P065_bt_gatt_service_结构体.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [bt_uuid](../bluetooth_connection_model_reference/P131_bt_uuid_结构体.md)
- [uuid](../data_utilities/P026_UUID二进制结构.md)
- [ssize_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)
- [标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [zephyr/bluetooth/gatt.h](../api_file_bluetooth_media_reference/P004_zephyr__bluetooth__gatt.h_文件参考.md)
- [bt_gatt_perm](../api_media_cellular_topic_reference/P003_通用属性配置文件（Generic Attribute Profile，GATT）.md#ga96e57500d2340a45badb23701cc43833)
- [bt_gatt_attr_read_func_t](../api_media_cellular_topic_reference/P003_通用属性配置文件（Generic Attribute Profile，GATT）.md#ga57e36bf94652531964fd4237c203fe7b)
- [bt_gatt_attr_write_func_t](../api_media_cellular_topic_reference/P003_通用属性配置文件（Generic Attribute Profile，GATT）.md#ga3fd8527a0f3e8f3699dc0d3b0339eba1)
- [客户端特征配置 UUID（Client Characteristic Configuration UUID）：`BT_UUID_GATT_CCC`。](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga03a2d3f0ce89508b794d5c87a4303057)
- [CONFIG_BT_MAX_CONN](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MAX_CONN)
- [CONFIG_BT_MAX_PAIRED](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MAX_PAIRED)
- [特征扩展属性 UUID（Characteristic Extended Properties UUID）：`BT_UUID_GATT_CEP`。](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6aa143b721d810f1536d7431a9bf7cc7)
- [BT_GATT_PERM_READ](../api_media_cellular_topic_reference/P003_通用属性配置文件（Generic Attribute Profile，GATT）.md#gga96e57500d2340a45badb23701cc43833a9afb838c2cef657e9cd035ef27521f17)
- [类型（Type）：`bt_gatt_cep`。](../bluetooth_connection_model_reference/P055_bt_gatt_cep_结构体.md)
- [BT_UUID_GATT_CHRC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gadcedbbe1c432c4ac737e54b318e01a0f)
- [类型（Type）：`bt_gatt_chrc`。](../bluetooth_connection_model_reference/P056_bt_gatt_chrc_结构体.md)
- [特征呈现格式 UUID（Characteristic Presentation Format UUID）：`BT_UUID_GATT_CPF`。](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga331a61702ffe9b15bac0de3d60414022)
- [类型（Type）：`bt_gatt_cpf`。](../bluetooth_connection_model_reference/P057_bt_gatt_cpf_结构体.md)
- [BT_UUID_GATT_CUD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaaaf94f5d918a1b6715cf4816b03875a2)
- [BT_UUID_GATT_INCLUDE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga995596ff7374ebcb44d4706bc16234e4)
- [BT_UUID_GATT_PRIMARY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6e87ce1575494eb90358e074e8dbe276)
- [BT_UUID_GATT_SECONDARY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad084d3658e663b6b8e200be256c54cdb)
- [ARRAY_SIZE](../util_reference/P001_通用工具公共接口.md#ga70c57aae3eb654e205459b4362c8089a)
- [STRUCT_SECTION_ITERABLE](../iterable_reference/P001_可遍历段公共接口.md#ga9104f42cbe4a67a931bed7f7cc8f600f)
- [bt_gatt_service_static](../bluetooth_connection_model_reference/P066_bt_gatt_service_static_结构体.md)
- [类型（Type）：`bt_gatt_include`。](../bluetooth_connection_model_reference/P060_bt_gatt_include_结构体.md)
- [bt_gatt_attr_write_flag](../api_media_cellular_topic_reference/P003_通用属性配置文件（Generic Attribute Profile，GATT）.md#ga830d437c8d0757f53af1de6aa3031906)
- [CONFIG_BT_GATT_AUTHORIZATION_CUSTOM](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_GATT_AUTHORIZATION_CUSTOM)
- [BT_GATT_ERR](../api_media_cellular_topic_reference/P003_通用属性配置文件（Generic Attribute Profile，GATT）.md#gaff31756c1bf8ee755e65b1e0fb689bb7)
- [CONFIG_BT_ATT_ERR_TO_STR](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ATT_ERR_TO_STR)
- [bt_att_get_max_indicate_size](../api_memory_network_topic_reference/P002_属性协议（Attribute Protocol，ATT）.md#ga2edca82fff038f16e6f7d09bc1db59a8)
- [BT_GATT_CCC_NOTIFY](../api_media_cellular_topic_reference/P003_通用属性配置文件（Generic Attribute Profile，GATT）.md#ga240a10df32aa7a256a103ceee7211f8d)
- [BT_GATT_CCC_INDICATE](../api_media_cellular_topic_reference/P003_通用属性配置文件（Generic Attribute Profile，GATT）.md#ga60ff2ddcc2e3148881a2f15745ba06e8)
- [bt_att_get_max_notify_size](../api_memory_network_topic_reference/P002_属性协议（Attribute Protocol，ATT）.md#ga653a0fc8803d7deebb0be93c8cf7910a)
- [回调执行上下文（Callback execution contexts）](../bluetooth/P004_低功耗蓝牙主机.md#bluetooth-callback-contexts)
- [CONFIG_BT_SETTINGS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SETTINGS)
- [settings_load](https://docs.zephyrproject.org/latest/doxygen/html/group__settings.html#ga89c6d618df81f197cc5c1a2018b00648)
- [CONFIG_BT_GATT_CACHING](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_GATT_CACHING)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__bt__gatt__server_html_gad8b296ecfd1139680f21da7904b9f585"></a>
<a id="astructbt__gatt__ccc__managed__user__data_html"></a>
<a id="agroup__bt__gatt__server_html_ga2e85b42136e2c6a4cb5b7ad8a2532573"></a>
<a id="agroup__bt__gatt__server_html_gabba965b676650a55cb9934072b34c75e"></a>
<a id="agroup__bt__gatt__server_html_gac4abfeb068d16dcdaceee812c12bf406"></a>
<a id="agroup__bt__uuid_html_ga03a2d3f0ce89508b794d5c87a4303057"></a>
<a id="agroup__bt__gatt__server_html_ga5893166f1b24f437a94ccf1fc57c7917"></a>
<a id="agroup__bt__gatt__server_html_ga83207fc083454327004f7d3c3e5b3840"></a>
<a id="agroup__bt__gatt_html_gga96e57500d2340a45badb23701cc43833a9afb838c2cef657e9cd035ef27521f17"></a>
<a id="agroup__bt__uuid_html_ga6aa143b721d810f1536d7431a9bf7cc7"></a>
<a id="agroup__bt__gatt__server_html_gad58b526a06334530c13292d14a11257c"></a>
<a id="agroup__bt__uuid_html_gadcedbbe1c432c4ac737e54b318e01a0f"></a>
<a id="astructbt__gatt__chrc_html"></a>
<a id="agroup__bt__gatt__server_html_ga5ae96590a0aaa5c4c3863a4a14d80fdd"></a>
<a id="agroup__bt__uuid_html_ga331a61702ffe9b15bac0de3d60414022"></a>
<a id="agroup__bt__gatt__server_html_ga29421c8788b47b6a648704d27d5f0d28"></a>
<a id="agroup__bt__uuid_html_gaaaf94f5d918a1b6715cf4816b03875a2"></a>
<a id="agroup__bt__gatt__server_html_ga4313a63decac2c8b7c4a1764df3d53ea"></a>
<a id="agroup__bt__uuid_html_ga995596ff7374ebcb44d4706bc16234e4"></a>
<a id="agroup__bt__gatt__server_html_gacae81c0f272bad7e6ac93c0d13b678c6"></a>
<a id="agroup__bt__uuid_html_ga6e87ce1575494eb90358e074e8dbe276"></a>
<a id="agroup__bt__uuid_html_gad084d3658e663b6b8e200be256c54cdb"></a>
<a id="agroup__sys-util_html_ga70c57aae3eb654e205459b4362c8089a"></a>
<a id="agroup__iterable__section__apis_html_ga9104f42cbe4a67a931bed7f7cc8f600f"></a>
<a id="astructbt__gatt__attr_html"></a>
<a id="astructbt__gatt__service__static_html"></a>
<a id="astructbt__gatt__service_html"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggab38994257f53473e62e01eff8f236ee1aa3f2a25e27c7065a2c7bb2a9ff09542e"></a>
<a id="ggab38994257f53473e62e01eff8f236ee1aea569feffa4815d3443e12be78c684f5"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P002_音频_视频远程控制配置文件（Audio Video Remote Control Profile，AVRCP）.md) · [返回大纲](大纲.md) · [下一章](P004_消息访问配置文件（Message Access Profile，MAP）.md)

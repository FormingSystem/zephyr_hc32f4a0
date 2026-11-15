---
id: learning.zephyr-docs.platform-security-model-reference.page-9
title: fido2_storage_api_结构体
kind: reference
status: maintained
domains: [zephyr, platform, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structfido2__storage__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_fido2\_storage\_api\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structfido2__storage__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

存储后端（Storage Backend）API。

```c
#include <zephyr/authentication/fido2/fido2_storage.h>
```

<a id="details"></a>

存储后端（Storage Backend）API。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 9.1\_数据成员（Data Fields）

<a id="r_a5a0ff58bbd5769839d45fe5dd8f32663"></a>

```c
int(* init )(void)
```

相关声明：[init](#a5a0ff58bbd5769839d45fe5dd8f32663)。

初始化存储后端（storage backend）。

<a id="r_a6e73c6a26dc5601d8936ce977e9061b1"></a>

```c
int(* store )(const struct fido2_credential *cred)
```

相关声明：[store](#a6e73c6a26dc5601d8936ce977e9061b1)、[fido2_credential](P007_fido2_credential_结构体.md)。

存储一项凭据。

<a id="r_a51e0d7161f98222bb587ad69f399256e"></a>

```c
int(* load )(const uint8_t *cred_id, size_t cred_id_len, struct fido2_credential *cred)
```

相关声明：[load](#a51e0d7161f98222bb587ad69f399256e)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[fido2_credential](P007_fido2_credential_结构体.md)。

按 ID 加载凭据。

<a id="r_a516702caaa10b783fbdbe6f6bf42ed96"></a>

```c
int(* remove )(const uint8_t *cred_id, size_t cred_id_len, struct fido2_credential *cred)
```

相关声明：[remove](#a516702caaa10b783fbdbe6f6bf42ed96)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[fido2_credential](P007_fido2_credential_结构体.md)。

按 ID 删除凭据。

<a id="r_a493ad305f851d7e71f53d27f596b5cec"></a>

```c
int(* find_by_rp )(const uint8_t rp_id_hash[32], struct fido2_credential *creds, size_t max_creds, size_t *count)
```

相关声明：[find_by_rp](#a493ad305f851d7e71f53d27f596b5cec)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[fido2_credential](P007_fido2_credential_结构体.md)。

按依赖方 ID 哈希查找凭据。

<a id="r_a11e569e7e42eb592e63de614bf3caea4"></a>

```c
int(* enumerate_rps )(size_t offset, struct fido2_credential *creds, size_t max_creds, size_t *count)
```

相关声明：[enumerate_rps](#a11e569e7e42eb592e63de614bf3caea4)、[fido2_credential](P007_fido2_credential_结构体.md)。

枚举已存储凭据中不重复的依赖方 ID（Relying Party IDs）。

<a id="r_a336bade2445fabab3f1583d2cced0932"></a>

```c
int(* iterate )(fido2_storage_iterate_cb_t cb, void *user_data)
```

相关声明：[iterate](#a336bade2445fabab3f1583d2cced0932)、[fido2_storage_iterate_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gad0f22c2a4c49fdd7b47ed0913115c5b2)。

遍历全部已存储凭据。

<a id="r_a7fdaf0829c6cacaba0e0e2966999c1fd"></a>

```c
int(* sign_count_increment )(const uint8_t *cred_id, size_t cred_id_len, uint32_t *new_count)
```

相关声明：[sign_count_increment](#a7fdaf0829c6cacaba0e0e2966999c1fd)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

递增签名计数器并返回其值。

<a id="r_a1c48cffc28698583435cb5fc5944b0a2"></a>

```c
int(* update_user_info )(const uint8_t *cred_id, size_t cred_id_len, const char *user_name, const char *user_display_name)
```

相关声明：[update_user_info](#a1c48cffc28698583435cb5fc5944b0a2)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

更新已有凭据的用户信息。

<a id="r_ab12cffb1e35e20105a118c3de6fca768"></a>

```c
int(* credential_count )(size_t *count)
```

相关声明：[credential_count](#ab12cffb1e35e20105a118c3de6fca768)。

获取已存储可发现凭据的总数。

<a id="r_a2aca20305a1b0919124231d5f62de79a"></a>

```c
int(* wipe_all )(void)
```

相关声明：[wipe_all](#a2aca20305a1b0919124231d5f62de79a)。

清除所有已存储凭据及 PIN 状态。

<a id="r_ad5d135ae94fd0d4feef3c815b0cbe213"></a>

```c
int(* pin_set )(const uint8_t pin_hash[16])
```

相关声明：[pin_set](#ad5d135ae94fd0d4feef3c815b0cbe213)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

存储 PIN 哈希。

<a id="r_a267cf93095b7d6c99f616cecbea71640"></a>

```c
int(* pin_get )(uint8_t pin_hash[16])
```

相关声明：[pin_get](#a267cf93095b7d6c99f616cecbea71640)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

加载已存储的 PIN 哈希。

<a id="r_a71cda9437a7abfc29644188addad3bec"></a>

```c
int(* pin_retries_get )(uint8_t *retries)
```

相关声明：[pin_retries_get](#a71cda9437a7abfc29644188addad3bec)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取剩余 PIN 重试次数。

<a id="r_aab707de64b5401fd8884f28c1d52b3af"></a>

```c
int(* pin_retries_decrement )(void)
```

相关声明：[pin_retries_decrement](#aab707de64b5401fd8884f28c1d52b3af)。

递减 PIN 重试计数器。

<a id="r_a72eac7fc7756ca6dbc53fe67d2161a93"></a>

```c
int(* pin_retries_reset )(void)
```

相关声明：[pin_retries_reset](#a72eac7fc7756ca6dbc53fe67d2161a93)。

将 PIN 重试计数器重置为最大值。

## 9.2\_详细说明（Detailed Documentation）

<a id="ab12cffb1e35e20105a118c3de6fca768"></a>

### `credential_count`

```c
int(* fido2_storage_api::credential_count) (size_t *count)
```

获取已存储可发现凭据的总数。

<a id="a11e569e7e42eb592e63de614bf3caea4"></a>

### `enumerate_rps`

```c
int(* fido2_storage_api::enumerate_rps) (size_t offset, struct fido2_credential *creds, size_t max_creds, size_t *count)
```

枚举已存储凭据中不重复的依赖方 ID（Relying Party IDs）。

<a id="a493ad305f851d7e71f53d27f596b5cec"></a>

### `find_by_rp`

```c
int(* fido2_storage_api::find_by_rp) (const uint8_t rp_id_hash[32], struct fido2_credential *creds, size_t max_creds, size_t *count)
```

按依赖方 ID 哈希查找凭据。

<a id="a5a0ff58bbd5769839d45fe5dd8f32663"></a>

### `init`

```c
int(* fido2_storage_api::init) (void)
```

初始化存储后端（storage backend）。

<a id="a336bade2445fabab3f1583d2cced0932"></a>

### `iterate`

```c
int(* fido2_storage_api::iterate) (fido2_storage_iterate_cb_t cb, void *user_data)
```

遍历全部已存储凭据。

<a id="a51e0d7161f98222bb587ad69f399256e"></a>

### `load`

```c
int(* fido2_storage_api::load) (const uint8_t *cred_id, size_t cred_id_len, struct fido2_credential *cred)
```

按 ID 加载凭据。

<a id="a267cf93095b7d6c99f616cecbea71640"></a>

### `pin_get`

```c
int(* fido2_storage_api::pin_get) (uint8_t pin_hash[16])
```

加载已存储的 PIN 哈希。

<a id="aab707de64b5401fd8884f28c1d52b3af"></a>

### `pin_retries_decrement`

```c
int(* fido2_storage_api::pin_retries_decrement) (void)
```

递减 PIN 重试计数器。

<a id="a71cda9437a7abfc29644188addad3bec"></a>

### `pin_retries_get`

```c
int(* fido2_storage_api::pin_retries_get) (uint8_t *retries)
```

获取剩余 PIN 重试次数。

<a id="a72eac7fc7756ca6dbc53fe67d2161a93"></a>

### `pin_retries_reset`

```c
int(* fido2_storage_api::pin_retries_reset) (void)
```

将 PIN 重试计数器重置为最大值。

<a id="ad5d135ae94fd0d4feef3c815b0cbe213"></a>

### `pin_set`

```c
int(* fido2_storage_api::pin_set) (const uint8_t pin_hash[16])
```

存储 PIN 哈希。

<a id="a516702caaa10b783fbdbe6f6bf42ed96"></a>

### `remove`

```c
int(* fido2_storage_api::remove) (const uint8_t *cred_id, size_t cred_id_len, struct fido2_credential *cred)
```

按 ID 删除凭据。

<a id="a7fdaf0829c6cacaba0e0e2966999c1fd"></a>

### `sign_count_increment`

```c
int(* fido2_storage_api::sign_count_increment) (const uint8_t *cred_id, size_t cred_id_len, uint32_t *new_count)
```

递增签名计数器并返回其值。

<a id="a6e73c6a26dc5601d8936ce977e9061b1"></a>

### `store`

```c
int(* fido2_storage_api::store) (const struct fido2_credential *cred)
```

存储一项凭据。

<a id="a1c48cffc28698583435cb5fc5944b0a2"></a>

### `update_user_info`

```c
int(* fido2_storage_api::update_user_info) (const uint8_t *cred_id, size_t cred_id_len, const char *user_name, const char *user_display_name)
```

更新已有凭据的用户信息。

<a id="a2aca20305a1b0919124231d5f62de79a"></a>

### `wipe_all`

```c
int(* fido2_storage_api::wipe_all) (void)
```

清除所有已存储凭据及 PIN 状态。

本数据类型文档由以下文件生成：

- `zephyr/authentication/fido2/fido2_storage.h`

## 9.3\_原页交叉引用（Cross References）

- [zephyr/authentication/fido2/fido2_storage.h](https://docs.zephyrproject.org/latest/doxygen/html/fido2__storage_8h_source.html)
- [fido2_credential](P007_fido2_credential_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [fido2_storage_iterate_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gad0f22c2a4c49fdd7b47ed0913115c5b2)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P008_fido2_device_info_结构体.md) · [返回大纲](大纲.md) · [下一章](P010_fido2_transport_结构体.md)

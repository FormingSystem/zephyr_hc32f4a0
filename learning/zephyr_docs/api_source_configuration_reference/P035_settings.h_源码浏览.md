---
id: learning.zephyr-docs.api-source-configuration-reference.page-35
title: settings.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2settings_2settings_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第35章\_settings.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2settings_2settings_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../storage/P076_设置子系统头文件.md)。

## 35.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00027"></a>
<a id="l00035"></a>
<a id="l00037"></a>
<a id="l00039"></a>
<a id="l00041"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="foldopen00076"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="foldopen00146"></a>
<a id="l00146"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="l00223"></a>
<a id="l00224"></a>
<a id="l00225"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="l00230"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="foldopen00248"></a>
<a id="l00248"></a>
<a id="l00249"></a>
<a id="l00250"></a>
<a id="l00260"></a>
<a id="l00261"></a>
<a id="l00271"></a>
<a id="l00272"></a>
<a id="l00281"></a>
<a id="l00282"></a>
<a id="l00290"></a>
<a id="l00291"></a>
<a id="l00300"></a>
<a id="l00301"></a>
<a id="l00311"></a>
<a id="l00312"></a>
<a id="l00319"></a>
<a id="l00320"></a>
<a id="l00336"></a>
<a id="l00337"></a>
<a id="l00338"></a>
<a id="l00356"></a>
<a id="l00357"></a>
<a id="l00364"></a>
<a id="l00365"></a>
<a id="l00374"></a>
<a id="l00375"></a>
<a id="l00387"></a>
<a id="l00388"></a>
<a id="l00399"></a>
<a id="l00400"></a>
<a id="l00407"></a>
<a id="l00408"></a>
<a id="l00417"></a>
<a id="l00418"></a>
<a id="l00433"></a>
<a id="l00434"></a>
<a id="l00435"></a>
<a id="l00439"></a>
<a id="l00445"></a>
<a id="l00446"></a>
<a id="l00447"></a>
<a id="l00448"></a>
<a id="l00449"></a>
<a id="l00450"></a>
<a id="l00451"></a>
<a id="foldopen00455"></a>
<a id="l00455"></a>
<a id="l00457"></a>
<a id="l00458"></a>
<a id="l00460"></a>
<a id="l00461"></a>
<a id="l00462"></a>
<a id="foldopen00467"></a>
<a id="l00467"></a>
<a id="l00473"></a>
<a id="l00479"></a>
<a id="l00485"></a>
<a id="l00486"></a>
<a id="l00487"></a>
<a id="foldopen00493"></a>
<a id="l00493"></a>
<a id="l00509"></a>
<a id="l00510"></a>
<a id="l00522"></a>
<a id="l00523"></a>
<a id="l00524"></a>
<a id="l00535"></a>
<a id="l00536"></a>
<a id="l00544"></a>
<a id="l00545"></a>
<a id="l00556"></a>
<a id="l00557"></a>
<a id="l00558"></a>
<a id="l00566"></a>
<a id="l00567"></a>
<a id="l00575"></a>
<a id="l00576"></a>
<a id="l00577"></a>
<a id="l00584"></a>
<a id="l00585"></a>
<a id="l00592"></a>
<a id="l00593"></a>
<a id="l00594"></a>
<a id="l00595"></a>
<a id="l00596"></a>
<a id="l00597"></a>
<a id="l00606"></a>
<a id="l00607"></a>
<a id="l00621"></a>
<a id="l00622"></a>
<a id="l00626"></a>
<a id="l00633"></a>
<a id="l00654"></a>
<a id="l00655"></a>
<a id="l00666"></a>
<a id="l00670"></a>
<a id="l00677"></a>
<a id="l00689"></a>
<a id="l00690"></a>
<a id="l00702"></a>
<a id="l00703"></a>
<a id="l00713"></a>
<a id="l00717"></a>
<a id="l00729"></a>
<a id="l00730"></a>
<a id="l00731"></a>
<a id="l00732"></a>
<a id="l00733"></a>
<a id="l00734"></a>
<a id="l00735"></a>
<a id="agroup__settings__backend_html_ga37bcada0be44b023cd3759e519e69d01"></a>
<a id="agroup__settings__backend_html_gab03a10ed0b65809369b4b6f220aa3df6"></a>
<a id="agroup__settings__backend_html_gad16bb70588cf69873f8872d7bf90e1c6"></a>
<a id="agroup__settings__backend_html_gaf94e311eba2b109cdbddd2767e502e77"></a>
<a id="agroup__settings__name__proc_html_ga6d9d36d54a1bfd59bf7729621653edd9"></a>
<a id="agroup__settings__name__proc_html_gacf259320845ae83c46df634f93c6d3e5"></a>
<a id="agroup__settings__rt_html_ga99a4714ba8c184afc659c43ec2020844"></a>
<a id="agroup__settings__rt_html_gae1b95c47c49774d53b4745af810e881e"></a>
<a id="agroup__settings__rt_html_gafa96974170dced7a131bfd5f022483f8"></a>
<a id="agroup__settings_html_ga070b6ad31bca0bee71ec1f1a4d67618d"></a>
<a id="agroup__settings_html_ga11523bc43121d78e0ac8ee1443559e42"></a>
<a id="agroup__settings_html_ga1dfe42f40a7d63bbdb81aed864d0ff12"></a>
<a id="agroup__settings_html_ga51cdac276c1fb8cd27fc3eec42749a04"></a>
<a id="agroup__settings_html_ga5d82a2e0a16585df406a45aa9beab4c6"></a>
<a id="agroup__settings_html_ga623c60b89dda3145f9334343748d5954"></a>
<a id="agroup__settings_html_ga6ada8f687dcd3f3374a766ca173fdf27"></a>
<a id="agroup__settings_html_ga767bf6c2709b1c58afcf4d1c5ef0d535"></a>
<a id="agroup__settings_html_ga789410aa059398d6c8a7851ea6945b55"></a>
<a id="agroup__settings_html_ga89c6d618df81f197cc5c1a2018b00648"></a>
<a id="agroup__settings_html_ga988b9cb22e256c87ac99d8007ff54a13"></a>
<a id="agroup__settings_html_gab2043a6d799202e177cc3dfa0cbfa531"></a>
<a id="agroup__settings_html_gab80e8a21c80243359b652386f7ce2424"></a>
<a id="agroup__settings_html_gacadb36d1cd5f6c7c6cbaf46e0e81ac7c"></a>
<a id="agroup__settings_html_gadf612631e30119ff688f83f16ad5aa89"></a>
<a id="agroup__settings_html_gaf22356f0dd01d4cf43a6297fafa86e30"></a>
<a id="agroup__settings_html_gaf81fad8575840f73a739d16d79613f8e"></a>
<a id="agroup__single-linked-list__apis_html_ga69bf43aad81e3ee2d55250c59b857493"></a>
<a id="ainclude_2zephyr_2settings_2settings_8h_html_a282c5c2c25ae5a375c51150a87869f14"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html_a5c5d83d87790efd59ea916c2b99f9118"></a>
<a id="aslist_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astructsettings__handler__static_html"></a>
<a id="astructsettings__handler__static_html_a093ab8346aedd0a9cb06dfaa4387f393"></a>
<a id="astructsettings__handler__static_html_a2cf94a6dad3ec35ca58b5ef869c7edae"></a>
<a id="astructsettings__handler__static_html_a612e973a6c91fbce7fb6ccc628638ed3"></a>
<a id="astructsettings__handler__static_html_aa8e57471bd89f4792cfb0689462b6f9b"></a>
<a id="astructsettings__handler__static_html_abb1df3f0f05fb2a57cd08e380bfffa09"></a>
<a id="astructsettings__handler__static_html_acc65e884503cf7db1276e7777f57fb12"></a>
<a id="astructsettings__handler_html"></a>
<a id="astructsettings__handler_html_a30207125407f57a0f117ecaee5a2054a"></a>
<a id="astructsettings__handler_html_a6aa2cc76c84341c3d29b679d2cc9c6ab"></a>
<a id="astructsettings__handler_html_a70aa25bf3b53898ab22906e9949963a4"></a>
<a id="astructsettings__handler_html_a8d4036babe22872777610e54c4dadf21"></a>
<a id="astructsettings__handler_html_ab8eee945dc866ec90b272fb526abc646"></a>
<a id="astructsettings__handler_html_ad2eae214e3ba8e50ead1a0e9afe2b251"></a>
<a id="astructsettings__handler_html_ad5e23a2acf29bbb2a5a4f249b5f80e0a"></a>
<a id="astructsettings__load__arg_html"></a>
<a id="astructsettings__load__arg_html_a0764239993147761b12e8999f860d267"></a>
<a id="astructsettings__load__arg_html_a7cbe713a1e0d2885528644b5a54f27d3"></a>
<a id="astructsettings__load__arg_html_aec32e51b4a6b61aff2ea415aa80a9987"></a>
<a id="astructsettings__store__itf_html"></a>
<a id="astructsettings__store__itf_html_a8c08da2cd010f5d73689e84d02d12734"></a>
<a id="astructsettings__store__itf_html_a90c2506cb06e5d80dffc6c08c6007bce"></a>
<a id="astructsettings__store__itf_html_ace444937a6c762d88c0143871cb71600"></a>
<a id="astructsettings__store__itf_html_ae3492100b922be0ef0f44022044ed151"></a>
<a id="astructsettings__store__itf_html_af6aae0b06cdc935975f19eb4c56eb991"></a>
<a id="astructsettings__store__itf_html_af97b8a3e2bdac663dd3872117251f0d2"></a>
<a id="astructsettings__store_html"></a>
<a id="astructsettings__store_html_a9f382f4e61737585228a6a3b86e9a38c"></a>
<a id="astructsettings__store_html_aaa0f629059f0c49b0f92f278791ce19c"></a>
<a id="asys_2iterable__sections_8h_html"></a>
<a id="asys_2util_8h_html"></a>

```c
/*
 * Copyright (c) 2018 Nordic Semiconductor ASA
 * Copyright (c) 2015 Runtime Inc
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_SETTINGS_SETTINGS_H_
#define ZEPHYR_INCLUDE_SETTINGS_SETTINGS_H_

#include <sys/types.h>
#include <zephyr/sys/util.h>
#include <zephyr/sys/slist.h>
#include <zephyr/sys/iterable_sections.h>
#include <stdint.h>

#ifdef __cplusplus
extern "C" {
#endif



#define SETTINGS_MAX_DIR_DEPTH  8
#define SETTINGS_MAX_NAME_LEN   (8 * SETTINGS_MAX_DIR_DEPTH)
#define SETTINGS_MAX_VAL_LEN    256
#define SETTINGS_NAME_SEPARATOR '/'
#define SETTINGS_NAME_END       '='

#define SETTINGS_EXTRA_LEN ((SETTINGS_MAX_DIR_DEPTH - 1) + 2)

#define SETTINGS_FULL_NAME_LEN ((SETTINGS_MAX_NAME_LEN) + (SETTINGS_EXTRA_LEN) + 1)

typedef ssize_t (*settings_read_cb)(void *cb_arg, void *data, size_t len);

struct settings_handler {

        const char *name;

        int cprio;

        int (*h_get)(const char *key, char *val, int val_len_max);

        int (*h_set)(const char *key, size_t len, settings_read_cb read_cb, void *cb_arg);

        int (*h_commit)(void);

        int (*h_export)(int (*export_func)(const char *name, const void *val, size_t val_len));

        sys_snode_t node;
};

struct settings_handler_static {
        const char *name;

        int cprio;

        int (*h_get)(const char *key, char *val, int val_len_max);

        int (*h_set)(const char *key, size_t len, settings_read_cb read_cb, void *cb_arg);

        int (*h_commit)(void);

        int (*h_export)(int (*export_func)(const char *name, const void *val, size_t val_len));
};


#define SETTINGS_STATIC_HANDLER_DEFINE_WITH_CPRIO(_hname, _tree, _get, _set, _commit, _export,     \
                                                  _cprio)                                          \
        const STRUCT_SECTION_ITERABLE(settings_handler_static, settings_handler_##_hname) = {      \
                .name = _tree,                                                                     \
                .cprio = _cprio,                                                                   \
                .h_get = _get,                                                                     \
                .h_set = _set,                                                                     \
                .h_commit = _commit,                                                               \
                .h_export = _export,                                                               \
        }

#define SETTINGS_STATIC_HANDLER_DEFINE(_hname, _tree, _get, _set, _commit, _export)                \
        SETTINGS_STATIC_HANDLER_DEFINE_WITH_CPRIO(_hname, _tree, _get, _set, _commit, _export, 0)

int settings_subsys_init(void);

int settings_register_with_cprio(struct settings_handler *cf, int cprio);

int settings_register(struct settings_handler *cf);

int settings_load(void);

int settings_load_subtree(const char *subtree);

ssize_t settings_load_one(const char *name, void *buf, size_t buf_len);

ssize_t settings_get_val_len(const char *key);

typedef int (*settings_load_direct_cb)(const char *key, size_t len, settings_read_cb read_cb,
                                       void *cb_arg, void *param);

int settings_load_subtree_direct(const char *subtree, settings_load_direct_cb cb, void *param);

int settings_save(void);

int settings_save_subtree(const char *subtree);

int settings_save_one(const char *name, const void *value, size_t val_len);

int settings_delete(const char *name);

int settings_commit(void);

int settings_commit_subtree(const char *subtree);

int settings_save_subtree_or_single_without_modification(const char *name, bool save_if_subtree,
                                                         bool save_if_single_setting);



/*
 * API for config storage
 */

struct settings_store_itf;

struct settings_store {
        sys_snode_t cs_next;

        const struct settings_store_itf *cs_itf;
};

struct settings_load_arg {
        const char *subtree;
        settings_load_direct_cb cb;
        void *param;
};

struct settings_store_itf {
        int (*csi_load)(struct settings_store *cs, const struct settings_load_arg *arg);

        ssize_t (*csi_load_one)(struct settings_store *cs, const char *name, char *buf,
                                size_t buf_len);

        ssize_t (*csi_get_val_len)(struct settings_store *cs, const char *name);

        int (*csi_save_start)(struct settings_store *cs);

        int (*csi_save)(struct settings_store *cs, const char *name, const char *value,
                        size_t val_len);

        int (*csi_save_end)(struct settings_store *cs);

        void *(*csi_storage_get)(struct settings_store *cs);
};

void settings_src_register(struct settings_store *cs);

void settings_dst_register(struct settings_store *cs);

/*
 * API for handler lookup
 */

struct settings_handler_static *settings_parse_and_lookup(const char *name, const char **next);

int settings_call_set_handler(const char *name, size_t len, settings_read_cb read_cb,
                              void *read_cb_arg, const struct settings_load_arg *load_arg);


int settings_name_steq(const char *name, const char *key, const char **next);

int settings_name_next(const char *name, const char **next);


int settings_runtime_set(const char *name, const void *data, size_t len);

int settings_runtime_get(const char *name, void *data, size_t len);

int settings_runtime_commit(const char *name);

int settings_storage_get(void **storage);

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_SETTINGS_SETTINGS_H_ */
```

## 35.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2018 Nordic Semiconductor ASA。

版权（Copyright）：© 2015 Runtime Inc。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 446 行

配置存储 API（API for config storage）。

### 注释 3：原第 594 行

处理程序查找 API（API for handler lookup）。

### 注释 4：原第 735 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_SETTINGS_SETTINGS_H_`。

## 35.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../storage/P076_设置子系统头文件.md)
- [sys/types.h](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html)
- [zephyr/sys/util.h](../util_reference/P002_通用工具头文件参考.md)
- [zephyr/sys/slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [ssize_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a5c5d83d87790efd59ea916c2b99f9118)
- [settings_read_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__settings.html#ga51cdac276c1fb8cd27fc3eec42749a04)
- [settings_handler](../storage/P066_设置动态处理器结构.md)
- [name](https://docs.zephyrproject.org/latest/doxygen/html/structsettings__handler.html#ab8eee945dc866ec90b272fb526abc646)
- [cprio](https://docs.zephyrproject.org/latest/doxygen/html/structsettings__handler.html#ad2eae214e3ba8e50ead1a0e9afe2b251)
- [h_get](https://docs.zephyrproject.org/latest/doxygen/html/structsettings__handler.html#a8d4036babe22872777610e54c4dadf21)
- [h_set](https://docs.zephyrproject.org/latest/doxygen/html/structsettings__handler.html#a70aa25bf3b53898ab22906e9949963a4)
- [h_commit](https://docs.zephyrproject.org/latest/doxygen/html/structsettings__handler.html#ad5e23a2acf29bbb2a5a4f249b5f80e0a)
- [h_export](https://docs.zephyrproject.org/latest/doxygen/html/structsettings__handler.html#a30207125407f57a0f117ecaee5a2054a)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [node](https://docs.zephyrproject.org/latest/doxygen/html/structsettings__handler.html#a6aa2cc76c84341c3d29b679d2cc9c6ab)
- [settings_handler_static](../storage/P067_设置静态处理器结构.md)
- [name](https://docs.zephyrproject.org/latest/doxygen/html/structsettings__handler__static.html#aa8e57471bd89f4792cfb0689462b6f9b)
- [cprio](https://docs.zephyrproject.org/latest/doxygen/html/structsettings__handler__static.html#a612e973a6c91fbce7fb6ccc628638ed3)
- [h_get](https://docs.zephyrproject.org/latest/doxygen/html/structsettings__handler__static.html#acc65e884503cf7db1276e7777f57fb12)
- [h_set](https://docs.zephyrproject.org/latest/doxygen/html/structsettings__handler__static.html#a2cf94a6dad3ec35ca58b5ef869c7edae)
- [h_commit](https://docs.zephyrproject.org/latest/doxygen/html/structsettings__handler__static.html#a093ab8346aedd0a9cb06dfaa4387f393)
- [h_export](https://docs.zephyrproject.org/latest/doxygen/html/structsettings__handler__static.html#abb1df3f0f05fb2a57cd08e380bfffa09)
- [settings_subsys_init](https://docs.zephyrproject.org/latest/doxygen/html/group__settings.html#gaf81fad8575840f73a739d16d79613f8e)
- [settings_register_with_cprio](https://docs.zephyrproject.org/latest/doxygen/html/group__settings.html#gadf612631e30119ff688f83f16ad5aa89)
- [settings_register](https://docs.zephyrproject.org/latest/doxygen/html/group__settings.html#gab2043a6d799202e177cc3dfa0cbfa531)
- [settings_load](https://docs.zephyrproject.org/latest/doxygen/html/group__settings.html#ga89c6d618df81f197cc5c1a2018b00648)
- [settings_load_subtree](https://docs.zephyrproject.org/latest/doxygen/html/group__settings.html#gab80e8a21c80243359b652386f7ce2424)
- [settings_load_one](https://docs.zephyrproject.org/latest/doxygen/html/group__settings.html#ga6ada8f687dcd3f3374a766ca173fdf27)
- [settings_get_val_len](https://docs.zephyrproject.org/latest/doxygen/html/group__settings.html#gacadb36d1cd5f6c7c6cbaf46e0e81ac7c)
- [settings_load_direct_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__settings.html#ga767bf6c2709b1c58afcf4d1c5ef0d535)
- [settings_load_subtree_direct](https://docs.zephyrproject.org/latest/doxygen/html/group__settings.html#ga1dfe42f40a7d63bbdb81aed864d0ff12)
- [settings_save](https://docs.zephyrproject.org/latest/doxygen/html/group__settings.html#ga789410aa059398d6c8a7851ea6945b55)
- [settings_save_subtree](https://docs.zephyrproject.org/latest/doxygen/html/group__settings.html#ga988b9cb22e256c87ac99d8007ff54a13)
- [settings_save_one](https://docs.zephyrproject.org/latest/doxygen/html/group__settings.html#gaf22356f0dd01d4cf43a6297fafa86e30)
- [settings_delete](https://docs.zephyrproject.org/latest/doxygen/html/group__settings.html#ga070b6ad31bca0bee71ec1f1a4d67618d)
- [settings_commit](https://docs.zephyrproject.org/latest/doxygen/html/group__settings.html#ga623c60b89dda3145f9334343748d5954)
- [settings_commit_subtree](https://docs.zephyrproject.org/latest/doxygen/html/group__settings.html#ga11523bc43121d78e0ac8ee1443559e42)
- [settings_save_subtree_or_single_without_modification](https://docs.zephyrproject.org/latest/doxygen/html/group__settings.html#ga5d82a2e0a16585df406a45aa9beab4c6)
- [settings_store_itf](../storage/P070_设置后端操作结构.md)
- [settings_store](../storage/P068_设置存储节点结构.md)
- [cs_next](https://docs.zephyrproject.org/latest/doxygen/html/structsettings__store.html#a9f382f4e61737585228a6a3b86e9a38c)
- [cs_itf](https://docs.zephyrproject.org/latest/doxygen/html/structsettings__store.html#aaa0f629059f0c49b0f92f278791ce19c)
- [settings_load_arg](../storage/P069_设置加载参数结构.md)
- [subtree](https://docs.zephyrproject.org/latest/doxygen/html/structsettings__load__arg.html#a0764239993147761b12e8999f860d267)
- [cb](https://docs.zephyrproject.org/latest/doxygen/html/structsettings__load__arg.html#aec32e51b4a6b61aff2ea415aa80a9987)
- [param](https://docs.zephyrproject.org/latest/doxygen/html/structsettings__load__arg.html#a7cbe713a1e0d2885528644b5a54f27d3)
- [csi_load](https://docs.zephyrproject.org/latest/doxygen/html/structsettings__store__itf.html#a8c08da2cd010f5d73689e84d02d12734)
- [csi_load_one](https://docs.zephyrproject.org/latest/doxygen/html/structsettings__store__itf.html#ae3492100b922be0ef0f44022044ed151)
- [csi_get_val_len](https://docs.zephyrproject.org/latest/doxygen/html/structsettings__store__itf.html#ace444937a6c762d88c0143871cb71600)
- [csi_save_start](https://docs.zephyrproject.org/latest/doxygen/html/structsettings__store__itf.html#af6aae0b06cdc935975f19eb4c56eb991)
- [csi_save](https://docs.zephyrproject.org/latest/doxygen/html/structsettings__store__itf.html#af97b8a3e2bdac663dd3872117251f0d2)
- [csi_save_end](https://docs.zephyrproject.org/latest/doxygen/html/structsettings__store__itf.html#a90c2506cb06e5d80dffc6c08c6007bce)
- [settings_src_register](https://docs.zephyrproject.org/latest/doxygen/html/group__settings__backend.html#gad16bb70588cf69873f8872d7bf90e1c6)
- [settings_dst_register](https://docs.zephyrproject.org/latest/doxygen/html/group__settings__backend.html#ga37bcada0be44b023cd3759e519e69d01)
- [settings_parse_and_lookup](https://docs.zephyrproject.org/latest/doxygen/html/group__settings__backend.html#gab03a10ed0b65809369b4b6f220aa3df6)
- [settings_call_set_handler](https://docs.zephyrproject.org/latest/doxygen/html/group__settings__backend.html#gaf94e311eba2b109cdbddd2767e502e77)
- [settings_name_steq](https://docs.zephyrproject.org/latest/doxygen/html/group__settings__name__proc.html#ga6d9d36d54a1bfd59bf7729621653edd9)
- [settings_name_next](https://docs.zephyrproject.org/latest/doxygen/html/group__settings__name__proc.html#gacf259320845ae83c46df634f93c6d3e5)
- [settings_runtime_set](https://docs.zephyrproject.org/latest/doxygen/html/group__settings__rt.html#gae1b95c47c49774d53b4745af810e881e)
- [settings_runtime_get](https://docs.zephyrproject.org/latest/doxygen/html/group__settings__rt.html#ga99a4714ba8c184afc659c43ec2020844)
- [settings_runtime_commit](https://docs.zephyrproject.org/latest/doxygen/html/group__settings__rt.html#gafa96974170dced7a131bfd5f022483f8)
- [settings_storage_get](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2settings_2settings_8h.html#a282c5c2c25ae5a375c51150a87869f14)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html)
- [slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [settings_handler_static::h_commit](https://docs.zephyrproject.org/latest/doxygen/html/structsettings__handler__static.html#a093ab8346aedd0a9cb06dfaa4387f393)
- [settings_handler_static::h_set](https://docs.zephyrproject.org/latest/doxygen/html/structsettings__handler__static.html#a2cf94a6dad3ec35ca58b5ef869c7edae)
- [settings_handler_static::cprio](https://docs.zephyrproject.org/latest/doxygen/html/structsettings__handler__static.html#a612e973a6c91fbce7fb6ccc628638ed3)
- [settings_handler_static::name](https://docs.zephyrproject.org/latest/doxygen/html/structsettings__handler__static.html#aa8e57471bd89f4792cfb0689462b6f9b)
- [settings_handler_static::h_export](https://docs.zephyrproject.org/latest/doxygen/html/structsettings__handler__static.html#abb1df3f0f05fb2a57cd08e380bfffa09)
- [settings_handler_static::h_get](https://docs.zephyrproject.org/latest/doxygen/html/structsettings__handler__static.html#acc65e884503cf7db1276e7777f57fb12)
- [settings_handler::h_export](https://docs.zephyrproject.org/latest/doxygen/html/structsettings__handler.html#a30207125407f57a0f117ecaee5a2054a)
- [settings_handler::node](https://docs.zephyrproject.org/latest/doxygen/html/structsettings__handler.html#a6aa2cc76c84341c3d29b679d2cc9c6ab)
- [settings_handler::h_set](https://docs.zephyrproject.org/latest/doxygen/html/structsettings__handler.html#a70aa25bf3b53898ab22906e9949963a4)
- [settings_handler::h_get](https://docs.zephyrproject.org/latest/doxygen/html/structsettings__handler.html#a8d4036babe22872777610e54c4dadf21)
- [settings_handler::name](https://docs.zephyrproject.org/latest/doxygen/html/structsettings__handler.html#ab8eee945dc866ec90b272fb526abc646)
- [settings_handler::cprio](https://docs.zephyrproject.org/latest/doxygen/html/structsettings__handler.html#ad2eae214e3ba8e50ead1a0e9afe2b251)
- [settings_handler::h_commit](https://docs.zephyrproject.org/latest/doxygen/html/structsettings__handler.html#ad5e23a2acf29bbb2a5a4f249b5f80e0a)
- [settings_load_arg::subtree](https://docs.zephyrproject.org/latest/doxygen/html/structsettings__load__arg.html#a0764239993147761b12e8999f860d267)
- [settings_load_arg::param](https://docs.zephyrproject.org/latest/doxygen/html/structsettings__load__arg.html#a7cbe713a1e0d2885528644b5a54f27d3)
- [settings_load_arg::cb](https://docs.zephyrproject.org/latest/doxygen/html/structsettings__load__arg.html#aec32e51b4a6b61aff2ea415aa80a9987)
- [settings_store_itf::csi_load](https://docs.zephyrproject.org/latest/doxygen/html/structsettings__store__itf.html#a8c08da2cd010f5d73689e84d02d12734)
- [settings_store_itf::csi_save_end](https://docs.zephyrproject.org/latest/doxygen/html/structsettings__store__itf.html#a90c2506cb06e5d80dffc6c08c6007bce)
- [settings_store_itf::csi_get_val_len](https://docs.zephyrproject.org/latest/doxygen/html/structsettings__store__itf.html#ace444937a6c762d88c0143871cb71600)
- [settings_store_itf::csi_load_one](https://docs.zephyrproject.org/latest/doxygen/html/structsettings__store__itf.html#ae3492100b922be0ef0f44022044ed151)
- [settings_store_itf::csi_save_start](https://docs.zephyrproject.org/latest/doxygen/html/structsettings__store__itf.html#af6aae0b06cdc935975f19eb4c56eb991)
- [settings_store_itf::csi_save](https://docs.zephyrproject.org/latest/doxygen/html/structsettings__store__itf.html#af97b8a3e2bdac663dd3872117251f0d2)
- [settings_store::cs_next](https://docs.zephyrproject.org/latest/doxygen/html/structsettings__store.html#a9f382f4e61737585228a6a3b86e9a38c)
- [settings_store::cs_itf](https://docs.zephyrproject.org/latest/doxygen/html/structsettings__store.html#aaa0f629059f0c49b0f92f278791ce19c)
- [iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)
- [util.h](../util_reference/P002_通用工具头文件参考.md)

---

[上一章](P034_imx_ccm.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P036_infineon-xmc4xxx-gpio.h_源码浏览.md)

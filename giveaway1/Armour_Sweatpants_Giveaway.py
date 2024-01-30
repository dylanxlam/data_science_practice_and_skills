import random
def extract_entries(tags, story_reshares):
    """
    Extract tags from the provided text.

    Args:
    - text (str): The text containing mentions.

    Returns:
    - list: A list of strings representing mentions.
    """
    # Split the text into lines and extract mentions
    mentions = []
    for line in tags.split('\n'):
        mention = line.split('@')[0].strip()
        # Check if the mention is not empty and does not contain only whitespace characters
        if mention and not all(char.isspace() or not char.isprintable() for char in mention) and '￼' not in mention:
            mentions.append(mention)
        # Add additional mentions
    mentions.extend(story_reshares * 10)
    return mentions


if __name__ == "__main__":
    # Example text containing mentions
    tags = """
    
    pbs.jayden  @devinnn.t1 


    _alavirg_@chasesmyth1 


    justinguy941@s0hyeongee
        


    meganhasani@ariana_zhuri1 


    jennitrann@meganhasani1 


    bwong.20@aritway1 


    issa_emta@gqtpn1 


    gavinbingen@abram.griffiths1 


    darrenndc@abby.villaa1 


    jomai__@youhaterich1 


    balabcoagaga@lujimori1 


    d9l@do9lifeless1 


    d9l@1anfoster i want dese1 


    tohtorou@mia.aarissa1 


    luvv4ishan@floormattttttt1 


    ariel.quack@purebredasian
        


    wh0s_j1mmy@alvarezsam_1 


    charmaraze@jugitooh1 


    andrew_liscio@j3ssfxb
        


    dwade_wayne3@tristanspamusubi1 


    zak.paraiso@rylerhuerto1 


    nuyorkluv@im.not._.eli1 


    c.lwolfe@th3onlyquin
        


    nuyorkluv@eli._.bored1 


    kuyasian@itzz.j91 


    1der9cMore
        


    kenneth.chen_Lemme cop
        


    chet2049_@norweigan_academy1 
        


    think_ink1@tsharahasina @moonstress__1 


    kuyasian@kassidy.vn1 


    c.lwolfe@whyits.privates
        




    wonginthong@brigitmorenoo1 


    4nderseepy@ccrystalwei1 


    4nderseepy@shiloh.vert1 


    kuyasian@trist9ns1 


    luvv4ishan@dallasmavs
        


    pbs.jayden@gublergram1 


    4nderseepy@mylesnoble_1 


    4nderseepy@anishwentwest1 


    4nderseepy@aaron.ekey1 


    4nderseepy@rcurtismen1 


    4nderseepy@mollywojj1 


    4nderseepy@alainareyess1 


    4nderseepy@madieson.d1 


    4nderseepy@mylesnoble_1 


    4nderseepy@malcolmmoore20291 


    4nderseepy@keiranhorbatuck1 


    4nderseepy@sha.an_091 


    4nderseepy@king_donovan121 


    4nderseepy@14udrey1 


    4nderseepy@jaybhimani491 


    4nderseepy@anonymousclinton1 


    4nderseepy@flat_earth_californian_31 


    4nderseepynah my turn lil bro
        


    kuyasian@gia._.riel1 


    siazphobic@hurtfultuna0241 


    kuyasian@marcsuniverse
        


    4nderseepy@kaiweipks1 


    4nderseepy@dangelovray
        


    wonginthong@joshf3rrer
        


    4nderseepy@kimchi.nick1 
        


    free.eyezack@ant.onthego @fjkrey @lilly_lilly07 @niahh.ml @isaaksluckii @guameire1 


    isshiikawa@kenziiyan


    dez_zuehlkeneed


    michaeltrnh@heber_.888


    los3r.robbie


    los3r.robbie@resolxv


    michaeltrnh@nathalie.q7 shh



    michaeltrnh@jam33sss___ 

    michaeltrnh@azuelaa._ mb


    michaeltrnh@joserwalesalt


    michaeltrnh@pappa_z12


    michaeltrnh@delilah.madrigall shhh


    michaeltrnh@love.on.b shhh


    michaeltrnh@overcookedp1g


    michaeltrnh@vianakim__ shhh


    michaeltrnh@mateo._.vl


    michaeltrnh@viet.jett


    michaeltrnh@jvvliie


    michaeltrnh@k.h.a.h.m


    michaeltrnh@k33lynn


    michaeltrnh@onlyodalis


    michaeltrnh@ami3_i


    michaeltrnh@4nhviet


    michaeltrnh@aljjorie


    michaeltrnh@alj0rie


    mandyyweng@utexaskpl


    mandyyweng@trinale__


    mandyyweng@denisekimm


    mandyyweng@jaynedaeun


    mandyyweng@c.ecevu


    mandyyweng@sophiidxng


    mandyyweng@vivnguyn


    mandyyweng@daovvivian


    mandyyweng@ashlynnhuynh


    mandyyweng@ytn._youssef


    mandyyweng@laurennllucas


    mandyyweng@kaitbernal


    mandyyweng@thuandoann
    ￼mandyyweng@jacobelordi
    ￼mandyyweng@austiinha
    ￼mandyyweng@ryansongvilay
    ￼mandyyweng@lsxac
    ￼mandyyweng@priscillaanguyenn
    ￼mandyyweng@kateeluo
    ￼mandyyweng@joooonkang
    ￼mandyyweng@jaclynguyenn
    ￼mandyyweng@jakobeha
    ￼mandyyweng@jesario
    ￼
    austiinha@tk.thomass
    ￼
    austiinha@lsxac
    ￼
    austiinha@phan.cindy
    ￼
    austiinha@mandyyweng
    ￼
    austiinha@joooonkang n
    ￼
    austiinha@dillanhong
    ￼
    austiinha@jakobeha
    ￼
    austiinha@ryansongvilay
    ￼
    austiinha@kiloplates
    ￼
    austiinha@lilyychau
    ￼
    austiinha@joshrasberry
    ￼
    austiinha@tyler.trann
    ￼
    austiinha@_jolenet
    ￼
    austiinha@ben.prakhin
    ￼
    austiinha@kevvin.kim
    ￼
    austiinha@kiloplates
    ￼
    austiinha@nathan_hahaha
    ￼
    tincala05@sg64831
    ￼
    worldbandits28@worldbandits28
    ￼
    matt_chuuuuuuu@bigb00ty_john
    ￼
    matt_chuuuuuuu@fatherbartholomew
    ￼
    matt_chuuuuuuu@alxxhuynh
    ￼
    matt_chuuuuuuu@d.iegoa
    ￼dan__bay@youbetterfuckingrun
    ￼dan__bay@artificialenvironments
    ￼dan__bay@verynichemarket
    ￼
    jade.tru@fatherbartholomew
    ￼
    jade.tru@alxxhuynh
    ￼
    jade.tru@bigb00ty_john
    ￼
    fatherbartholomew@tahah.21
    ￼
    fatherbartholomew@matt_chuuuuuuu
    ￼
    fatherbartholomew@danielyeepez
    ￼
    fatherbartholomew@alxxhuynh
    ￼
    fatherbartholomew@bigb00ty_john
    ￼
    bigb00ty_john@alxxhuynh
    ￼
    bigb00ty_john@matt_chuuuuuuu
    ￼
    bigb00ty_john@jade.tru
    ￼
    bigb00ty_john@fatherbartholomew
    ￼4nderseepy@bbtandkeshi
        
    ￼4nderseepy@dat.kid_niles
    ￼4nderseepy@ballwmustafa
    ￼4nderseepy@user_12349275
    ￼4nderseepy@555.ikus
    ￼4nderseepy@bradyhosaka
    ￼4nderseepy@vienn_aaa17
    ￼4nderseepy@diana.lutska
    ￼4nderseepy@sanakhn.t
    ￼
    kaylaanthony_@kayshopkinslover
    ￼
    kaylaanthony_@notmebutme2007
    ￼
    awesome8842019
    ￼
    awesome8842019@rowleykara
    ￼
    leoo_fel004@godsfandom3
    ￼
    ruishuzhang@kellyfangg
    ￼
    lucas_d_789@love_deln
    ￼
    wyadenni@ruishuzhang
    ￼

    ￼
    siazphobic@sammie.m_10
    ￼
    worldbandits28Need bruh
    ￼
    kairukugreb@derekcacao
    ￼
    carmenreece@love_me_foever 
    ￼lateforwork__@_ohhha
    ￼
    tuneski__@my.less5
    ￼
    freespectrum@cameron.lee.g
    ￼
    freespectrum@jackson.reid9
    ￼
    aniruddh25@ryanchu03
    ￼
    aniruddh25@jia.xuanz
    ￼
    intergains@undesireble
    ￼
    intergains@lntensively
    ￼
    based.lulu@meowshellers
    ￼
    based.lulu@dachuanggg
    ￼
    based.lulu@radrob
    ￼
    based.lulu@steven._shin
    ￼
    based.lulu@chicken.nuggets.no.burgers
    ￼
    based.lulu@hongryhongrykev
    ￼
    based.lulu@michelanjuno
    ￼
    thehighherald@woodever10
    ￼
    thehighherald@greengoddess430
    ￼
    thehighherald@reeferreporter
    ￼
    thehighherald@omgpackage
    ￼
    thehighherald@ohanimeattack
    ￼
    thehighherald@psilymyc
    ￼
    thehighherald@bigheartrising_
    ￼
    just.joonas@jonashatnenwitzgemacht
    ￼
    just.joonas@bastiresch2007
    ￼
    just.joonas@jonaswolfsteiner
    ￼
    jonashatnenwitzgemacht@just.joonas
    ￼
    jonashatnenwitzgemacht@bastiresch2007
    ￼
    jonashatnenwitzgemacht@jonaswolfsteiner
    ￼
    sherazerino@austiinha
    ￼
    sherazerino@mandyyweng
    ￼
    sherazerino@kentmorii
    ￼
    sherazerino@hwhyzee
    ￼
    rafmarco@fyeekicks
    ￼
    zatlonn@lenaaa.dolores
    ￼
    soydanielit0@amcastelann
    ￼pbs.jayden@baileyhava
    ￼pbs.jayden@pbs.fabiwaviii
    ￼pbs.jayden@pbs.tony
    ￼pbs.jayden@fboyarde
    ￼pbs.jayden@jordydivas
    ￼pbs.jayden@sxtiera
    ￼pbs.jayden@sofeacouch
    ￼pbs.jayden@adrianrxno
    ￼pbs.jayden@g.cecilia13
    ￼pbs.jayden@zachary_breed
    ￼pbs.jayden@aj_iopez
    ￼pbs.jayden@pbs.kiel
    ￼pbs.jayden@nik_larsonn
    ￼pbs.jayden@jjayzeea
    ￼pbs.jayden@beccahx2
    ￼pbs.jayden@david.ckra
    ￼
    fboyarde@artsybails
    ￼
    fboyarde@rensapplejuicestand
    ￼
    fboyarde@sofeacouch
    ￼
    fboyarde@adrianrxno
    ￼
    fboyarde@quietpapi
    ￼pbs.jayden@yuki_ishikawa_official
    ￼pbs.jayden@nishidayuji0130
    ￼pbs.jayden@clixsthegoat
    ￼pbs.jayden@asianjeff._
    ￼pbs.jayden@sinatraa_ow
    ￼pbs.jayden@dominicfike.df
    ￼pbs.jayden@catherinepaiz
    ￼pbs.jayden@deacon.perryman
    ￼pbs.jayden@t3ntc0re
    ￼pbs.jayden@flwushot
    ￼pbs.jayden@joss.hh
    ￼pbs.jayden@em_belanger
    ￼
    baileyhava@pbs.jayden
    ￼
    baileyhava@fboyarde
    ￼
    baileyhava@artsybails
    ￼
    wonginthong@maleah.777
    ￼
    wonginthong@lylynnatran
    ￼
    wonginthong@denize.zol
    ￼ethan_huynh@bleeblooblaaa
    ￼ethan_huynh@colin_trinh
    ￼ethan_huynh@chatcha.m
    ￼ethan_huynh@matchatcha_
    ￼__benhanma__@shareef.11
    ￼__benhanma__@shareef.photography1
    ￼__benhanma__@jxanellx
    ￼__benhanma__@kevinmomoney98
    ￼__benhanma__@moya_kevinn
    ￼__benhanma__@8jeanelle
    ￼__benhanma__@thisisjeanelle
    ￼__benhanma__@krystal0827_
    ￼__benhanma__@jonelversus
    ￼__benhanma__@lalopradine
    ￼__benhanma__@martinvayas
    ￼__benhanma__@yodaryy
    ￼__benhanma__@yodaforthapeople
    ￼__benhanma__@troncoco1220
    ￼__benhanma__@bebecito_brrr
    ￼__benhanma__@thismfdamian
    ￼__benhanma__@raymond__batista
    ￼__benhanma__@martinvayas
    ￼__benhanma__@cami.nanay
    ￼__benhanma__@big_o.meme.spams
    ￼__benhanma__@bigasianenergy.04
    ￼__benhanma__@jay.vibinnn
    ￼__benhanma__@sebav2006
    ￼__benhanma__@_._.travi
    ￼__benhanma__@bryan.do.things
    ￼__benhanma__@sheluvsseba
    ￼__benhanma__@oswizzybeats
    ￼__benhanma__@hochigon4
    ￼__benhanma__@andr3sinho_
    ￼__benhanma__@michael.valenciaa
    ￼__benhanma__@panwithmayo
    ￼__benhanma__@hiddenfiles
    ￼
    albert_lu_@kenneth.chen_
    ￼
    albert_lu_@hwhyzee
    ￼__benhanma__@kailee_e_s
    ￼
    shugoku_go@lexyygarcia
    ￼
    shugoku_go@shobrigg.s
    ￼
    shugoku_go@kamotbo
    ￼alexxromerro@amanda_dinh
    ￼alexxromerro@kwame.morrison
    ￼alexxromerro@kwame.morrison
    ￼alexxromerro@kwame.morrison
    ￼alexxromerro@hry_2003
    ￼alexxromerro@tomas.changg
    ￼alexxromerro@danchen_01
    ￼alexxromerro@realeddiecao
    ￼alexxromerro@ez6as
    ￼alexxromerro@dylan.epham
    ￼alexxromerro@unu.noh
    ￼alexxromerro@andy.lxm
    ￼alexxromerro@jrm_81
    ￼alexxromerro@the_ze_chen
    ￼alexxromerro@ericdnguyenn
    ￼alexxromerro@arn_pnrd
    ￼alexxromerro@austiinha
    ￼alexxromerro@scvttva
    ￼alexxromerro@luhbriqq
    ￼alexxromerro@daviid.morris
    ￼alexxromerro@jc.444
    ￼alexxromerro@texasomegas
    ￼alexxromerro@alextu27
    ￼alexxromerro@aido.bih
    ￼alexxromerro@ethann_shaw
    ￼alexxromerro@connora1221
    ￼alexxromerro@kevin_zhou__
    ￼
    aido.bih@derjckv
    ￼
    aido.bih@nvthon
    ￼
    aido.bih@alexxromerro
    ￼alexxromerro@aanthonyle
    ￼alexxromerro@dejenirate
    ￼
    connora1221@brandon129578643

    ￼__benhanma__@krisisnotfunny
    ￼__benhanma__@nayanasookdeo
    ￼nuyorkluv@fvrangel
    ￼nuyorkluv@unableari
    ￼nuyorkluv@cristit1re
    ￼nuyorkluv@poalaloo
    ￼nuyorkluv@ungamer22
    ￼nuyorkluv@its_alex_.888
    ￼nuyorkluv@nyjul__1905
    ￼nuyorkluv@_tima.li
    ￼__benhanma__@incognito.zip
    ￼realeddiecao@billyhuuu
    ￼brennanfromalawai@ezruh
    ￼brennanfromalawai@pohakuboys
    ￼brennanfromalawai@acesiahh
    ￼brennanfromalawai@tuan___pham
    ￼
    siazphobic@rubyscrims__
    ￼
    siazphobic@chris.k.c.s
    ￼
    siazphobic@fw.danilo17
    ￼
    hanwakeyy@becky.alw
    ￼
    hanwakeyy@oleg.jen
    ￼
    maoma522@imissmonkee nice ass sweat oants
    ￼romasantaethan@holliday_brendon
    ￼romasantaethan@romasantajulie
    ￼romasantaethan@jr.maybe.3
    ￼
    luigiqw08@cameron05simmons
    ￼
    siazphobic@siazp2
    ￼
    siazphobic@big_sad_johnson_69
    ￼
    siazphobic@sai_yuhh
    ￼kenescoto@sydney.cordero

    ￼indio_zhensi@divinedealer_
    ￼indio_zhensi@nas_1llm9tic
    ￼indio_zhensi@gyalrie
    ￼alexxromerro@dvlanl
    ￼
    undesireble@lntensively
    ￼
    undesireble@intergains
    ￼
    undesireble@moimran2668
    ￼
    lntensively@manitsharm05
    ￼politehex@m1ddleschoolbully
    ￼politehex@g0thkardashian 
    ￼mycuhll@dpr.n0va
    ￼
    sunnelkim@andrewoog
    ￼
    sunnelkim@andrewjung553
    ￼
    sunnelkim@lol_ani_
    ￼
    sunnelkim@doobookoo
    ￼
    sunnelkim@boohoo_koo
    ￼
    sunnelkim@k.sunyul
    ￼
    sunnelkim@poohjaniparty
    ￼
    sunnelkim@erinlee_0410
    ￼
    jepujwl@jeffjwl
    ￼
    geraldinemanio@josh_labrador
    ￼
    geraldinemaniostraight heat
    ￼
    geraldinemanio@jsesel
    ￼
    geraldinemanio@a_.anaaa
    ￼
    geraldinemanio@chlxstar
    ￼
    geraldinemanio@e.dgar_20
    ￼romasantaethan@hayleyta2136
    ￼romasantaethan@notabaddie.thx
    ￼
    joobearrr@icarliedv
    ￼
    joobearrr@cartierrrmoee
    ￼
    joobearrr@xxking_sosaxx
    ￼
    joobearrr@_trxppy._.kixd_
    ￼
    joobearrr@atx.gregory1
    ￼
    joobearrr@luhh_darkii
    ￼
    joobearrr@jaclyn’s_old_acc
    ￼
    joobearrr@annabel_urrabazo
    ￼
    joobearrr@thuggahh.leneee
    ￼
    joobearrr@_trippi3.kvng_
    ￼
    joobearrr@houston_._texas
    ￼
    joobearrr@kvng.townsend
    ￼
    joobearrr@ratchet__sarah_
    ￼
    joobearrr@nana.kai.spams
    ￼
    joobearrr@lamekidddreina
    ￼
    joobearrr@maddieperez9910
    ￼romasantaethan@yna_cao
    ￼
    carmelloow@exclusivelydez @yagfwantsm3 @xodezzaarrae
    ￼romasantaethan@tolbeezyy
    ￼romasantaethan@tolberdaaron
    ￼romasantaethan@joowiereads
    ￼
    eighteenwinter@erinkwun
    ￼
    eighteenwinter@kacie.tong
    ￼
    ￼
    andrew_liscio@lk12485
    ￼
    andrew_liscio@somm_nites
    ￼
    andrew_liscio@havok_toxic
    ￼
    sunnelkim@3ileen.png
    ￼
    sunnelkim@basic_catholic_boi
    ￼
    sunnelkim@_raeannel_
    ￼
    sunnelkim@solomon_is_sleepy
    ￼
    sunnelkim@eugenius_kimsta
    ￼romasantaethan@bdiddy_spams
    ￼
    d9l@oip.eee
    ￼
    d9l@2067xenon
    ￼
    connora1221@_bonifer
    ￼
    connora1221@arn_pnrd
    ￼
    connora1221@kennynguyxn
    ￼
    connora1221@brandon129578643
    ￼
    arn_pnrd@kennynguyxn
    ￼
    raynate07@_horaciio
    ￼
    raynate07@danmahdrid
    ￼
    raynate07@nathan_vieyra
    ￼
    raynate07@ilov3.nik
    ￼
    frank_fiend@juan_rod5
    ￼
    frank_fiend@ev_wrk
    ￼
    frank_fiend@toycarrt
    ￼sk84uu@yvesmei
    ￼
    frank_fiend@zekedestroyerofrealms
    ￼
    maakhiii@diorjohnsonfanaccount318
    ￼aboutzoelee
    ￼
    jc7llueng@jaaashhh
    ￼
    zak.paraiso@sandwwaaa
    ￼
    tysonline2003@donovan.martel
    ￼
    beelocsin@maxkanter_

    ￼
    mrtnkhuu@klou1s
    ￼
    mrtnkhuu@kkhoi__nnguyen
    ￼
    mrtnkhuu@phquch
    ￼
    mrtnkhuu@johnson_1546
    ￼
    mrtnkhuu@frnk_luong
    ￼
    mrtnkhuu@lukas.obrr
    ￼
    mrtnkhuu@thanhii7
    ￼
    mrtnkhuu@tinooo_1109
    ￼
    mrtnkhuu@captainasscan
    ￼
    mrtnkhuu@azes_403
    ￼4nderseepy@a.v.zz
    ￼4nderseepy@cc.camarillo6
    ￼4nderseepy@vib3with.sophia
    ￼
    tylqo@tylernqo
    ￼
    lilwesvert@easymoneycobbs
    ￼
    ethangranat@jamelafoutch
    ￼
    ethangranat@ailishhhhhh
    ￼
    ethangranat@mvuriciomendozv
    ￼
    ethangranat@ppprxncess
    ￼
    ethangranat@_linaward
    ￼
    storm_rider81@konstantia_mi
    ￼
    storm_rider81@mikekotsos
    ￼
    storm_rider81@iwannito
    ￼
    storm_rider81@nightchriss_89
    ￼
    storm_rider81@panos_tsartsalis
    ￼
    lieutenantt_dannn@yuriwithluv2
    ￼
    fuckwadee@johnwickofminecraft
    ￼
    fuckwadee@therealkingmenace
    ￼

    ￼
    fuckwadee@sweepers00


    ￼itssoliaa@patricia.tanola1
    ￼itssoliaa@melissaaates1
    ￼itssoliaa@sabho81
    ￼sakura_pangelinan@jaacobsantiago1
    ￼sakura_pangelinan@jissele.g1
    ￼sakura_pangelinan@kiryana_fulgencio1
    ￼sakura_pangelinan@derp_turttle1
    ￼sakura_pangelinan@kaaeellaa_1
    ￼sabho8@patricia.tanola1
    ￼sabho8@melissaaates1
    ￼
    jory_mitchell@laurisasimkins1
    ￼towobou@tekehuotu ♡
    ￼towobou@dylantinito
    ￼towobou@honeyjayyx
    ￼
    tincala05@sg64831
    ￼charmaraze@jonlonganiza
    ￼charmaraze@chefxnoah
    ￼
    joobearrr@ cms.sqxad
    ￼
    joobearrr@queen_kelci11
    ￼
    joobearrr@drippy_kxd23
    ￼
    joobearrr@aye_itz_jenar0
    ￼
    joobearrr@_.issa.lamekidd
    ￼
    joobearrr@dope_delacruz
    ￼
    joobearrr@_ppeteee
    ￼
    joobearrr@craccheadethan
    ￼
    joobearrr@asssopointed
    ￼
    joobearrr@its_beth08
    ￼
    joobearrr@yuhlulbabyvonna
    ￼
    joobearrr@_.littkidjjarin
    ￼
    joobearrr@ugly.kidd.chris
    ￼
    joobearrr@king_rob_lustic
    ￼
    joobearrr@_xlaixnaax_
    ￼
    joobearrr@stokes23
    ￼
    joobearrr@ninagoofyaccount
    ￼
    joobearrr@gonzales_jermey
    ￼
    joobearrr@gonzales_jermey
    ￼danielklamb@nathanp.png
    ￼
    mrbokchoyboy@marcel.boomer
    ￼
    materialspiritualspace@javincchan
    ￼
    tyler_hudgins7689@uhhlisah
    ￼
    linchjosh@linchj243m
    ￼
    kiya_kiya99@its_kiya_jalon
    ￼stjameel@ihavefemaletraits
    ￼
    kiya_kiya99@mickey_tk_
    ￼stjameel@breespack
    ￼grahamfindell@speed_limit_5
    ￼toekneema@ethanadlee
    ￼
    brndnsng@_alavirg_
    ￼
    oreodasillygoose@bobisspam
    ￼
    oreodasillygoose@kosherseasalt
    ￼
    oreodasillygoose@lilosiii
    ￼mrcattmatt@ejejdisjtitoqna
    ￼
    writtenbyewz@aidan_hwang
    ￼
    writtenbyewz@aiden.mceachern
    ￼
    writtenbyewz@ethanerawan
    ￼
    wonginthong@zzachcho
    ￼
    wonginthong@khiiemtrnn
    ￼
    wonginthong@ilenecastaneda
    ￼
    wonginthong@yutokitag
    ￼
    wonginthong@erinkwun
    ￼
    grant.shirata@p4trina
    ￼
    isaque.ldn@neclaruz
    ￼
    isaque.ldn@muriloovee
    ￼
    isaque.ldn@gabezik123
    ￼
    isaque.ldn@nicolaslorenzonii
    ￼
    jckthsnck@cscottt_
    ￼
    jckthsnck@samhoh04
    ￼
    jckthsnck@carmencware
    ￼
    samhoh04@jckthsnck
    ￼
    samhoh04@cscottt_
    ￼
    cscottt_@samhoh04
    ￼
    cscottt_@jckthsnck
    ￼
    cscottt_@carmencware
    ￼
    cscottt_@colinfranco_
    ￼
    cscottt_@elleryhorne
    ￼
    cscottt_@colin_franco92
    ￼
    jckthsnck@paul.defenbaugh
    ￼__benhanma__@ummm.melanie
    ￼
    lil_clown_man@moon._bug
    ￼
    1der9c@wheres._.sophiaaa

    ￼
    tj.99_@_darrenhuang_
    ￼
    tj.99_@dragonchilung
    ￼
    1der9c@its._al3xx
    ￼
    tj.99_@thien.thedoan
    ￼
    1der9c@probably._.nate
    ￼
    1der9c@evre.xrx
    ￼
    tj.99_@brianbhoang
    ￼
    1der9c@luvv4ishan
    ￼
    tj.99_@dc_el
    ￼
    1der9c@lilpinkblob5
    ￼
    1der9c@owxn.gm
    ￼
    tj.99_@jeremytaj_
    ￼
    1der9c@kamilaaquiroz_
    ￼
    1der9c@4nderseepy
    ￼
    tj.99_@draingang_alex
    ￼
    1der9c@masonnn.h.7
    ￼
    tj.99_@victor.y.ang
    ￼
    tj.99_@v12v0
    ￼
    1der9c@cameronqdo
    ￼
    tj.99_@tinnha_
    ￼
    1der9c@travis__han
    ￼
    1der9c@408dominic_
    ￼
    1der9c@huhjavi
    ￼4nderseepy@spammm4phia
    ￼
    1der9c@jawnn._loo
    ￼4nderseepy@ian.loooooooooong
    ￼
    1der9c@jacobfigueroa._
    ￼4nderseepy@theyluvmalcolm_
    ￼4nderseepy@sunny.dee7
    ￼
    1der9c@jay.nayal
    ￼4nderseepy@nathan._.gg
    ￼4nderseepy@diana.lutska
    ￼4nderseepy@travis__han
    ￼

    ￼4nderseepy@faaris.iq
    ￼4nderseepy@ghostkilika
    ￼
    1der9c@kai_1yn
    ￼
    1der9c@probably._.nate
    ￼
    1der9c@flippinlucas1
    ￼
    1der9c@dallasspam567
    ￼
    1der9c@dallasc.c
    ￼
    1der9c@vjujuboards
    ￼
    1der9c@emmanuel.floresss
    ￼
    kuyasian@dwade_wayne3
    ￼
    kuyasian@valrimz
    ￼
    kuyasian@abelstoesreek
    ￼
    kuyasian@ethanvpam
    ￼
    kuyasian@br1qnz
    ￼
    kuyasian@povvmiu
    ￼b_dianati@sai.m.iar
    ￼
    atomicinertia@pooptosis
    ￼
    tthienman@kwvintrwn
    ￼
    brownmanray@brooke.alexa113
    ￼
    brownmanray@mustafuh
    ￼
    brownmanray@mucrocs
    ￼
    brownmanray@uluvapollo
    ￼
    brownmanray@zayynob
    ￼
    brownmanray@adrian.gct
    ￼
    brownmanray@davinfamous
    ￼
    brownmanray@adrianspump
    ￼miconotnico@_alvarezvilma
    ￼
    leoarmdz@evelynsuzettem
    ￼
    brownmanray@jaysonplaceres
    ￼4nderseepy@phillip.lu
    ￼4nderseepy@sasha_keila_dumps
    ￼4nderseepy@notreallydante_
    ￼4nderseepy@phillip_sucks_at_life
    ￼4nderseepy@erumohr.408
    ￼4nderseepy@chefclaira
    ￼4nderseepy@nikhil_gum
    ￼4nderseepy@other_darryn
    ￼4nderseepy@kiwrxn
    ￼4nderseepy@_jsdiego
    ￼4nderseepy@darryn.p_
    ￼4nderseepy@kian.b27
    ￼4nderseepy@444.lukasnunes
    ￼4nderseepy@kreme_lifts
    ￼4nderseepy@ian_jjjjjjjjjjj
    ￼4nderseepy@scooter_weaver
    ￼4nderseepy@4rkadd
    ￼4nderseepy@sidkodangal34
    ￼4nderseepy@jussromeoo
    ￼4nderseepy@vtiwari28
    ￼4nderseepy@minionlover281
    ￼4nderseepy@_nel._.__
    ￼4nderseepy@prayag.nambiar
    ￼4nderseepy@phoenixn03
    ￼4nderseepy@alt_account838282
    ￼4nderseepy@rayaanjam
    ￼4nderseepy@omthechromosome
    ￼4nderseepy@jake_pianist
    ￼4nderseepy@4isabelle1600
    ￼4nderseepy@ohkkian
    ￼stjameel@amadu74s
    ￼edward.kim@faithbang
    ￼bronson_alonzo@ryanclarklover911
    ￼4nderseepy@earth2jacob_
    ￼4nderseepy@jacksonksu
    ￼4nderseepy@anish_.shankar
    ￼4nderseepy@hhilary.ho
    ￼
    thomasrobles_@mia.lanning
    ￼
    thomasrobles_@styafynie
    ￼
    gl_kickz18@sorayadrage
    ￼
    gl_kickz18@soraya.drage
    ￼
    gl_kickz18@sorayaa.papayaa
    ￼
    gl_kickz18@dumb.n.dumber2.0
    ￼
    k.steezy_1@g9nie
    ￼
    k.steezy_1@__sloppytoppy__
    ￼
    jatr4n@not._.kevvv
    ￼4nderseepy@ncortez472
    ￼4nderseepy@sidkodangal34
    ￼4nderseepy@evanspamfriedrice
    ￼4nderseepy@quent.stolpe
    ￼4nderseepy@clairas.alt
    ￼4nderseepy@sinigangster_
    ￼4nderseepy@krankshanks
    ￼4nderseepy@jayyyx.2
    ￼4nderseepy@jasperrr.t
    ￼
    sean21._@sison.sean
    ￼
    sean21._@banh_.bao
    ￼
    sean21._@axcura
    ￼
    fresshwater@lilchinki
    ￼
    fresshwater@thenotsogreatadrian
    ￼
    fresshwater@rad_sai
    ￼
    fresshwater@derius.j
    ￼
    fresshwater@dylankhang
    ￼
    fresshwater@vtonpadilla
    ￼
    fresshwater@chromeheartjaime
    ￼
    jordan.mattheww@sakura_pangelinan
    ￼
    jordan.mattheww@darrenndc
    ￼
    jordan.mattheww@jtjtc
    ￼
    jordan.mattheww@nateramos22
    ￼
    jordan.mattheww@danielblores
    ￼
    jordan.mattheww@rafsrecaps
    ￼
    maycoreyes_@guap0c
    ￼
    darrenndc@friedricejohn
    ￼
    maycoreyes_@imminentkhaos
    ￼
    darrenndc@jaacobsantiago
    ￼
    jordan.mattheww@friedricejohn
    ￼
    jordan.mattheww@jaacobsantiago
    ￼
    jordan.mattheww@andrewxsantoss
    ￼
    kwame.morrison@ryanchai_
    ￼
    kwame.morrison@_evangee
    ￼
    kwame.morrison@_bonifer
    ￼

    ￼
    kuyasian@hashtagsuperlit
    ￼
    kuyasian@inwasoki
    ￼
    kuyasian@jamz0326
    ￼
    kuyasian@kai.agliam
    ￼
    kuyasian@ry4ns.world
    ￼
    kuyasian@pookiew00kie2
    ￼dwade_wayne3@kauluvsmatcha
    ￼dwade_wayne3@kaylvrv
    ￼
    kuyasian@axron.lxe
    ￼dwade_wayne3@kkvrkluvsmoneyyy
    ￼
    kuyasian@r41den15
    ￼dwade_wayne3@wzv.ee
    ￼dwade_wayne3@kvyzoa
    ￼
    kuyasian@el_nano08__
    ￼dwade_wayne3@_gene.rafa
    ￼
    kuyasian@mr_.mcgrath
    ￼dwade_wayne3@1of1raven
    ￼dwade_wayne3@quocbui15
    ￼
    kuyasian@w4yne.ee
    ￼dwade_wayne3@jaelen_claire
    ￼
    kuyasian@nathantfrancoo_
    ￼
    kuyasian@kvyzoa
    ￼
    kuyasian@kuhtreenuh__
    ￼dwade_wayne3@fuckyouandyourpiercings
    ￼
    marcsuniverse@larsrodriguez
    ￼
    marcsuniverse@ryvnvelvrde
    ￼
    marcsuniverse@ruccimanee
    ￼
    marcsuniverse@melvinvngelo
    ￼
    marcsuniverse@cjdvvv
    ￼
    marcsuniverse@belleza310
    ￼
    marcsuniverse@brianguanlao
    ￼
    marcsuniverse@jerrelspov
    ￼
    marcsuniverse@marynevergrace
    ￼
    marcsuniverse@notredknapp
    ￼
    marcsuniverse@michaelvita
    ￼
    marcsuniverse@chris_resula
    ￼
    gavinbingen@dez_zuehlke
    ￼
    gavinbingen@bradenbingen
    ￼
    gavinbingen@ihateyounesto
    ￼
    gavinbingen@huhvro
    ￼
    gavinbingen@strive.xyz
    ￼
    gavinbingen@colinmarone
    ￼
    gavinbingen@erictrxnn
    ￼
    gavinbingen@gio.gonzalez_08
    ￼c.lwolfe@mariotofuyu
    ￼c.lwolfe@ali.habila16
    ￼c.lwolfe@hawk.roberts
    ￼c.lwolfe@mucrocs
    ￼
    kwame.morrison@nthonyha
    ￼
    kwame.morrison@alanphantastic
    ￼c.lwolfe@john.box123
    ￼
    kwame.morrison@theskreetpoet
    ￼c.lwolfe@jxydxn816
    ￼
    kwame.morrison@jrm_81
    ￼
    kwame.morrison@danchen_01
    ￼
    kwame.morrison@realeddiecao
    ￼
    kwame.morrison@ez6as
    ￼
    kwame.morrison@ericdnguyenn
    ￼
    kwame.morrison@luhbriqq
    ￼
    kwame.morrison@unu.noh
    ￼
    kwame.morrison@andy.lxm
    ￼
    kwame.morrison@ianjhs
    ￼c.lwolfe@longquachnguyen
    ￼c.lwolfe@tylv.er
    ￼c.lwolfe@spinachthekid.spam
    ￼
    jr92_ncap@munoznessa
    ￼
    marcsuniverse@zenny.pc
    ￼dez_zuehlke@drilltime840
    ￼dez_zuehlke@thevaughnwilliston
    ￼dez_zuehlke@connor.hull
    ￼dez_zuehlke@jseangreen
    ￼dez_zuehlke@masonn.brown
    ￼dez_zuehlke@bradygerritson
    ￼
    marcsuniverse@rjnotrj
    ￼dez_zuehlke@isaac.howe04
    ￼dez_zuehlke@coltonslatt
    ￼
    marcsuniverse@d.s.writes
    ￼
    rrestaurantt@trlnoa
    ￼
    marcsuniverse@kesdelr
    ￼
    marcsuniverse@strawbuhni
    ￼
    nfrc_oshiji@purplephantom_456 @injuns2k
    ￼
    ncky.an@jesoncarino
    ￼
    evelynsuzettem@nestor.bajo_and_guitar
    ￼
    lntensively@intergains
    ￼
    lntensively@undesireble
    ￼
    lntensivelyneed these
    ￼
    luvv4ishan@ariel.quack
    ￼
    luvv4ishan@evre.xrx
    ￼
    luvv4ishan@_sebastians17_
    ￼
    luvv4ishan@1tzax_
    ￼
    luvv4ishan@daraghav23
    ￼
    ariel.quack@rishab_manian
    ￼
    luvv4ishan@im_.vaibhav._
    ￼
    ariel.quack@kavinkwak
    ￼
    ariel.quack@jitae324
    ￼
    luvv4ishan@riiyavr
    ￼
    luvv4ishan@_amir1614
    ￼
    luvv4ishan@spencer_maffeo
    ￼
    luvv4ishan@evre.xrx
    ￼
    luvv4ishan@d1looksmaxxer
    ￼
    luvv4ishan@probably._.nate
    ￼aanthonyle@krispy.keane
    ￼
    ariel.quack@notvihnn
    ￼
    luvv4ishan@dallasc.c
    ￼
    ariel.quack@jaydenli117
    ￼aanthonyle@mmariavle
    ￼aanthonyle@sarvvvvvvvv
    ￼
    ariel.quack@davidchuckswanjane
    ￼
    ariel.quack@jinnyboi_
    ￼
    ariel.quack@caaalbeb
    ￼aanthonyle@jordan_magbag
    ￼aanthonyle@alexledp
    ￼aanthonyle@aludawg17
    ￼aanthonyle@dd_nation
    ￼aanthonyle@rzhangwave
    ￼aanthonyle@athanble
    ￼
    ariel.quack@jamestong08
    ￼aanthonyle@andy.lxm
    ￼
    ariel.quack@i.van_leman
    ￼
    ariel.quack@rianjain_08
    ￼
    ariel.quack@darshanpatel1_
    ￼aanthonyle@kennethdangg
    ￼
    ariel.quack@vjujuboards
    ￼
    s0sa.466@alexander_mardjonovic
    ￼
    ariel.quack@dallasc.c
    ￼
    hoorayforclay@ariel__austin
    ￼
    hoorayforclay@beulaneug
    ￼
    hoorayforclay@axa18.1
    ￼
    s0sa.466@photosoulja
    ￼
    s0sa.466@alex.fon
    ￼
    s0sa.466@_octavio2003
    ￼
    s0sa.466@chris_castro918
    ￼
    brownmanray@jun671k
    ￼
    brownmanray@in_dexlab
    ￼
    brownmanray@parismanuel_vs_theworld
    ￼
    brownmanray@snarericc
    ￼
    brownmanray@deathtokarsa
    ￼
    luvv4ishan@ncortez472
    ￼
    luvv4ishan@4nderseepy
    ￼
    luvv4ishan@luvv4ishan
    ￼
    luvv4ishan@chiefkeeefstan
    ￼
    ethann_shaw@jake.perez8
    ￼
    ethann_shaw@__enrique
    ￼
    ethann_shaw@peyton_sh
    ￼
    ethann_shaw@_cs_22
    ￼jomai__@cpt.alex__
    ￼jomai__@divakbg
    ￼jomai__@avi.ahiyya
    ￼jomai__@jessesmall1
    ￼jomai__@prodk3
    ￼jomai__@hamswizzz
    ￼jomai__@savannahh.graceee
    ￼jomai__@lengptaing
    ￼jomai__@ceciliandang
    ￼
    bashirthebandit@fuckyouandyourpiercings
    ￼
    bashirthebandit@bewareofthedog4
    ￼
    bashirthebandit@tristanspamusubi
    ￼
    bashirthebandit@sexyaszmf
    ￼
    bashirthebandit@_9ohn
    ￼
    bashirthebandit@ilove.korn666
    ￼
    bashirthebandit@br1qnz
    ￼
    bwong.20@francis.yeh
    ￼
    bwong.20@jjoon_l_ee
    ￼
    bwong.20@johnnybboiii
    ￼
    bwong.20@john_hwang02
    ￼
    bwong.20@trietmnguyen_ d
    ￼
    bwong.20@kevinjqyu
    ￼
    bwong.20@derek._.wang
    ￼
    bwong.20@ninahmgs
    ￼
    bwong.20@_trishthefish_
    ￼
    bwong.20@ttt.ranng
    ￼
    bwong.20@mai.cecilia
    ￼
    bwong.20@michellexau
    ￼
    bwong.20@dejenirate
    ￼
    bwong.20@lizzanyaa
    ￼
    bwong.20@marlene.carsenlee
    ￼methstones@joshdarealest444 @joshdarealest777 @d00mstone. Help a brother out g
    ￼
    calum_h7123@kasia.wykret
    ￼
    calum_h7123@kasia.wykret
    ￼
    calum_h7123@kasia.wykret
    ￼
    calum_h7123@kasia.wykret
    ￼
    calum_h7123@kasia.wykret
    ￼
    theskreetpoet@jomwrld
    ￼
    theskreetpoet@onlyphanss
    ￼
    theskreetpoet@danchen_01
    ￼
    theskreetpoet@muffolifto ￼
    joellloydclarke@bjembra
    ￼
    joellloydclarke@pechonis
    ￼
    tohtorou@5.714_
    ￼
    tohtorou@shesconcerned
    ￼
    tohtorou@champagnenutter
    ￼
    tohtorou@minaaweena
    ￼
    joellloydclarke@levikemp
    ￼
    joellloydclarke@samclarke2005
    ￼
    joellloydclarke@rae.in4k
    ￼
    jnh_dav1es@martha.ashrafff
    ￼
    jjjjulian___@lyralimcolioc
    ￼
    carmenreece@romeureece Pretty Pants

    carmenreece@franklindianne 

    carmenreece@hardin5925

    """

    story_reshares = ['Wonginthong', 'Oreodasillygoose' , '__benhanma__', '1der9c', '4nderseepy', 'Jenni', 'Brownmanray', 'Fresshwater', 'Kwame.morrison', 'Dwade_wayne3', 'Marcsuniverse', 'C.lwolfe', 'Dez_zuehlke', 'Evelynsuzettem', 'Leoarmdz', 'Ne5t0r_', 'LUVV4ISHAN', 'Aanthonyle', 'Jomai__', 'Scvtta', 'Bwong.20', 'Calum_h7123', 'Wh0s_j1mmy', 'Jjjjulian___', 'Thehighherald', 'Zatlonnn', 'PBS.jayden', 'Austiinha', 'Alex', 'Nuyorkluv' , 'Bigb00ty_john', 'Think_ink1', 'Balabcoagaga' , 'Indio_zhensi', 'Sunnelkim' , 'Vamp3doutt', 'Andrew_liscio', 'Sk844u', 'Frank_fiend', 'Storm_rider81', 'Sakura_pangelinan', 'Sabho8', 'Towobou','theskreetpoet','theskreetpoet','theskreetpoet','theskreetpoet','theskreetpoet','theskreetpoet','theskreetpoet','theskreetpoet','theskreetpoet','theskreetpoet','theskreetpoet','theskreetpoet','theskreetpoet','theskreetpoet','theskreetpoet',]

    mentions = extract_entries(tags, story_reshares)
    # print(mentions)
    print('Out of', len(mentions), 'entries, the 2 winners are:')
    random_mentions = random.sample(mentions, 2)
    print(random_mentions)
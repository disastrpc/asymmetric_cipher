#!/usr/bin/env python

import cryutils, argparse, string, sys, os
from time import perf_counter as prog
from churner import KeyContainer, BlockHandler
from helper import Helper, Helper_Thread
from logging import log
from threading import Thread

def parse():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('-h','--help',dest='help',action='store_true')

    # mode arg
    parser.add_argument('mode',nargs='*')

    # gen mode
    parser.add_argument('-l','--lenght',default=1024,type=int,dest='keysize')
    parser.add_argument('-o','--output',dest='output')
    parser.add_argument('--force',action='store_true',dest='force')
    parser.add_argument('--print',action='store_true',dest='print')

    # en/de mode
    parser.add_argument('-f','--file',dest='input')
    parser.add_argument('--privatekey',dest='priv_key')
    parser.add_argument('--publickey',dest='pub_key')
    namespace = parser.parse_args()
    return namespace

def main():
    namespace = parse()
    if namespace.help:
        Helper.show_help()

    elif 'gen' in namespace.mode:
        repr(KeyContainer(1024,1726917693118203110852644560454016525004115359300824263296084065946873781184622504322522371051917142494394093810603312425182490138976308391110332614971794788367953963954640405753506718343322160891249771427327017993564339195970747899537634026455097966077921556910208570012072027120804529641388150204056275879744188250771911339580506488489290365280044988274639121672002746911359523512205578280205367899808644471799000772980742218181641451212673468173671082737792457054295777196743610706076218274169613668795529016650237820121777816081953272736938973826250329235743597402302678176894123805341495853141643362719511003647112017103674433126640714534510270386374025383894119128275193977338135943879785362663134457826690391291571380297361617732959779884293682100313863613044330460847387150627153297771463856431292004880348608813846896305271241812084283949342666692184352802050371674398538880775756832335481162598441114976335769004254730944745144104443745691393981667988410936513745493684589866975150546177995786505937261450100208759919482126671516048449906573887411773746290527030735332268199750593199117335135385611864258484192565534456512542688643786051652653382579818786462822347118037327993222349876402815514225450812047058272316350190579,17269176931182031108526445604540165250041153593008242632960840659468737811846225043225223710519171424943940938106033124251824901389763083911103326149717947883679539639546404057535067183433221608912497714273270179935643391959707478995376340264550979660779215569102085700120720271208045296413881502040562758797441882507719113395805064884892903652800449882746391216720027469113595235122055782802053678998086444717990007729807422181816414512126734681736710827377924570542957771967436107060762182741696136687955290166502378201217778160819532727369389738262503292357435974023026781768941238053414958531416433627195110036471109614955720967248444035430236361960995640422669278781028073143168477235350344566010248498450564035018065704367883204890644310632939186133785115806810790294591065440623763508570333844307632083531777169099369169725904948945901819915628188176883818096581169177761335279812323156177088211685873359568787751175419))
        
        # key_container = KeyContainer(namespace.keysize)
        # msg = "generating public and private keys......"
        # t = Helper_Thread('anim',msg)
        # t_start = prog()
        # t.start()
        # key_container.generate()
        # t_stop = prog()
        # t.kill()
        # t.join()
        
        # if namespace.force:
        #     key_container.to_file(namespace.output, overwrite=True)
        #     Helper.message_success_timed(t_start, t_stop)
        # elif namespace.print:   
        #     print(key_container.__repr__())  
        #     sys.stdout.write(key_container.__str__()+'\n')
        #     Helper.message_success_timed(t_start, t_stop)
        # else:
        #     key_container.to_file(namespace.output)
        #     Helper.message_success_timed(t_start, t_stop)

    elif 'en' in namespace.mode:
        kf = open(namespace.pub_key,'r')
        pub_key_path = kf.read()
        kf.close()
        
        with open(namespace.input,'r') as f:
            raw_data = f.read()
            encrypter = BlockHandler()
            cipher_text = encrypter.encrypt(raw_data, pub_key_path)
            print(cipher_text)


if __name__ == '__main__':
    main()   

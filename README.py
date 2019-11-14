from design_corpus import design
if __name__ == '__main__':
    ###################################### Readme ############################################
    # csv_path : A String. File path of huge speech database.
    # skip : An integer. skiphone, for example, tri-phone: skip=3
    # sorted_mode : An integer in [0, 1]. sorted by phone's type or phone's total number. 0 represents by type while 1 represents by number.
    # read_mode : A String. represents  LJSpeech data format or normal data format
    '''
    LJSpeech data format:
        wav_name1|sent1|sent1
        wav_name2|sent2|sent2 ...
    e.x.
        LJS_0001|I am a basketball player|I am a basketball player
        LJS_0002|I am xieyb|I am xieyb ...

    normal data format:
       wav_name1 sent1
       wav_name2 sent2 ...
    e.x.
        001.wav I am a basketball player
        002.wav I am xieyb ...
    '''
    # log_file : None or String. String represents log file path.
    # if None, convert rate and count results do not write into file, else String, convert rate and count results write into log file.
    ###################################### Readme ############################################

    # e.x.
    #####################ljspeech_data_format_handle#####################
    # handle1 = create(csv_path='data/LJSpeech-1.1/metadata.csv', skip=2, read_mode='ljspeech', sorted_mode=0)
    #####################normal_data_format_handle#######################
    handle1 = design(csv_path='../data/LJSpeech-1.1/metadata.csv', skip=3, read_mode='ljspeech', sorted_mode=0, log_file='./logs/1h-3phone-ljs.log')

    # bynum : An integer. which represents the needed sentense number.
    #sents = handle1.get_sent(num=2400, get_mode='bynum')
    # bydur
    # wavs_dir : String. Total wav files directory.
    # duration : A number. required duration time. Unit: h.
    # sr : An integer. sample rate.
    sents = handle1.get_sent(wavs_dir='../data/LJSpeech-1.1/wavs/', duration=1, sr=22050, get_mode='bydur')

    # fpath : A String. file path which restore handled sentenses.
    # sents : A List. includes handled sentenses.
    handle1.res2file(fpath='./design_lib/1h-3phone-ljs.txt', sents=sents)

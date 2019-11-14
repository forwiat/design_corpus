from design_corpus import design

#test1: get 3phone sorted by total selected 0.5h duration.
test_design = design(csv_path='metadata.csv', skip=3, read_mode='ljspeech', sorted_mode=0, log_file='./logs/test_ljspeech_3phone_bytype_by0.5dur.log')
sentences = test_design.get_sent(num=None, wavs_dir='../data/LJSpeech-1.1/wavs/', duration=0.5, sr=22050, get_mode='bydur')
test_design.res2file(fpath='./design_lib/test_ljspeech_3phone_bytype_by0.5dur.csv', sents=sentences)


#test2: get 2phone sorted by type selected 500 number of sentenses.
test_design = design(csv_path='metadata.csv', skip=2, read_mode='ljspeech', sorted_mode=1, log_file='./logs/test_ljspeech_2phone_bytotal_by500num.log')
sentences = test_design.get_sent(num=500, wavs_dir=None, duration=None, sr=None, get_mode='bynum')
test_design.res2file(fpath='./design_lib/test_ljspeech_2phone_bytotal_by500num.csv', sents=sentences)

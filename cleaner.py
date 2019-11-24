# -*- coding: utf-8 -*-

import preprocessor as p
import re
from emoji_list import emojis


class cleaning(emojis):
  def __init__(self, tweets):
    super(cleaning, self).__init__()
    self.tweets=tweets
    self.clean_tweets=[]
    self.basic_clean_tweets=[]
    for _ in self.tweets:
      tmp=self.basic_clean(_.full_text)
      if tmp [0:2] != 'RT':
        _.clean_text=tmp
        self.basic_clean_tweets.append(_)
    self.complete_cleaner()


  def basic_clean(self, sentence):
    p.set_options(p.OPT.URL, p.OPT.SMILEY)
    tmp=p.clean(sentence)
    tmp=re.sub(r"via @","@",tmp)
    return(tmp) 

  def word_clean(self, sentence):
    p.set_options(p.OPT.HASHTAG,p.OPT.MENTION)
    tmp=p.clean(sentence)
    emoji_list=self.emojis_sub_word
    emoji_list.update({"\s\s+":" "})
    for key,val in emoji_list.items():
      tmp=val.join(tmp.split(key))
    return([_.lower() for _ in (re.split(r'[`\-=~!$%^&*()_+\[\]{};\\\:"|<,./<>? ]',tmp)) if _ !=""])

  def sentence_clean(self, sentence):
    p.set_options(p.OPT.MENTION)
    tmp=p.clean(sentence)
    emoji_list=self.emojis_sub_sentence
    emoji_list.update({"#":"","\s\s+":" "})
    for key,val in emoji_list.items():
      tmp=val.join(tmp.split(key))
    return(tmp)
  
  def complete_cleaner(self):
    for _ in self.basic_clean_tweets:
      _.words=(self.word_clean(_.clean_text))
      tmp=self.sentence_clean(_.clean_text)
      _.clean_text=(" ".join([_.lower() for _ in (re.split(r'[`\-=~!$%^&*()_+\[\]{};\\\:"|<,/<>? ]',tmp)) if _ !=""]))
      self.clean_tweets.append(_)

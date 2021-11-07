# SeekTruth.py : Classify text objects into two categories
#
# PLEASE PUT YOUR NAMES AND USER IDs HERE
#Purnima Surve-pursurve
#Teammembers:Tejaswy Ghanta-lghanta Shruthi Gutta-shrgutta
#
# Based on skeleton code by D. Crandall, October 2021
#
import re
import sys
import math
import numpy as np
from decimal import Decimal

def load_file(filename):
    objects=[]
    labels=[]
    with open(filename, "r") as f:
        for line in f:
            parsed = line.strip().split(' ',1)
            labels.append(parsed[0] if len(parsed)>0 else "")
            objects.append(parsed[1] if len(parsed)>1 else "")

    return {"objects": objects, "labels": labels, "classes": list(set(labels))}


def deceptive_vocabulary(train_data):                                                    #return a dictionary of unique words in deceptive reviews with their frequencies
    split_string=[]
    vocab_unique_words_decep = []
    total=[]
    for i in train_data["objects"]:
        j=train_data["objects"].index(i)
        total.append([w.lower() for w in re.split(r'[-.?!" ")(),390$4~125678]', i) if w])
        if train_data["labels"][j] != "truthful":
            split_string.append([w.lower() for w in re.split(r'[-.?!" ")(),390$4~125678]', i) if w])

    dec_vocabularyy = [item for i in split_string for item in i]
    vocab_unique_words_decep = list(dict.fromkeys(dec_vocabularyy))              # unique words in deceptive reviews
    dict_deceptive = {}
    for w in vocab_unique_words_decep:
        reviews_w = 0                                                            # counter
        for sentence in dec_vocabularyy:
            if w in sentence:
                reviews_w += 1
        dict_deceptive[w.lower()] =reviews_w

    return dict_deceptive

def truthful_vocabulary(train_data):                                             #return a dictionary of unique words in truthful reviews with their frequencies
    split_stringg=[]

    for i in train_data["objects"]:
        j=train_data["objects"].index(i)
        if train_data["labels"][j] != "deceptive":
            split_stringg.append([w.lower() for w in re.split(r'[-.?!" ")(),390$4~125678]', i) if w])

    truth_vocabularyy = [item for i in split_stringg for item in i]
    vocab_unique_words_truth = list(dict.fromkeys(truth_vocabularyy))
    dict_truthful = {}
    for w in vocab_unique_words_truth:
        treviews_w = 0  # counter
        for sentence in truth_vocabularyy:
            if w in sentence:
                treviews_w += 1
        dict_truthful[w.lower()] = treviews_w
    return dict_truthful


def testwords(test_data):                                                                        #Cleans and splits the test dataset
    total = []
    for i in test_data["objects"]:
        total.append([w.lower() for w in re.split(r'[-.?!" ")(),]390$4~125678', i) if w])
    total1=[item.split() for i in total for item in i]

    return total1

# classifier : Train and apply a bayes net classifier
#
# This function should take a train_data dictionary that has three entries:
#        train_data["objects"] is a list of strings corresponding to reviews
#        train_data["labels"] is a list of strings corresponding to ground truth labels for each review
#        train_data["classes"] is the list of possible class names (always two)
#
# and a test_data dictionary that has objects and classes entries in the same format as above. It
# should return a list of the same length as test_data["objects"], where the i-th element of the result
# list is the estimated classlabel for test_data["objects"][i]
#
# Do not change the return type or parameters of this function!
#
def classifier(train_data, test_data):
    # This is just dummy code -- put yours here!
    results=[]
    a=1
    count_decep = train_data["labels"].count("deceptive")  # no of deceptives in the data

    count_truth = train_data["labels"].count("truthful")  # no of truthfuls in the data
    count_total = count_decep + count_truth

    Pr_d=count_decep/count_total
    Pr_t=count_truth/count_total
    dec_vocfrq=deceptive_vocabulary(train_data)

    true_vocfrq=truthful_vocabulary(train_data)

    total_voc=len(dec_vocfrq)+len(true_vocfrq)

    truthful_prob={}
    deceptive_prob={}
    for word in true_vocfrq.keys():
        truthful_prob[word] = (true_vocfrq[word] + a) / (total_voc + 2)
    for word in dec_vocfrq.keys():
        deceptive_prob[word] = (dec_vocfrq[word] + a) / (total_voc + 2)
    testwds=testwords(test_data)
    reduced_words = []
    for i in testwds:                                                            #filtering the words from the training data which are present in the test data
        words = []
        for j in i:
            if j in dec_vocfrq:
                words.append(j)
            elif j in true_vocfrq:
                words.append(j)
            else:
                continue
        reduced_words.append(words)

    for i in range(len(reduced_words)):
        likelihood_deceptive = 1
        likelihood_true = 1
        for word in reduced_words[i]:
            likelihood_true = likelihood_true * Decimal(
                truthful_prob.get(word, a / (total_voc + 2)))
            likelihood_deceptive = likelihood_deceptive * Decimal(
                deceptive_prob.get(word, a / (total_voc + 2)))
        prob_dec_given_a_word = (likelihood_deceptive) * Decimal(Pr_d)           #Using Bayes Theorem ignoring the denominator since both deceptive and truthful posterior
                                                                                 # probabilities have the same denominator
        prob_truth_given_a_word = (likelihood_true) * Decimal(Pr_t)
        if prob_truth_given_a_word> prob_dec_given_a_word :
            results.append("truthful")
        else :
            results.append("deceptive")

    return results


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise Exception("Usage: classify.py train_file.txt test_file.txt")

    (_, train_file, test_file) = sys.argv
    # Load in the training and test datasets. The file format is simple: one object
    # per line, the first word one the line is the label.
    train_data = load_file(train_file)
    test_data = load_file(test_file)
    if(sorted(train_data["classes"]) != sorted(test_data["classes"]) or len(test_data["classes"]) != 2):
        raise Exception("Number of classes should be 2, and must be the same in test and training data")


    # make a copy of the test data without the correct labels, so the classifier can't cheat!
    test_data_sanitized = {"objects": test_data["objects"], "classes": test_data["classes"]}

    results= classifier(train_data, test_data_sanitized)

    # calculate accuracy
    correct_ct = sum([ (results[i] == test_data["labels"][i]) for i in range(0, len(test_data["labels"])) ])
    print("Classification accuracy = %5.2f%%" % (100.0 * correct_ct / len(test_data["labels"])))




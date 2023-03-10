# -*- coding: utf-8 -*-
"""KEAM_Data.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OThGgS7jqpFfI29Zncp1oVgbPFSl-PBz
"""
import os
import pandas as pd
from flask import Flask, jsonify
curr_dir = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)

cllg_sort_path = os.path.join(curr_dir,"cllg_sort.csv")
df_path = os.path.join(curr_dir,"df.csv")

cllg_sort = pd.read_csv(cllg_sort_path)
df = pd.read_csv(df_path)

@app.route('/predict/<int:rank>/<int:i>/<string:bestCollege_Pred>')
@app.route('/predict/<int:rank>/<int:i>')
def predict(rank,i,bestCollege_Pred="False"):
    bestCollegePred = bestCollege_Pred.lower() == "true"
    if(bestCollegePred):
      filtered_df = cllg_sort[cllg_sort['Rank'] >= rank]
    else:
      filtered_df = df[df['Rank'] >= rank]
    result = filtered_df[["College","Branch"]][:i].reset_index(drop = True)
    result_dict = result.to_dict(orient = "list")
    return jsonify(result_dict)

@app.route('/predict_by_college/<int:rank>/<int:i>/<string:college>')
def predict_by_college(rank,i,college):
  filtered_df = cllg_sort.loc[(cllg_sort["College"]==college)&(cllg_sort["Rank"]>rank)]
  result_dict = filtered_df[["College","Branch"]][:i].reset_index(drop = True).to_dict(orient="list")
  return jsonify(result_dict)


if __name__ == '__main__':
    app.run()

